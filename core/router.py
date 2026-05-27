from ai.llm import local_chat


ROUTER_PROMPT = """
You are an intent classifier.

Determine whether the user wants:

1. TOOL
- opening apps
- browser actions
- memory operations
- automation tasks

2. CHAT
- factual questions
- conversation
- explanations
- casual talking
- mathematical calculations

Return ONLY:

TOOL

or

CHAT
"""


TOOL_KEYWORDS = [

    "open",
    "play",
    "search",
    "remember",
    "recall",

    "where is",
    "where did",
    "where i kept",
    "where i keep",
    "tell me where",

    "youtube",
    "browser",
    "website",

    "click",
    "type",
    "press",

    "volume",
    "pause",
    "resume"
]


def classify_intent(command):

    lowered = command.lower()

    # Rule-based detection
    for keyword in TOOL_KEYWORDS:

        if keyword in lowered:

            return "TOOL"

    # LLM fallback                             #can you help me listen to music
    response = local_chat(
        ROUTER_PROMPT,
        command
    )

    response = response.strip().upper()

    if "TOOL" in response:

        return "TOOL"

    return "CHAT"