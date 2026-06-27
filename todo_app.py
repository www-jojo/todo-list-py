#To-Do List
tasks = []
user = ""

#function to load user
def loadUser():
    try:
        with open("user.txt", "r") as file:
            user = file.read()
            print(f"Welcome back {user}!!")
    except FileNotFoundError: 
        with open("user.txt", "w") as file: # Creates an empty user.txt file 
            user = input("Enter your name ")
            file.write(user)
            print(f"Welcome {user}!")


#function to load tasks from file
def loadTasks():
    try:
        with open("tasks.txt", "r") as file:
            content = file.read()
            tasks.extend(content.splitlines())
    except FileNotFoundError: 
        with open("tasks.txt", "w") as file: # Creates an empty tasks.txt file 
            pass

#function to save tasks to file
def saveTasks():
    print("Saving tasks...")
    try:
        with open("tasks.txt", "w") as file:
            content = "\n".join(tasks)
            file.write(content)
    except FileNotFoundError:
        print("File not found")
        
# menu display
def showMenu():
    print('\n--------------MENU-----------------')
    print("\nSelect one of the following options")
    print("-----------------------------------")
    print("\n1. add task\n2. remove task\n3. view tasks\n4. exit")

# function to add tasks
def addTask():
    task = input("Enter task: ")
    tasks.append(task)
    print(f"{task} has been added to your to do list")

# function to view exsisting tasks
def viewTasks():
    if not tasks:
        print(f"You have no tasks today {user}")
    else:
        print("-------TODAY'S TASKS--------\n")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# function to remove tasks
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

# main program

loadUser()
loadTasks()

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
        saveTasks()
        print(f"Byee {user}! 👋")
        break
    else:
        print("Invalid choice. Try again")

