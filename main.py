from workflow import run_workflow


from workflow import run_workflow


def main():
    print("=== Glox Content Agent ===")

    title = input("\nEnter the original YouTube title: ").strip()

    if not title:
        print("Title cannot be empty.")
        return

    context = input("Enter the video context: ").strip()

    if not context:
        print("Context cannot be empty.")
        return

    result = run_workflow(title, context)

    print("\n" + result)


if __name__ == "__main__":
    main()
