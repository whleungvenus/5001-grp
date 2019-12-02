#import tkinter
import tkinter as tk
from tkinter import ttk
import pandas as pd
import csv
import math  
from tkinter import StringVar, IntVar
init = 0
userList = pd.read_csv('candidates.csv', usecols=['user_id', 'taste_group','user_name'])
print(userList)
tasteGroup = []
with open('taste_grp.csv', 'r') as f:
  reader = csv.reader(f)
  tastegrp = list(reader)

with open('taste_groups.csv', 'r') as f:
    reader = csv.reader(f)
    tasteGroup = list(reader)
    tasteGroup.remove(tasteGroup[0])
#print(tasteGroup)


master = tk.Tk()
tabControl = ttk.Notebook(master)

tab1 = ttk.Frame(tabControl)            # Create a tab 
tabControl.add(tab1, text='Recommendation')      # Add the tab
#tab2 = ttk.Frame(tabControl)            # Add a second tab
#tabControl.add(tab2, text='Suggested by restautant type')
tabControl.pack(expand=1, fill="both") 

var2 = tk.StringVar(value=tastegrp)

#创建Listbox

lb = tk.Listbox(tab1, listvariable=var2,selectmode='multiple') 
lb.grid(row=1,column=1,padx=(20,5),pady=20)

finalScore  = []

def clickPredictSubmit():
    selectList = [idx for idx in lb.curselection()]        
    finalScore  = []   
    for grp in tasteGroup:
        local_sum_square =0
        for idx, val in enumerate(grp):
            if(idx in selectList):
                #print(idx)
                local_sum_square = local_sum_square +((float(val)-1)*(float(val)-1))
            else:
                local_sum_square = local_sum_square +(float(val))*(float(val))
        #print(math.sqrt(local_sum_square))
        finalScore.append(math.sqrt(local_sum_square))
    #print('finalScore',min(finalScore))
    #print('finalScore',finalScore.index(min(finalScore)))
    showTargetUser(finalScore.index(min(finalScore)))   
text = StringVar()
text.set('')
tk.Label(tab1, text="User you should find:").grid(row=2)
tk.Label(tab1, textvariable=text).grid(row=2,column=1)

def showTargetUser(group):
    user =userList[userList['taste_group'] == group]['user_name'].sample().item()
    print(user)
    text.set(user)
   
  
        
   


                

tk.Button(tab1, 
          text='Submit', 
          command=clickPredictSubmit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
#e1 = tk.Entry(tab1)
#e1.grid(row=0, column=1)
#e2.grid(row=1, column=1)

#Suggestion

#tk.Label(tab2, text="Restaurant Type:").grid(row=0)
#tk.Label(tab2, text="User you should find:").grid(row=1)


#def clickTypeSubmit():
#    lbl = tk.Label(tab1, text="123")
#    lbl.grid(column=1, row=1)
#e1 = tk.Entry(tab1)
#tk.Button(tab1, 
#          text='Submit', 
#          command=clickTypeSubmit).grid(row=3, 
#                                    column=0, 
#                                    sticky=tk.W, 
#                                    pady=4)






master.mainloop()