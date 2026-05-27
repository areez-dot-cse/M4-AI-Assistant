from core.registry import TOOLS


def validate_plan(plan):

    # Basic structure check
    if "steps" not in plan:
        return False, "Plan missing steps"


    if not isinstance(plan["steps"], list):
        return False, "Steps must be a list"


    # Validate each step
    for step in plan["steps"]:

        if "tool" not in step:

            return False, "Step missing tool"


        if "parameters" not in step:

            return False, "Step missing parameters"


        tool_name = step["tool"]


        # Tool existence check
        if tool_name not in TOOLS:

            return False, f"Unknown tool: {tool_name}"


        if not isinstance(step["parameters"], dict):

            return False, "Parameters must be dictionary"


    return True, "Plan valid"