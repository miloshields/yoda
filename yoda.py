import sys
from openai import OpenAI

client = OpenAI()

def getChatCompletion(userInput):
    response = client.responses.create(
        model="o3-mini-2025-01-31",
        input=userInput,
        stream=True,
    )
    return response

def printResponse(response):
    for chunk in response:
        if chunk.type == 'response.output_text.delta':
            print(chunk.delta, end='', flush=True)

data = sys.stdin.read()
response = getChatCompletion(data)
printResponse(response)
print('\n')
