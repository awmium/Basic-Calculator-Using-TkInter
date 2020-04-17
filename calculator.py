from tkinter import *
window = Tk()
window.title("Calculator")
window.geometry('700x1300')

#from tkinter import font as tkf
#fnt = tkf.Font(family='Helvetica', size=10, weight='bold')

w=6
h=4

lbl= Label(window, text="",
width=40,height=7,
bg='gray80', anchor='e')
lbl.grid(columnspan=4,row=0)

lbl2 = Label(window, text="",
width=40,height=5,
bg='gray77', anchor='e')
lbl2.grid(columnspan=4,row=1)

def ACclicked():
	lbl.configure(text= '')
	lbl2.configure(text= '')

def Minusclicked():
	txt=lbl.cget('text')
	txt=txt[:-1]
	lbl.configure(text= txt)
	
def Modclicked():
	txt=lbl.cget('text') + "% "
	lbl.configure(text= txt)
	
def Divclicked():
	txt=lbl.cget('text') + "/"
	lbl.configure(text= txt)

def Oneclicked():
	txt=lbl.cget('text') + "1"
	lbl.configure(text= txt)

def Twoclicked():
	txt=lbl.cget('text') + "2"
	lbl.configure(text= txt)

def Threeclicked():
	txt=lbl.cget('text') + "3"
	lbl.configure(text= txt)
		
def Mulclicked():
	txt=lbl.cget('text') + "*"
	lbl.configure(text= txt)
	
def Fourclicked():
	txt=lbl.cget('text') + "4"
	lbl.configure(text= txt)
	
def Fiveclicked():
	txt=lbl.cget('text') + "5"
	lbl.configure(text= txt)
	
def Sixclicked():
	txt=lbl.cget('text') + "6"
	lbl.configure(text= txt)

def Subclicked():
	txt=lbl.cget('text') + "-"
	lbl.configure(text= txt)
	
def Sevenclicked():
	txt=lbl.cget('text') + "7"
	lbl.configure(text= txt)
	
def Eightclicked():
	txt=lbl.cget('text') + "8"
	lbl.configure(text= txt)

	
def Nineclicked():
	txt=lbl.cget('text') + "9"
	lbl.configure(text= txt)
	
def Addclicked():
	txt=lbl.cget('text') + "+"
	lbl.configure(text= txt)
	

	
def Pointclicked():
	txt=lbl.cget('text') + "."
	lbl.configure(text= txt)
	
def Zeroclicked():
	txt=lbl.cget('text') + "0"
	lbl.configure(text= txt)
	


btnAC = Button(window, text="AC",
width=w,height=h,
command=ACclicked)
btnAC.grid(column=0, row=2)

btnMinus = Button(window, text="<-", 
fg="orange",
width=w,height=h,
command=Minusclicked)
btnMinus.grid(column=1, row=2)

btnMod = Button(window, text="%", 
fg="orange",
width=w,height=h,
command=Modclicked)
btnMod.grid(column=2, row=2)

btnDiv = Button(window, text="/", 
fg="orange",
width=w,height=h ,
command=Divclicked)
btnDiv.grid(column=3, row=2)

btnOne= Button(window, text="1",
width=w,height=h,
command=Oneclicked )
btnOne.grid(column=0, row=3)

btnTwo = Button(window, text="2",
width=w,height=h,
command=Twoclicked )
btnTwo.grid(column=1, row=3)

btnThree = Button(window, text="3",
width=w,height=h,
command=Threeclicked)
btnThree.grid(column=2, row=3)

btnMul = Button(window, text="×" ,
fg="orange",
width=w,height=h,
command=Mulclicked)  
btnMul.grid(column=3, row=3)

btnFour = Button(window, text="4",
width=w,height=h,
command=Fourclicked)
btnFour.grid(column=0, row=4)

btnFive = Button(window, text="5",
width=w,height=h,
command=Fiveclicked)
btnFive.grid(column=1, row=4)

btnSix = Button(window, text="6",
width=w,height=h,
command=Sixclicked)
btnSix.grid(column=2, row=4)

btnSub = Button(window, text="-" , 
fg="orange",
width=w,height=h,
command=Subclicked)
btnSub.grid(column=3, row=4)

btnSeven= Button(window, text="7",
width=w,height=h,
command=Sevenclicked)
btnSeven.grid(column=0, row=5)

btnEight = Button(window, text="8",
width=w,height=h,
command=Eightclicked)
btnEight.grid(column=1, row=5)

btnNine = Button(window, text="9",
width=w,height=h,
command=Nineclicked)
btnNine.grid(column=2, row=5)

btnAdd = Button(window, text="+" , 
fg="orange",
width=w,height=h,
command=Addclicked)  
btnAdd.grid(column=3, row=5) 

def Cclicked():
	lbl.configure(text= '')	

btnC = Button(window, text="C",
width=w,height=h+1,
command=Cclicked)
btnC.grid(column=0, row=6)

btnZero = Button(window, text="0",
width=w,height=h+1,
command=Zeroclicked)
btnZero.grid(column=1, row=6)

btnPoint = Button(window, text=".", 
command=Pointclicked,
width=w,height=h+1)
btnPoint.grid(column=2, row=6)

def Equalclicked():
	string=lbl.cget('text')
	result=eval(string)
	print(result)
	lbl2.configure(text= result)

btnEqual= Button(window, text="=",
bg="orange", fg="black",
width=w,height=h+1,
command=Equalclicked)
btnEqual.grid(column=3, row=6)

	

window.mainloop()

