from core.registry import TOOLS

def execute_plan(plan):

    results = []

    for step in plan["steps"]:

        tool_name = step["tool"]

        parameters = step["parameters"]


        # Tool existence check
        if tool_name not in TOOLS:

            result = f"Unknown tool: {tool_name}"

            results.append(result)

            continue


        try:

            tool_function = TOOLS[tool_name]

            result = tool_function(**parameters)

            results.append(result)


        except Exception as e:

            results.append(
                f"Error executing {tool_name}: {e}"
            )

    return results