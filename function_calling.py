from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()
key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key = key)

tools = [
    {
        "name" : "get_whether",
        "type" : "function",
        "description" : "Get the whether of the location",
        "parameters" : {
            "type" : "object",
            "properties" : {
                "location" : {
                    "type" : "string",
                    "description" : "The location for the temperature with its country like, Delhi, India"
                }
            },
            "required" : ["location"],
            "additionalProperties" :False
        },
    }
]

def get_whether(location):
    # Some logic to derive the temperature given location
    return "26"

request = client.responses.create(
    model = "gpt-4.1",
    input = [
        {"role" : "user", "content": "What is the whether like today in Paris?"}
    ],
    tools = tools 
)

# print(request.output)

tool_call = request.output[0]
args = tool_call.arguments
args = json.loads(args)
output = get_whether(args["location"])

input_messages = [{"role" : "user", "content": "What is the whether like today in Paris?"}]
input_messages.append(tool_call)
input_messages.append({
    "type" : "function_call_output",
    "call_id" : tool_call.call_id,
    "output" : str(output)
})

request_2 = client.responses.create(
    model = "gpt-4.1",
    input = input_messages,
    tools = tools 
)

print(request_2.output_text)

# 1. Design your Function Call Schema in OpenAPI json schema format
# 2. Call the api first time to see if the tool call is required
# 3. If the request.output is emptty, it means no tool is required and we can end the program
# 4. If it contains the tool call, extract it and create the output by extracting the arguments from tool call
# 5. Finally, generate a final answer for the user.
