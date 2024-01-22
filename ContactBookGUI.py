

from tkinter import *
from tkinter import messagebox





def AddWindow():
    window1 = Toplevel()

    window1.geometry("800x800")
    window1.title("ADD CONTACT")
    window1.config(background="lightpink")
    label1 = Label(window1,text="Name",font="bold")
    label1.place(x=100,y=200)
    label2 = Label(window1,text="Phone No",font="bold")
    label2.place(x=100,y=300)
    label3 = Label(window1,text="Email",font="bold")
    label3.place(x=100,y=400)
    label4 = Label(window1,text="Address",font="bold")
    label4.place(x=100,y=500)
    entry1 = Entry(window1)
    entry1.place(x=300,y=200)
    entry2 = Entry(window1)
    entry2.place(x=300,y=300)
    entry3 = Entry(window1)
    entry3.place(x=300,y=400)
    entry4 = Entry(window1)
    entry4.place(x=300,y=500)
    add = Button(window1,text="ADD",command=lambda: AddContact(entry1, entry2, entry3, entry4))
    add.place(x=400,y=600)
    window1.mainloop()



def SearchWindow():
    window2 = Toplevel();
    window2.geometry("600x600")
    window2.title("SEARCH CONTACT")
    window2.config(background="lightpink")
    label11 = Label(window2,text="Enter Name to Search",font="bold 13")
    label11.place(x=100,y=100)
    entry11 = Entry(window2)
    entry11.place(x=280,y=100)
    search = Button(window2,text="search",command=lambda: SearchInFile(entry11,Listbox1))
    search.place(x=450,y=100)
    label22 = Label(window2,text="Contact Details:",font="bold 13")
    label22.place(x=100,y=150)
    Listbox1 = Listbox(window2,height=15,width=40,font="bold 10")
    Listbox1.place(x=100,y=200)
    window2.mainloop()



def ViewAllContacts():
    window3 = Toplevel()
    window3.geometry("600x600")
    window3.title("VIEW ALL CONTACTS")
    window3.config(background="lightpink")

    Listbox2 = Listbox(window3, height=50, width=50, font="bold 13")
    Listbox2.place(x=50, y=50)

    scrollbar = Scrollbar(window3, orient=VERTICAL, command=Listbox2.yview, width=20)
    scrollbar.place(x=550, y=50, height=500)

    Listbox2.config(yscrollcommand=scrollbar.set)

    with open("contact.json", "r") as json_file:
        data = json_file.readlines()

    contacts = [json.loads(line) for line in data]

    for contact in contacts:
        Listbox2.insert(END, f"Name: {contact['name']}")
        Listbox2.insert(END, f"Phone: {contact['contact']}")
        Listbox2.insert(END, f"Email: {contact['email']}")
        Listbox2.insert(END, f"Address: {contact['Address']}")
        Listbox2.insert(END, "")

    window3.mainloop()



def UpdateContactWindow():
    window4 = Toplevel()

    window4.geometry("800x800")
    window4.title("ADD CONTACT")
    window4.config(background="lightpink")
    label14 = Label(window4,text="Name",font="bold")
    label14.place(x=100,y=200)
    label24 = Label(window4,text="Phone No",font="bold")
    label24.place(x=100,y=300)
    label34 = Label(window4,text="Email",font="bold")
    label34.place(x=100,y=400)
    label44 = Label(window4,text="Address",font="bold")
    label44.place(x=100,y=500)
    entry14 = Entry(window4)
    entry14.place(x=300,y=200)
    entry24 = Entry(window4)
    entry24.place(x=300,y=300)
    entry34 = Entry(window4)
    entry34.place(x=300,y=400)
    entry44 = Entry(window4)
    entry44.place(x=300,y=500)
    update = Button(window4, text="UPDATE", command=lambda: UpdateContact(entry14.get(), {
        "email": entry24.get(),
        "contact": entry34.get(),
        "Address": entry44.get()
    }))
    update.place(x=400,y=600)
    window4.mainloop()





