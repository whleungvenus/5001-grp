#import tkinter
import tkinter as tk
from tkinter import ttk




master = tk.Tk()
tabControl = ttk.Notebook(master)

tab1 = ttk.Frame(tabControl)            # Create a tab 
tabControl.add(tab1, text='Predict By Restaurant')      # Add the tab
tab2 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab2, text='Suggested by restautant type')
tabControl.pack(expand=1, fill="both") 

#Predict By Restaurant
tk.Label(tab1, text="Restaurant ID:").grid(row=0)
tk.Label(tab1, text="User you should find:").grid(row=1)
def clickPredictSubmit():
    lbl = tk.Label(tab1, text="123")
    lbl.grid(column=1, row=1)
e1 = tk.Entry(tab1)
tk.Button(tab1, 
          text='Submit', 
          command=clickPredictSubmit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
e1.grid(row=0, column=1)
#e2.grid(row=1, column=1)

#Suggestion

tk.Label(tab2, text="Restaurant Type:").grid(row=0)
tk.Label(tab2, text="User you should find:").grid(row=1)


def clickTypeSubmit():
    lbl = tk.Label(tab1, text="123")
    lbl.grid(column=1, row=1)
e1 = tk.Entry(tab1)
tk.Button(tab1, 
          text='Submit', 
          command=clickTypeSubmit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)




# li = ['王记','12','男']
# tree = ttk.Treeview(tab2,columns=['1','2','3'],show='headings')
# tree.column('1',width=100,anchor='center')
# tree.column('2',width=100,anchor='center')
# tree.column('3',width=100,anchor='center')
# tree.heading('1',text='姓名')
# tree.heading('2',text='学号')
# tree.heading('3',text='性别')
# tree.insert('','end',values=li)
# tree.grid()


master.mainloop()