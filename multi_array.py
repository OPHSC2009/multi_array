from tkinter import*
import random 
root=Tk()
root.geometry("1000x1000")
root.title("Password Generator")

lbl=Label(root)
lbl.place(relx=0.5,rely=0.4,anchor=CENTER)
array=[[["1","2","5","6","4","9"],["!","@","#","$","%","^"],["Head","Tail"]]]
def generate():
    r1=random.randint(0,5)
    r2=random.randint(0,5)
    r3=random.randint(0,1)
    
    l1=array[0][0][r1]
    l2=array[0][1][r2]
    l3=array[0][2][r3]
    lbl["text"]=l1+l2+l3
    
    
btn=Button(root,text="Generate",command=generate)   
btn.place(relx=0.5,rely=0.7,anchor=CENTER)
root.mainloop()
    
    