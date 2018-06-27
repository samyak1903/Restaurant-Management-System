from tkinter import *
import time
root =Tk()
root.geometry('1500x800')
root.title("Restaurant Management System")

f1=Frame(root,width=1500,height=60,bg='powder blue')
f1.pack(side=TOP)

f2 = Frame(root, width=900, height=800)
f2.pack(side=LEFT)

f3 = Frame(root, width=500, height=800)
f3.pack(side=RIGHT)

lbl1 = Label(f1, text="Restaurant Management System", font='Times 30 bold', fg='blue')
lbl1.grid(row=0, column=0)
current_time = time.asctime(time.localtime(time.time()))
lbl2 = Label(f1, text=current_time, font='Times 20 bold', fg='blue')
lbl2.grid(row=1, column=0)

txtE=Entry(f3,font='Arial 20 bold',bg='white',justify='right')
txtE.grid(columnspan=4)

btn0=Button(f3,padx=16,pady=16,bd=4,font=('ariel', 20 ,'bold'),text="0",bg="powder blue")
btn0.grid(row=5,column=0)

btn1=Button(f3,padx=16,pady=16,bd=4,font=('ariel', 20 ,'bold'),text="1",bg="powder blue",)
btn1.grid(row=4,column=0)

btn2=Button(f3,padx=16,pady=16,bd=4,font=('ariel', 20 ,'bold'),text="2",bg="powder blue")
btn2.grid(row=4,column=1)

btn3=Button(f3,padx=16,pady=16,bd=4,font=('ariel', 20 ,'bold'),text="3",bg="powder blue")
btn3.grid(row=4,column=2)

btn4=Button(f3,padx=16,pady=16,bd=4,font=('ariel', 20 ,'bold'),text="4",bg="powder blue")
btn4.grid(row=3,column=0)

btn5=Button(f3,padx=16,pady=16,bd=4,font=('ariel', 20 ,'bold'),text="5",bg="powder blue")
btn5.grid(row=3,column=1)

btn6=Button(f3,padx=16,pady=16,bd=4,font=('ariel', 20 ,'bold'),text="6",bg="powder blue")
btn6.grid(row=3,column=2)

btn7=Button(f3,padx=16,pady=16,bd=4,font=('ariel', 20 ,'bold'),text="7",bg="powder blue")
btn7.grid(row=2,column=0)

btn8=Button(f3,padx=16,pady=16,bd=4,font=('ariel', 20 ,'bold'),text="8",bg="powder blue")
btn8.grid(row=2,column=1)

btn9=Button(f3,padx=16,pady=16,bd=4,font=('ariel', 20 ,'bold'),text="9",bg="powder blue")
btn9.grid(row=2,column=2)

Add=Button(f3,padx=16,pady=16,bd=4,font=('ariel', 20 ,'bold'),text="+",bg="powder blue")
Add.grid(row=2,column=3)

Sub=Button(f3,padx=16,pady=16,bd=4,font=('ariel', 20 ,'bold'),text="-",bg="powder blue")
Sub.grid(row=3,column=3)

multiply=Button(f3,padx=16,pady=16,bd=4,font=('ariel', 20 ,'bold'),text="*",bg="powder blue")
multiply.grid(row=4,column=3)

btnclear=Button(f3,padx=16,pady=16,bd=4,font=('ariel', 20 ,'bold'),text="c",bg="powder blue")
btnclear.grid(row=5,column=1)

Decimal=Button(f3,padx=16,pady=16,bd=4, font=('ariel', 20 ,'bold'),text=".",bg="powder blue")
Decimal.grid(row=5,column=2)

Division=Button(f3,padx=16,pady=16,bd=4,font=('ariel', 20 ,'bold'),text="/",bg="powder blue")
Division.grid(row=5,column=3)

btnequal=Button(f3,padx=16,pady=16,bd=4,width = 16,font=('ariel', 20 ,'bold'),text="=",bg="powder blue")
btnequal.grid(columnspan=4)

