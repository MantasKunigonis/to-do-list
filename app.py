# Import the Flask class from the flask module
from flask import Flask, render_template, request, redirect

# Create a new Flask web application instance
app = Flask(__name__)

# Define the route for the home page ("/")
@app.route("/")
def index():
    # Read tasks file
    try:
        with open("tasks.txt", "r", encoding="utf-8") as file:
            tasks = file.readlines()
    except FileNotFoundError:
        tasks = []
    return render_template("index.html", tasks=tasks)

# Define the route for adding tasks ("/add")
@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")  # Get task from form
    if task:
        with open("tasks.txt", "a", encoding="utf-8") as file:
            file.write(task + "\n")
    return redirect("/")

# Define the rout for removing tasks ("/remove")
@app.route("/remove/<int:task_id>", methods=["POST"])
def remove(task_id):
    try:
        # Read tasks from file
        with open("tasks.txt", "r", encoding="utf-8") as file:
            tasks = file.readlines()
        # Remove task
        tasks.pop(task_id)
        # Update tasks file
        with open("tasks.txt", "w", encoding="utf-8") as file:
            file.writelines(tasks)
    except FileNotFoundError:
        pass
    return redirect("/")

# Runs the application only if this file is executed directly
if __name__ == "__main__":
    app.run(debug=True)  # Start the server in debug mode