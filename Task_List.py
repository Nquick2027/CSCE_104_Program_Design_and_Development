# TODO: Start with an empty list
task_list = []

print('Welcome to the tsk list app! Let me help you get started.\n')

# TODO: Prompt the user for the first task
first_task = input('Enter the first task: ')
    
# TODO: Add that task to the list
task_list.append(first_task)

# Loop Begins Here
while True:
    # TODO: 4 options: add, remove, view, quit
    print('\nHere are your options:')
    print('1) Create a new task \n2) Remove a task \n3) View the list \n4) Quit')
    choice = input('Enter your choice: ')

    if choice == '1':
        u_task = input('\nEnter a task: ')
        task_list.append(u_task)
        print('There are {} two item(s) in the list'.format(len(task_list)))
    elif choice == '2':
        remove = input('\nType the full task you wish to remove (casing must be exact): ')
        task_list.remove(remove)
        print('There are {} two item(s) in the list'.format(len(task_list)))
    elif choice == '3':
        print('\nHere is your list: {}'.format(task_list))
    elif choice == '4':
        print('\nQuit')
        break
    else:
        print("\nInvalid option! Try again")

        # TODO: Loop the whole thing until the user picks to quit

# Loop Ends Here