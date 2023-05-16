import os
import pickle

from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.faiss import FAISS


class DocumentIngestor:
    def __init__(self, store_path="./vectorstore.pkl", data_path="./FAQ"):
        self.store_path = store_path
        self.data_path = data_path
        self.vectorstore = None

        if os.path.exists(self.store_path):
            self.load_vectorstore()
        else:
            self.create_vectorstore()

    def load_vectorstore(self):
        with open(self.store_path, "rb") as f:
            self.vectorstore = pickle.load(f)

    def create_vectorstore(self):
        loader = DirectoryLoader(
            path=self.data_path, glob="**/*.txt", show_progress=True, loader_cls=TextLoader
        )

        raw_documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100,
        )
        documents = text_splitter.split_documents(raw_documents)

        embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("API_KEY"))

        self.vectorstore = FAISS.from_documents(documents, embeddings)

        with open(self.store_path, "wb") as f:
            pickle.dump(self.vectorstore, f)

    def get_vectorstore(self):
        return self.vectorstore

