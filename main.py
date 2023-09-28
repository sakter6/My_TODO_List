from tkinter import *
from tkinter import messagebox
# thst massage box is for when the user don't put anything in the text box.

def newTask():
    task = my_entry.get()
    if task != '':
        lb.insert(END, task)
        my_entry.delete(0, 'end')
    else:
        messagebox.showwarning('Please enter a task...')

def deleteTake():
    lb.delete(ANCHOR) # this will delete any take in the anchor

#maine window
bx = Tk()#TK is the library and storing the value in bx
bx.geometry('600x500+500+200') # this line is for where(500 and 200) how big (600 and 500)the application will be
bx.title('my TODO list') # this line is the title of the application
bx.config(bg='#9c637c') # this is for what color my background is

frame = Frame(bx) # frame is the list box where I can add or remove more item
frame.pack(pady = 10)

# below are what is going to be in the frame of the listbox
lb = Listbox(
    frame,
    width = 30, # width of the frame
    height= 14, # hight
    font= ('Time',20), # font and size
    bd = 0,
    fg= '#464646',
    highlightthickness = 0,
    selectbackground ='#a6a6a6',
    activestyle= 'none',
)
lb.pack(side=LEFT, fill=BOTH)

task_list = [

]# empty list.

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)# this will add the scroll bar on the for the text box
sb.pack(side = RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)
# where the user put the item to put in the list of thing to do.
my_entry = Entry(
    bx,
    font=('time', 24)
)

my_entry.pack(pady=20)

button_frame = Frame(bx)
button_frame.pack(pady=20)
# this is the button for adding text into the frame.
addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('time 14'),
    bg= '#c5f776',
    padx= 20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

# this is the button for deleting a text and it will use the def delet function using ANCHOR to pick which item to delet.
delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('time 14'),
    bg= '#ff8b61',
    padx=20,
    pady=10,
    command=deleteTake
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

bx.mainloop()

