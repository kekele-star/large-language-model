from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name():
    llm = OpenAI(temperature=0.7)

    name = llm("I have a cat pet and i want a cool name for it. Sugggest to me five cool names for my pet.")

    return name

    