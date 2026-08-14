import json

from config import client, MODEL_NAME
from prompts import ANALYZER_PROMPT


def analyze_content(title, context):

    prompt = ANALYZER_PROMPT.format(
        title=title,
        context=context
    )

    response = client.chat.send(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        raise ValueError(
            f"Analyzer returned invalid JSON:\n{content}"
        )