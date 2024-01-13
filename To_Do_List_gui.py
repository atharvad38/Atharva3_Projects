from tkinter import Tk
from tkinter import *
from tkinter import messagebox

window = Tk()

def view_Tasks():
    Listbox1.delete(0,'end')
    with open("List.txt","r",encoding="utf-8") as file:
        Tasks = file.readlines()
        if Tasks:
            for i,task in enumerate(Tasks,start=1):
                Listbox1.insert(END,f"{i}. {task.strip()}")
        else:
            messagebox.showwarning(title="EMPTY",message="Task list is empty")



def Add_Tasks():
    text = entry1.get()
    if text:
         with open("List.txt","a",encoding="utf-8") as file:
              file.write(text+"\n")
         messagebox.showinfo(title="Task added",message="Task added successfully !!!!")
         entry1.delete(0,'end')
         
    else:
        messagebox.showwarning(title="WARNING",message="Task cannot be empty")




def delete_tasks( ):



    try:

        task_indices = Listbox1.curselection()


        if task_indices:
            task_number = task_indices[0] + 1


            with open("List.txt", "r") as file:
                tasks = file.readlines()
                if 1 <= task_number <= len(tasks):
                    deleted_task = tasks.pop(task_number - 1)
                    with open("List.txt", "w",encoding="utf-8") as file:
                        file.writelines(tasks)
                    messagebox.showinfo(title="Deletion successful", message=f"Task '{deleted_task.strip()}' deleted.")
                    Listbox1.delete(0,'end')
                else:
                    messagebox.showwarning(title="ERROR", message="INVALID TASK NUMBER")
        else:
            messagebox.showwarning(title="WARNING", message="Please select a task!!!")
    except Exception as e:
        messagebox.showwarning(title="Exception occurred", message=str(e))




def MarkAsComplete():


    try:
        task_indices = Listbox1.curselection()

        if task_indices:
            for task_index in task_indices:
                task_number = task_index + 1

                with open("List.txt", "r") as file:
                    tasks = file.readlines()
                    if 1 <= task_number <= len(tasks):
                        tasks[task_number - 1] = tasks[task_number - 1].rstrip() + " ✓\n"
                        with open("List.txt", "w", encoding="utf-8") as file:
                            file.writelines(tasks)
                    else:
                        messagebox.showwarning(title="ERROR", message=f"INVALID TASK NUMBER: {task_number}")

            messagebox.showinfo(title="Success", message="Task(s) marked as completed")
            Listbox1.delete(0, 'end')
        else:
            messagebox.showwarning(title="WARNING", message="Please select a task!!!")
    except Exception as e:
        messagebox.showwarning(title="Exception occurred", message=str(e))







window.title("TO DO LIST");
window.config(background="lightblue")

window.geometry("700x1000")
label1 = Label(window, text="TO DO LIST", font=("Arial", 20, "bold"))
label1.place(x=200, y=100)

button2 = Button(window, text="ADD TASK",command=Add_Tasks)
button2.place(x=100, y=200)

button3 = Button(window, text="VIEW TASK",command=view_Tasks)
button3.place(x=100, y=300)

button4 = Button(window, text="DELETE TASK",command=delete_tasks)
button4.place(x=100, y=400)

button5 = Button(window, text="MARK AS COMPLETE",command=MarkAsComplete)
button5.place(x=100, y=500)



entry1 = Entry(window,width="40")
entry1.place(x=300,y=200)

Listbox1 = Listbox(window,height=15,width=40)
Listbox1.place(x=300,y=300)
instructions_label = Label(
    window,
    text="     \n"
         "INSTRUCTIONS:\n"
         "- Add tasks by entering text and clicking 'ADD TASK'\n"
         "- View tasks by clicking 'VIEW TASK'\n"
        
         "\n"
         "For Deleting and Marking the task as complete, follow the instructions below:\n"
         "- Click on 'VIEW TASK'\n"
         "- Select the task to delete or mark as complete\n"
         "- Click on 'DELETE TASK' or 'MARK AS COMPLETE' button as per your choice",
    font=("Arial", 12),
    wraplength=500  ,anchor="w",justify=LEFT
)
instructions_label.place(x=100, y=550)


window.mainloop()
