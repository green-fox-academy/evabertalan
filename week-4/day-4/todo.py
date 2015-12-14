filename="task.txt"


def test_assert(expected,actual,message):
    if expected == actual:
        print('chek')
    else:
        print('Error:' + message)


def open_file():
    input_file = open(filename)
    input_text = input_file.read()
    input_file.close()
    return input_text


def write_file(todo_items):
    output_file = open(filename,'w')
    output_file.write('\n'.join(todo_items))
    output_file.close()


def add_todo(new_task=""):
    if new_task=="":
        new_task=input("IRJAD!: ")
        return add_todo(new_task)
    todo_items=open_file().split('\n')
    todo_items.append(new_task)
    write_file(todo_items)
    print('Ok!')

def list_todo():
    output = list_helper()
    for i in range(len(output)):
        if output[i][-1]=="X":
            print(i+1, ". [X] ", output[i][0:len(output[i])-1], sep="")
        else:
            print(i+1,'. [ ] ',output[i],sep = '')


def list_helper():
    todo_items=open_file().split('\n')
    output = []
    for item in todo_items:
        if item != '' and item[len(item)-1] != '*':
            output.append(item)
    return output


def remove_todo(task_id=""):
    items = list_helper()
    output = []
    if task_id=="":
        list_todo()
        task_id=input("Valaszd ki az eltavolitando sorszamat!: ")
        return remove_todo(task_id)
    task_id=int(task_id)
    for i in range(len(items)):
        if i != (task_id - 1):
            output.append(items[i])
        else:
            output.append(items[i]+"*")
    write_file(output)

def completed_todo(task_id=""):
    items = list_helper()
    output = []
    if task_id=="":
        list_todo()
        task_id=input("Valaszd ki az eltavolitando sorszamat!: ")
        return completed_todo(task_id)
    task_id=int(task_id)
    for i in range(len(items)):
        if task_id != i+1:
            output.append(items[i])
        else:
            output.append(items[i] + " X")
    write_file(output)

def uncompleted_todo(task_id=""):
    items = list_helper()
    output = []
    if task_id=="":
        list_todo()
        task_id=input("Valaszd ki az eltavolitando sorszamat!: ")
        return uncompleted_todo(task_id)
    task_id=int(task_id)
    for i in range(len(items)):
        if task_id != i+1:
            output.append(items[i])
        else:
            output.append(items[i][:len(items[i])-1])
    write_file(output)

def list_removed_todo():
    output=open_file()
    removed=[]
    for i in range(len(output)):
        if output[i][-1]=="*":
            removed.append(output[i]t)
    print(removed)
