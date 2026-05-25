import ollama


CHAT_SYSTEM_PROMPT = """
You are m416, a voice assistant.

Rules:
- Maximum 1 sentence.
- Maximum 15 words.
- Be concise.
- Speak naturally.
- Do not explain too much.
- Do not elaborate unless asked.
- Reply like Alexa or Siri.
"""


def generate_chat_response(command):

    response = ollama.chat(

        model="qwen2.5:3b",

        options={
            "temperature": 0.4,
            "num_predict": 40
        },

        messages=[

            {
                "role": "system",
                "content": CHAT_SYSTEM_PROMPT
            },

            {
                "role": "user",
                "content": command
            }
        ]
    )

    text = response["message"]["content"].strip()

    return text