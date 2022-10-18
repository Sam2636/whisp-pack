import openai
import os
from dotenv import load_dotenv   #for python-dotenv method
load_dotenv() 
openai.api_key=os.environ.get('API_KEY')

prompt="say this is a test"

response=openai.Completion.create(engine="text-davinci-001",prompt=prompt,max_tokens=6)

print(response)