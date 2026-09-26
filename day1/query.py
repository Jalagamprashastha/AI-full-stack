import ollama 
response = ollama.chat(
    model = "llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "types of ai in deep learning"       
        }
    ]
)
print(response["message"]["content"])