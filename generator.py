import json

from openrouter import OpenRouter

from config import client, MODEL_NAME
from prompts import GENERATOR_PROMPT


def clean_json_response(content):
    """
    Clean common formatting problems returned by LLMs
    before parsing JSON.
    """

    content = content.strip()

    # Remove markdown code fences
    if content.startswith("```"):
        lines = content.splitlines()

        if lines and lines[0].startswith("```"):
            lines = lines[1:]

        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]

        content = "\n".join(lines).strip()

    # Find the actual JSON object
    start = content.find("{")
    end = content.rfind("}")

    if start != -1 and end != -1:
        content = content[start:end + 1]

    # Convert literal newlines inside JSON strings into escaped newlines.
    result = []
    inside_string = False
    escaped = False

    for char in content:

        if char == '"' and not escaped:
            inside_string = not inside_string

        if char == "\n" and inside_string:
            result.append("\\n")
        elif char == "\r" and inside_string:
            continue
        else:
            result.append(char)

        if char == "\\" and not escaped:
            escaped = True
        else:
            escaped = False

    return "".join(result)


def generate_content(title, context, analysis):

    prompt = GENERATOR_PROMPT.format(
        title=title,
        context=context,
        analysis=json.dumps(
            analysis,
            ensure_ascii=False,
            indent=2
        )
    )

    response = client.chat.send(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.8
    )

    content = response.choices[0].message.content

    try:

        cleaned_content = clean_json_response(content)

        return json.loads(cleaned_content)

    except json.JSONDecodeError as e:

        raise ValueError(
            f"Generator returned invalid JSON:\n"
            f"{content}\n\n"
            f"JSON Error: {e}"
        )