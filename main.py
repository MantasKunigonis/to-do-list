print("Welcome to your To-Do List!\n")

while True:

    # Prompt to choose action (1 - New Task / 2 - View Tasks / 3 - Exit)
    action = input("What would you like to do?\n"
                   "1: New Task\n"
                   "2: View Tasks\n"
                   "3: Exit\n\n"
                   "Choice: ")

    if action == "1":

        # Prompt input
        task = input("Enter a task: ")

        # Append file
        with open("tasks.txt", "a") as file:
            file.write(task + "\n")

        # Notify success
        print("Task saved!\n")

    elif action == "2":

        try:

            # Read file
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()

            # Display tasks
            print("Tasks list:\n")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t.strip()}")

        except FileNotFoundError:
            print("No tasks found.\n")

    elif action == "3":
        print("Goodbye!\n")
        break

    else:
        print("Invalid choice. Try again. \n")

print()