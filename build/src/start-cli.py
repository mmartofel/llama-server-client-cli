# Chat with an intelligent assistant in your terminal

import os 
from openai import OpenAI

server_url=os.environ.get("SERVER_URL","http://127.0.0.1:8000/v1/")

# Point to the local server
client = OpenAI(base_url=server_url, api_key="not-needed")

client

history = [
    {"role": "system", "content": "You are an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful."},
    {"role": "user", "content": "Hello, introduce yourself to someone opening this program for the first time. Be concise."},
]
print("\033[92;1m")

while True:
    completion = client.chat.completions.create(
        model="local-model", # this field is currently unused
        messages=history,
        temperature=0.7,
        stream=True,
    )

    new_message = {"role": "assistant", "content": ""}
    
    for chunk in completion:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
            new_message["content"] += chunk.choices[0].delta.content

    history.append(new_message)
    print("\033[91;1m")
    userinput = input("> ")
    if userinput.lower() in ["quit", "exit"]:
        print("\033[0mBYE BYE!")
        break
    history.append({"role": "user", "content": userinput})
    print("\033[92;1m")


