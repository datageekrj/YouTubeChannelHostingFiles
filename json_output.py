from openai import OpenAI
from dotenv import load_dotenv
import os
import json
from pydantic import BaseModel

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key = api_key)

class Company(BaseModel):
    name: str

class Person(BaseModel):
    name: str
    designation: str
    company: list[Company]
    interests: list[str]


# response = client.responses.create(
#     model = "gpt-4.1",
#     input = [
#         {"role" : "user", "content" : "Extract the following pieces of info from the given paragraph/text: {name : str, designation: str, company:str}. Vikas is a data scientist working at kotak."}
#     ]
# )

# res = json.loads(response.output_text)
# print(res["name"])

response = client.responses.parse(
    model = "gpt-4.1",
    input = [
        {"role" : "user", "content" : "Vikas is a data scientist working at kotak. He previously worked at nagarro. He likes reading and spending time in nature. "}
    ],
    text_format = Person
)
print(response.output_parsed)
print(response.output_parsed.model_dump())