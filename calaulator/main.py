import tkinter as tk

from PIL import Image
from PIL import ImageTk

but_width=80
but_heigh=80
#########################################
txt=""
def click(num):
    global txt
    txt=txt+str(num)
    equation.set(txt)

def equal():
    global txt
    txt=txt.replace('×','*')
    txt=txt.replace('÷','/')
    ans = str(eval(txt))
    equation.set(ans)
    txt=""

def all_clear():
    global txt
    txt=" " 
    equation.set(txt)


def clear():
    global txt
    txt=txt[:-1]
    equation.set(txt)





    



#####################################
back=tk.Tk()
back.geometry("370x550")
back.config(bg="chartreuse1")

ico = Image.open('icon2.ico')
photo = ImageTk.PhotoImage(ico)
back.wm_iconphoto(False, photo)

equation=tk.StringVar()
txt_field=tk.Entry(width=25,  textvariable=equation, bg="light blue",font=("Aerial",20),fg="black")
txt_field.place(x=10,y=10,width=350,height=50)


img_1=Image.open("1.png")
resized_image=img_1.resize((but_width,but_heigh))
resized_image_1=ImageTk.PhotoImage(resized_image)

but1=tk.Button(back,image=resized_image_1,width=but_width,height=but_heigh,command=lambda:click(1))
but1.place(x=10,y=170)



img_2=Image.open("2.png")
resized_image=img_2.resize((but_width,but_heigh))
resized_image_2=ImageTk.PhotoImage(resized_image)

but2=tk.Button(back,image=resized_image_2,width=but_width,height=but_heigh,command=lambda:click(2))
but2.place(x=100,y=170)


img_3=Image.open("3.png")
resized_image=img_3.resize((but_width,but_heigh))
resized_image_3=ImageTk.PhotoImage(resized_image)

but3=tk.Button(back,image=resized_image_3,width=but_width,height=but_heigh,command=lambda:click(3))
but3.place(x=190,y=170)


img_4=Image.open("4.png")
resized_image=img_4.resize((but_width,but_heigh))
resized_image_4=ImageTk.PhotoImage(resized_image)

but4=tk.Button(back,image=resized_image_4,width=but_width,height=but_heigh,command=lambda:click(4))
but4.place(x=10,y=260)


img_5=Image.open("5.png")
resized_image=img_5.resize((but_width,but_heigh))
resized_image_5=ImageTk.PhotoImage(resized_image)

but5=tk.Button(back,image=resized_image_5,width=but_width,height=but_heigh,command=lambda:click(5))
but5.place(x=100,y=260)


img_6=Image.open("6.png")
resized_image=img_6.resize((but_width,but_heigh))
resized_image_6=ImageTk.PhotoImage(resized_image)

but6=tk.Button(back,image=resized_image_6,width=but_width,height=but_heigh,command=lambda:click(6))
but6.place(x=190,y=260)



img_7=Image.open("7.png")
resized_image=img_7.resize((but_width,but_heigh))
resized_image_7=ImageTk.PhotoImage(resized_image)

but7=tk.Button(back,image=resized_image_7,width=but_width,height=but_heigh,command=lambda:click(7))
but7.place(x=10,y=350)


img_8=Image.open("8.jpg")
resized_image=img_8.resize((but_width,but_heigh))
resized_image_8=ImageTk.PhotoImage(resized_image)

but8=tk.Button(back,image=resized_image_8,width=but_width,height=but_heigh,command=lambda:click(8))
but8.place(x=100,y=350)


img_9=Image.open("9.png")
resized_image=img_9.resize((but_width,but_heigh))
resized_image_9=ImageTk.PhotoImage(resized_image)

but9=tk.Button(back,image=resized_image_9,width=but_width,height=but_heigh,command=lambda:click(9))
but9.place(x=190,y=350)


img_0=Image.open("0.png")
resized_image=img_0.resize((but_width,but_heigh))
resized_image_0=ImageTk.PhotoImage(resized_image)

but0=tk.Button(back,image=resized_image_0,width=but_width,height=but_heigh,command=lambda:click(9))
but0.place(x=10,y=440)


###################################################
img_multiple=Image.open("multiple.png")
resized_image=img_multiple.resize((but_width,but_heigh))
resized_image_multiple=ImageTk.PhotoImage(resized_image)

but_multiple=tk.Button(back,image=resized_image_multiple,width=but_width,height=but_heigh,command=lambda:click("×"))
but_multiple.place(x=280,y=80)

img_prantezR=Image.open("r.png")
resized_image=img_prantezR.resize((but_width,but_heigh))
resized_image_prantezR=ImageTk.PhotoImage(resized_image)

but_prantezR=tk.Button(back,image=resized_image_prantezR,width=but_width,height=but_heigh,command=lambda:click(")"))
but_prantezR.place(x=190,y=80)

img_prantezL=Image.open("l.png")
resized_image=img_prantezL.resize((but_width,but_heigh))
resized_image_prantezL=ImageTk.PhotoImage(resized_image)

but_prantezL=tk.Button(back,image=resized_image_prantezL,width=but_width,height=but_heigh,command=lambda:click("("))
but_prantezL.place(x=100,y=80)



img_plus=Image.open("plus.png")
resized_image=img_plus.resize((but_width,but_heigh))
resized_image_plus=ImageTk.PhotoImage(resized_image)

but_plus=tk.Button(back,image=resized_image_plus,width=but_width,height=but_heigh,command=lambda:click("+"))
but_plus.place(x=280,y=260)


img_minus=Image.open("minus.png")
resized_image=img_minus.resize((but_width,but_heigh))
resized_image_minus=ImageTk.PhotoImage(resized_image)

but_minus=tk.Button(back,image=resized_image_minus,width=but_width,height=but_heigh,command=lambda:click("-"))
but_minus.place(x=280,y=170)



img_divid=Image.open("divide.png")
resized_image=img_divid.resize((but_width,but_heigh))
resized_image_divid=ImageTk.PhotoImage(resized_image)

but_divid=tk.Button(back,image=resized_image_divid,width=but_width,height=but_heigh,command=lambda:click("÷"))
but_divid.place(x=280,y=350)


img_equal=Image.open("equal.jpg")
resized_image=img_equal.resize((2*but_width+10,but_heigh))
resized_image_equal=ImageTk.PhotoImage(resized_image)

but_equal=tk.Button(back,image=resized_image_equal,width=2*but_width+10,height=but_heigh,command=equal)
but_equal.place(x=190,y=440)



img_dot=Image.open("dot.png")
resized_image=img_dot.resize((but_width,but_heigh))
resized_image_dot=ImageTk.PhotoImage(resized_image)

but_dot=tk.Button(back,image=resized_image_dot,width=but_width,height=but_heigh,command=lambda:click("."))
but_dot.place(x=100,y=440)

img_clear=Image.open("clear.png")
resized_image=img_clear.resize((but_width,but_heigh))
resized_image_clear=ImageTk.PhotoImage(resized_image)

but_clear=tk.Button(back,image=resized_image_clear,width=but_width,height=but_heigh,command=clear)
but_clear.place(x=10,y=80)








back.mainloop()

