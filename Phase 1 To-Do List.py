# Phase 1 To-Do List

tasks = []

# user input
user = input("Enter your name ")
print(f"Welcome {user}!")

# menu display
def showMenu():
    print('\n--------------MENU-----------------')
    print("\nSelect one of the following options")
    print("-----------------------------------")
    print("\n1. add task\n2. remove task\n3. view tasks\n4. exit")

def addTask():
    task = input("Enter task: ")
    tasks.append(task)
    print(f"{task} has been added to your to do list")

def viewTasks():
    if not tasks:
        print(f"You have no tasks today {user}")
    else:
        print("-------TODAY'S TASKS--------\n")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def removeTask():
    if not tasks:
        print("There's nothing on your to do list today!")
        return

    try:
        remove = int(input("Enter task number to delete: ")) - 1
        if remove >= 0 and remove < len(tasks):
            removed = tasks.pop(remove)
            print(f"\n{removed} was removed\n")
        else:
            print("Task not found")
    except ValueError:
        print("Enter a valid task number")

while True:
    showMenu()
    choice = input("\nEnter your choice (number): ")

    if choice == "1":
        addTask()
    elif choice == "2":
        removeTask()
    elif choice == "3":
        viewTasks()
    elif choice == "4":
        print(f"Byee {user}! 👋")
        break
    else:
        print("Invalid choice. Try again")

