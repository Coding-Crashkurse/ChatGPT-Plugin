import os
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from ingest import DocumentIngestor
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

ingestor = DocumentIngestor()
vectorstore = ingestor.get_vectorstore()
memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True, output_key='answer')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://chat.openai.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Message(BaseModel):
    query: str


@app.post("/chat")
async def chat(message: Message):
    qa = ConversationalRetrievalChain.from_llm(
    llm=OpenAI(model_name="text-davinci-003", temperature=0, openai_api_key=os.environ.get("API_KEY")),
    memory=memory,
    retriever=vectorstore.as_retriever(),
)
    result = qa({"question": message.query})
    return result["answer"]

@app.get("/logo.png")
async def plugin_logo():
    filename = "logo.png"
    return FileResponse(filename, media_type="image/png")


@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return Response(text, media_type="application/json")


@app.get("/openapi.yaml")
async def openapi_spec():
    with open("openapi.yaml") as f:
        text = f.read()
        return Response(text, media_type="text/yaml")
