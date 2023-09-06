# creates an empty list to store the tasks the user inputs
to_do_list = []

def display_welcome_message():
    """
    Function to display a welcome message
    """
    print("Welcome to your own personal TO-DO List")

def add_task():
    """
    Function to add a task to the to-do list
    """
    # User enters the task and the task the user inputed is stored in "task"
    task = input("Enter the task: ")
    # Appends the task the user inputed to the "to_do_list" list above 
    to_do_list.append(task)
    print(f"Task '{task}' has been successfully added to the to-do list.")


def remove_task():
    """
    Function to remove a task from the to-do list
    """


def dispaly_list():
    """
    Function to display the to-do list
    """



add_task()