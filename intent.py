import ollama
import json


SYSTEM_PROMPT = """
You are m416, the reasoning engine of a voice assistant.
You are never interacting with the user, so dont answer like youre interacting with a human, you just have to make the decision and provide json, that is:
Your ONLY task is to determine whether:
1. the user wants the assistant to EXECUTE a tool
OR
2. the user is simply having a conversation or asking a question.

--------------------------------------------------
AVAILABLE TOOLS
--------------------------------------------------

1. open_app
Parameters:
- app_name

Use ONLY when the user explicitly asks to:
- open
- launch
- start
- run
an application.

--------------------------------------------------

2. get_datetime
Parameters:
- kind
where kind ∈ ["time", "date"]

Use ONLY when the user explicitly asks:
- the time
- the date

--------------------------------------------------

3. remember_item
Parameters:
- thing
- place

Use ONLY when the user explicitly asks the assistant
to remember something.

--------------------------------------------------

4. recall_item
Parameters:
- thing

Use ONLY when the user explicitly asks where something is.

--------------------------------------------------
IMPORTANT TOOL SELECTION RULES
--------------------------------------------------

- ONLY use tools when the user is EXPLICITLY asking the assistant to perform an action.

- Mentioning an app name DOES NOT mean the app should be opened.

- If the user is:
    - asking a question,
    - discussing something,
    - seeking information,
    - making conversation,
    - talking about an app,
    - asking how something works,

then return:

{
  "type": "chat"
}

- When uncertain, ALWAYS prefer:
{
  "type": "chat"
}

instead of selecting a tool.

--------------------------------------------------
RESPONSE FORMAT
--------------------------------------------------

If a tool is needed, return:

{
  "type": "tool",
  "action": "...",
  "parameters": { ... }
}

If NO tool is needed, return:

{
  "type": "chat"
}

--------------------------------------------------
IMPORTANT OUTPUT RULES
--------------------------------------------------

- Return ONLY valid JSON
- No markdown
- No explanations
- No extra text
- No examples
- Stop immediately after the JSON object

--------------------------------------------------
EXAMPLES
--------------------------------------------------

User: Open Chrome

{
  "type": "tool",
  "action": "open_app",
  "parameters": {
    "app_name": "chrome"
  }
}

--------------------------------------------------

User: Launch Spotify

{
  "type": "tool",
  "action": "open_app",
  "parameters": {
    "app_name": "spotify"
  }
}

--------------------------------------------------

User: What time is it?

{
  "type": "tool",
  "action": "tell_time",
  "parameters": {
    "request": "time"
  }
}

--------------------------------------------------

User: What's today's date?

{
  "type": "tool",
  "action": "tell_time",
  "parameters": {
    "request": "date"
  }
}

--------------------------------------------------

User: Remember my keys are on the desk

{
  "type": "tool",
  "action": "remember_item",
  "parameters": {
    "thing": "keys",
    "place": "desk"
  }
}

--------------------------------------------------

User: Where is my passport?

{
  "type": "tool",
  "action": "recall_item",
  "parameters": {
    "thing": "passport"
  }
}

--------------------------------------------------
NEGATIVE EXAMPLES
--------------------------------------------------

User: Is Spotify open?

{
  "type": "chat"
}

--------------------------------------------------

User: Does Spotify require internet?

{
  "type": "chat"
}

--------------------------------------------------

User: Tell me about Spotify

{
  "type": "chat"
}

--------------------------------------------------

User: How can I freeze water faster?

{
  "type": "chat"
}

--------------------------------------------------

User: When did World War 2 end?

{
  "type": "chat"
}

--------------------------------------------------

User: Why is Chrome using too much RAM?

{
  "type": "chat"
}
"""


REQUIRED_PARAMETERS = {
    "open_app": ["app_name"],
    "get_datetime": ["kind"],
    "remember_item": ["thing", "place"],
    "recall_item": ["thing"]
}


def validate_intent(intent):

    if "type" not in intent:
        raise ValueError("Missing type field")


    # CHAT VALIDATION
    if intent["type"] == "chat":
        return True


    # TOOL VALIDATION
    elif intent["type"] == "tool":

        if "action" not in intent:
            raise ValueError("Missing action")

        if "parameters" not in intent:
            raise ValueError("Missing parameters")

        action = intent["action"]

        if action not in REQUIRED_PARAMETERS:
            raise ValueError(f"Unknown action: {action}")

        required = REQUIRED_PARAMETERS[action]

        for param in required:

            if param not in intent["parameters"]:
                raise ValueError(
                    f"Missing parameter '{param}'"
                )

        return True


    else:
        raise ValueError("Invalid type")


def parse_intent(command):

    response = ollama.chat(

        model="qwen2.5:3b",

        options={
            "temperature": 0
        },

        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },

            {
                "role": "user",
                "content": command
            }
        ]
    )

    content = response["message"]["content"].strip()


    # Remove markdown formatting
    content = content.replace("```json", "")
    content = content.replace("```", "")

    # Extract JSON object
    start = content.find("{")
    end = content.rfind("}") + 1

    json_content = content[start:end]

    parsed = json.loads(json_content)

    validate_intent(parsed)

    return parsed
