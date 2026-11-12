from langchain_groq import ChatGroq
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
app = FastAPI()
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key="GROQ_API_KEY"
)
app = FastAPI()
class chat(BaseModel):
    question : str
def generate_answer(question):
    return llm.invoke(f"""you are a helpful assitant in MSE-courses company,
we have in the company now:
-- AI course and it costs 200 dollars, it contains python and machine learning basics and numpy, pandas, amtplotlib and sklearn, and deep learning with pytorch.
-- front end course and costs 120 dollars, contains html, css, js and typescript, and frameworks like veo.js and react.js.
-- backend with node.js and costs 130 dollars.
-- fullstack costs 220 dollars and contains front end course and backend.
-- android mobile apps development costs 180 dollars, covers java and kotlin.
-- ios mobile app costs 200 dollars, covers swift.
-- c++ course costs 80 dollars, cvers the progrmming and computer sciencee fundmentals and data structure and oop.
-- generative ai course costs 80 dollars, covers LLMs APIs and prompt engineering and RAG and vector database.
if the question is out of the coursees or the company just say a do not know or say i am an assitant of the MSE-courses and this is out of the system and i am sorry.
if the user asks sbout courses that does not exist say we do not offer the 'the course name' course.
---- i want the answer to be clear and without any (* or / or " or ') and you can use the word 'and'.
answer the question with the language of the question.

the user question :

{question}.



answer:

""").content
@app.post("/generate")
def generate(request:chat):
    try:
        answer = generate_answer(request.question)
        return {
            "question":request.question, "answer": answer
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

