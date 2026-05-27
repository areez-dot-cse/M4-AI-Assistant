import ollama

LOCAL_MODEL = "qwen2.5:3b"

def local_chat(system_prompt, user_prompt):
    response = ollama.chat(
        model=LOCAL_MODEL,
        options={
            "temperature": 0
        },

        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )
    return response["message"]["content"]