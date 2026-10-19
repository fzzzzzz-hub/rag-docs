import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client=OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"),base_url="https://api.deepseek.com")
r=client.chat.completions.create(model="deepseek-chat",messages=[{"role":"user","content":"用最直白最不绕弯子最通俗的语言告诉我怎么年入五十万"}])
print(r.choices[0].message.content)
print(r.usage.prompt_tokens)
print("环境 OK")