def deleteWindow():
        window5 = Toplevel()
        window5.geometry("600x600")
        window5.title("SEARCH CONTACT")
        window5.config(background="lightpink")
        label51 = Label(window5,text="Enter Name to Search",font="bold 13")
        label51.place(x=100,y=100)
        entry51 = Entry(window5)
        entry51.place(x=280,y=100)
        Delete = Button(window5,text="Delete",command=lambda: DeleteContact(entry51))
        Delete.place(x=450,y=100)
        window5.mainloop()






def AddContact(entry1,entry2,entry3,entry4):
    name = entry1.get()
    contact = entry2.get()
    email = entry3.get()
    address = entry4.get()
    with open("contact.json","a") as json_file:
        contact_details={"name":name,"contact":contact,"email":email,"Address":address}
        json.dump(contact_details,json_file)
        json_file.write("\n")
        messagebox.showinfo(title="SUCCESS",message="Contact Added successfully")



def SearchInFile(entry11, Listbox1):
    name = entry11.get()
    Listbox1.delete(0, END)

    with open("contact.json", "r") as json_file:
        data = json_file.readlines()

    contacts = [json.loads(line) for line in data]

    matching_contacts = [contact for contact in contacts if contact.get("name") == name]

    if matching_contacts:
        for contact in matching_contacts:
            Listbox1.insert(END, f"Name: {contact['name']}")
            Listbox1.insert(END, f"Phone: {contact['contact']}")
            Listbox1.insert(END, f"Email: {contact['email']}")
            Listbox1.insert(END, f"Address: {contact['Address']}")
            Listbox1.insert(END, "")
    else:
        Listbox1.insert(END, f"Contact with name '{name}' not found in the JSON file.")
        messagebox.showinfo(title="Contact not found",message="Contact with this name does not exist")

import json

def UpdateContact(name, updated_fields):
    with open("contact.json", "r") as json_file:
        data = json_file.readlines()

    contacts = [json.loads(line) for line in data]


    index_to_update = next((index for index, contact in enumerate(contacts) if contact.get("name") == name), None)

    if index_to_update is not None:

        contacts[index_to_update].update(updated_fields)


        with open("contact.json", "w") as json_file:
            json_file.writelines(json.dumps(contact) + "\n" for contact in contacts)

        messagebox.showinfo(title="UPDATE SUCCESSFUL",message="Contact updated successfully ")
    else:
        messagebox.showinfo(title="Contact not found",message="Contact with this name does not exist")




import json

def DeleteContact(entry51):
    name = entry51.get()

    with open("contact.json", "r") as json_file:
        data = json_file.readlines()

    contacts = [json.loads(line) for line in data]


    index_to_delete = next((index for index, contact in enumerate(contacts) if contact.get("name") == name), None)

    if index_to_delete is not None:

        del contacts[index_to_delete]


        with open("contact.json", "w") as json_file:
            json_file.writelines(json.dumps(contact) + "\n" for contact in contacts)

        messagebox.showinfo(title="SUCCESS",message="Contact deleted Successfully")
    else:
        messagebox.showinfo(title="Contact not found",message="Contact with this name does not exist")




window = Tk()

window.geometry("800x800")
window.title("CONTACT BOOK")
window.config(background="lightpink")


label = Label(window,text="CONTACT BOOK",font="bold  30")
label.place(x=250,y=100)

button2 = Button(window,text="VIEW ALL CONTACTS",font="bold",command=ViewAllContacts)

button2.place(x=300, y=300)
button3 = Button(window,text="SEARCH CONTACT",font="bold",command=SearchWindow)

button3.place(x=300, y=400)
button4 = Button(window,text="UPDATE CONTACT",font="bold",command=UpdateContactWindow)

button4.place(x=300, y=500)
button5 = Button(window,text="DELETE CONTACT",font="bold",command=deleteWindow)

button5.place(x=300, y=600)



button1 = Button(window,text="ADD NEW CONTACT",command=AddWindow,font="bold")

button1.place(x=300, y=200)
window.mainloop();