status = Label(f3,font=('aria', 15, 'bold'),width = 16, text="-By Samyak Jain",bd=2)
status.grid(row=7,columnspan=3)



lblorder=Label(f2,text="Order No.",font='ariel 15 bold',bd=10)
lblorder.grid(row=0,column=0)
txtorder=Entry(f2,font='Helvetica 13 bold',bd=6)
txtorder.grid(row=0,column=1)

lblfries=Label(f2,text="Fries Meal.",font='ariel 15 bold',bd=10)
lblfries.grid(row=1,column=0)
txtfries=Entry(f2,font='Helvetica 13 bold',bd=6)
txtfries.grid(row=1,column=1)

lblMeal=Label(f2,text="Lunch Meal",font='ariel 15 bold',bd=10)
lblMeal.grid(row=2,column=0)
txtMeal=Entry(f2,font='Helvetica 13 bold',bd=6)
txtMeal.grid(row=2,column=1)

lblBurger=Label(f2,text="Burger",font='ariel 15 bold',bd=10)
lblBurger.grid(row=3,column=0)
txtBurger=Entry(f2,font='Helvetica 13 bold',bd=6)
txtBurger.grid(row=3,column=1)

lblPizza=Label(f2,text="Pizza",font='ariel 15 bold',bd=10)
lblPizza.grid(row=4,column=0)
txtPizza=Entry(f2,font='Helvetica 13 bold',bd=6)
txtPizza.grid(row=4,column=1)

lblcheese=Label(f2,text="Cheese Burger",font='ariel 15 bold',bd=10)
lblcheese.grid(row=5,column=0)
txtcheese=Entry(f2,font='Helvetica 13 bold',bd=6)
txtcheese.grid(row=5,column=1)

lblDrinks=Label(f2,text="Drinks",font='ariel 15 bold',bd=10)
lblDrinks.grid(row=0,column=2)
txtDrinks=Entry(f2,font='Helvetica 13 bold',bd=6)
txtDrinks.grid(row=0,column=3)

lblcost=Label(f2,text="Cost",font='ariel 15 bold',bd=10)
lblcost.grid(row=1,column=2)
txtcost=Entry(f2,font='Helvetica 13 bold',bd=6)
txtcost.grid(row=1,column=3)

lblservice=Label(f2,text="Service Charge",font='ariel 15 bold',bd=10)
lblservice.grid(row=2,column=2)
txtservice=Entry(f2,font='Helvetica 13 bold',bd=6)
txtservice.grid(row=2,column=3)

lblTax=Label(f2,text="Tax",font='ariel 15 bold',bd=10)
lblTax.grid(row=3,column=2)
txtTax=Entry(f2,font='Helvetica 13 bold',bd=6)
txtTax.grid(row=3,column=3)

lblSubTotal=Label(f2,text="Sub Total",font='ariel 15 bold',bd=10)
lblSubTotal.grid(row=4,column=2)
txtSubTotal=Entry(f2,font='Helvetica 13 bold',bd=6)
txtSubTotal.grid(row=4,column=3)

lblTotal=Label(f2,text="Total",font='ariel 15 bold',bd=10)
lblTotal.grid(row=5,column=2)
txtTotal=Entry(f2,font='Helvetica 13 bold',bd=6)
txtTotal.grid(row=5,column=3)

btnprice=Button(f2,text='Price',padx=16,pady=8,bd=10,width=10,font='Arial 16 bold')
btnprice.grid(row=7,column=0)

btntotal=Button(f2,text='Total',padx=16,pady=8,bd=10,width=10,font='Arial 16 bold')
btntotal.grid(row=7,column=1)

btnreset=Button(f2,text='Reset',padx=16,pady=8,bd=10,width=10,font='Arial 16 bold')
btnreset.grid(row=7,column=2)

btnexit=Button(f2,text='Exit',padx=16,pady=8,bd=10,width=10,font='Arial 16 bold',command=root.destroy)
btnexit.grid(row=7,column=3)








root.mainloop()
