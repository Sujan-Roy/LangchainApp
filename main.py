#activate virtual machine by
# source venv2310Toyota/bin/activate
import os
from dotenv import load_dotenv
import openai
import langchain
from typing_extensions import Protocol
from langchain.llms import OpenAI 

load_dotenv()

my_key= os.getenv("OPENAI_API_KEY")
#print(my_key)
llm= OpenAI(temperature=0,openai_api_key=my_key)
text= "Central city of Japan?"
print(llm(text))