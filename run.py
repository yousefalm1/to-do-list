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
    # User enters the task they wish to remove and that will be stored in "task"
    task = input("Enter the task to remove: ")
    # checks if the  what the user inputed is in "to_do_list" 
    # If the task is present in the "to_do_list" the code below would run which will remove the task
    if task in to_do_list:
        to_do_list_remove(task)
    # If task is not found in the "to_do_list" it will print this statement out.
    else:
        print("Task not found in the to-do list")



def display_list():
    """
    Function to display the to-do list
    """
    # Checks if the "to_do_list" is empty, if it is print the statement below
    if not to_do_list:
        print("Your to-do list is empty.")
    # If "to_do_list" is not empty the code below will run
    else:
        print("To-DO List:")
        # This keeps track of the task numbers in the "to_do_list"
        count = 1
        # This for loop iterates over each item the user submited in the "to_do_list" and assigns it to "task"
        for task in to_do_list:
            # Inside the loop the print line it prints "1. Task 1", "2. Task 2" ....
            print(f"{count}. {task}")
            # After printing each task the count goes up by 1 for the next task
            count += 1



def main():
    display_welcome_message()
    
#  Creates an infinite loop until the user chooses to quits
while True:
    # Print the options so the user knows what to pick
    print("\nOptions.")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Display to-do-list")
    print("4. Quit")

    # The number the user input will be assigned to "Choice"
    choice = input("Enter Your choice:")

    # Checks what number the user inputed and calls the function linked to that number
    if choice == "1":
        # Calls the fuction to add a task
        add_task()
    elif choice == "2":
        # Calls the fuction to remove a task
        remove_task()
    elif choice == "3":
        # Calls the fuction to display tasks
        display_list()
    elif choice == "4":
        # Exit the loop and quit
        break 
    else:
        print("Invalid choice. Please try again.")