import json

from config import client, MODEL_NAME
from prompts import EVALUATOR_PROMPT


def evaluate_titles(original_title, title_1, title_2, context):

    prompt = EVALUATOR_PROMPT.format(
        original_title=original_title,
        title_1=title_1,
        title_2=title_2,
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
        temperature=0.4
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        raise ValueError(
            f"Evaluator returned invalid JSON:\n{content}"
        )