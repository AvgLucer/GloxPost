from analyzer import analyze_content
from generator import generate_content
from evaluator import evaluate_titles
from formatter import format_output


def run_workflow(title, context):

    # Step 1: Analyze the content
    analysis = analyze_content(title, context)

    # Step 2: Generate content
    generated = generate_content(
        title,
        context,
        analysis
    )

    # Step 3: Evaluate the generated titles
    evaluation = evaluate_titles(
        title,
        generated["titles"][0],
        generated["titles"][1],
        context
    )

    # Step 4: Format and save the final report
    report = format_output(
        title,
        context,
        analysis,
        generated,
        evaluation
    )

    return report