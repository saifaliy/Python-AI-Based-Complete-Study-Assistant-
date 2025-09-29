from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo")

def generate_quiz_questions(text: str, num_questions: int = 5) -> list:
    prompt = f"""
    Based on the following study material, generate {num_questions} quiz questions.
    Use clear language and vary the difficulty.

    Text:
    {text}
    """
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content.strip().split("\n")
