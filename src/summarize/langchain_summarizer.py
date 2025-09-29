import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI as OpenAIClient
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import HumanMessage

load_dotenv()

llm = OpenAIClient(model="gpt-3.5-turbo")  # Create once

def split_text(text: str, chunk_size=1000, chunk_overlap=100):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", " "]
    )
    return splitter.split_text(text)

def summarize_text(text: str) -> str:
    chunks = split_text(text)

    summaries = []
    for chunk in chunks:
        prompt = f"""
        Summarize the following study material into bullet points.

        Text:
        {chunk}
        """
        response = llm.invoke([HumanMessage(content=prompt)])
        summaries.append(response.content)

    return "\n\n".join(summaries)
