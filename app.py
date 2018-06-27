from tkinter import *
import time

root =Tk()
root.geometry('1500x800')
root.title("Restaurant Management System")
text=StringVar()
s=""
def btnclick(n):
    global s
    s= s + str(n)
    text.set(s)


def clear():
    global s
    s = ""
    text.set("")

def equals():
    global s
    sumup = str(eval(s))
    text.set(sumup)
    s = ""


def reset():
    txtorder.delete(0,END)
    txtfries.delete(0,END)
    txtBurger.delete(0,END)
    txtTotal.delete(0,END)
    txtcheese.delete(0,END)
    txtcost.delete(0,END)
    txtDrinks.delete(0,END)
    txtMeal.delete(0,END)
    txtPizza.delete(0,END)
    txtservice.delete(0,END)
    txtSubTotal.delete(0,END)
    txtTax.delete(0,END)


def price():
    roo = Tk()
    roo.geometry("600x220")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="                                   ", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fries Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Lunch Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="40", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cheese Burger", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)

def total():
    if len(txtfries.get())==0:
        txtfries.insert(0,0)
    if len(txtMeal.get())==0:
        txtMeal.insert(0,0)
    if len(txtBurger.get())==0:
        txtBurger.insert(0,0)
    if len(txtPizza.get())==0:
        txtPizza.insert(0,0)
    if len(txtcheese.get())==0:
        txtcheese.insert(0,0)
    if len(txtDrinks.get())==0:
        txtDrinks.insert(0,0)


    fries = float(txtfries.get())
    meal= float(txtMeal.get())
    burger = float(txtBurger.get())
    Pizza= float(txtPizza.get())
    cheese= float(txtcheese.get())
    Drinks= float(txtDrinks.get())

    friestotal=fries*25
    mealtotal=meal*40
    burgertotal=burger*35
    Pizzatotal=Pizza*50
    cheesetotal=cheese*50
    Drinkstotal=Drinks*50

    costofmeal = "Rs.", str('%.2f' %(friestotal + mealtotal + burgertotal + Pizzatotal + cheesetotal + Drinkstotal))
    PayTax = ((friestotal + mealtotal + burgertotal + Pizzatotal + cheesetotal + Drinkstotal) * 0.33)
    Totalcost = (friestotal + mealtotal + burgertotal + Pizzatotal + cheesetotal + Drinkstotal)
    Ser_Charge = ((friestotal + mealtotal + burgertotal + Pizzatotal + cheesetotal + Drinkstotal) / 99)
    Service = "Rs.", str('%.2f' %Ser_Charge)
    OverAllCost = "Rs.", str('%.2f' %(PayTax + Totalcost + Ser_Charge))
    Total=(PayTax + Totalcost + Ser_Charge)
    PaidTax = "Rs.", str('%.2f' % PayTax)
    Total=round(Total)

    txtTax.insert(0,PaidTax)
    txtSubTotal.insert(0,OverAllCost)
    txtTotal.insert(0,Total)
    txtservice.insert(0,Service)
    txtcost.insert(0,costofmeal)


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
#-----------------------------------CALCULATOR---------------------------------------------------------------
txtE=Entry(f3,font='Arial 20 bold',bg='white',textvariable=text, bd=5 ,justify='right')
txtE.grid(columnspan=4)

btn1=Button(f3,padx=16,pady=16,bd=4,font=('ariel', 20 ,'bold'),text="1",bg="powder blue",command=lambda:btnclick(1))
btn1.grid(row=4,column=0)

btn2=Button(f3,padx=16,pady=16,bd=4,font=('ariel', 20 ,'bold'),text="2",bg="powder blue",command=lambda:btnclick(2))
btn2.grid(row=4,column=1)

btn3=Button(f3,padx=16,pady=16,bd=4,font=('ariel', 20 ,'bold'),text="3",bg="powder blue",command=lambda:btnclick(3))
btn3.grid(row=4,column=2)

btn4=Button(f3,padx=16,pady=16,bd=4,font=('ariel', 20 ,'bold'),text="4",bg="powder blue",command=lambda:btnclick(4))
btn4.grid(row=3,column=0)

btn5=Button(f3,padx=16,pady=16,bd=4,font=('ariel', 20 ,'bold'),text="5",bg="powder blue",command=lambda:btnclick(5))
btn5.grid(row=3,column=1)

btn6=Button(f3,padx=16,pady=16,bd=4,font=('ariel', 20 ,'bold'),text="6",bg="powder blue",command=lambda:btnclick(6))
btn6.grid(row=3,column=2)

btn7=Button(f3,padx=16,pady=16,bd=4,font=('ariel', 20 ,'bold'),text="7",bg="powder blue",command=lambda:btnclick(7))
btn7.grid(row=2,column=0)

btn8=Button(f3,padx=16,pady=16,bd=4,font=('ariel', 20 ,'bold'),text="8",bg="powder blue",command=lambda:btnclick(8))
btn8.grid(row=2,column=1)

btn9=Button(f3,padx=16,pady=16,bd=4,font=('ariel', 20 ,'bold'),text="9",bg="powder blue",command=lambda:btnclick(9))
btn9.grid(row=2,column=2)

btn0=Button(f3,padx=16,pady=16,bd=4,font=('ariel', 20 ,'bold'),text="0",bg="powder blue",command=lambda:btnclick(0))
btn0.grid(row=5,column=0)

Add=Button(f3,padx=16,pady=16,bd=4,font=('ariel', 20 ,'bold'),text="+",bg="powder blue",command=lambda:btnclick('+'))
Add.grid(row=2,column=3)

Sub=Button(f3,padx=16,pady=16,bd=4,font=('ariel', 20 ,'bold'),text="-",bg="powder blue",command=lambda:btnclick('-'))
Sub.grid(row=3,column=3)

multiply=Button(f3,padx=16,pady=16,bd=4,font=('ariel', 20 ,'bold'),text="*",bg="powder blue",command=lambda:btnclick('*'))
multiply.grid(row=4,column=3)

btnclear=Button(f3,padx=16,pady=16,bd=4,font=('ariel', 20 ,'bold'),text="c",bg="powder blue",command=lambda:clear())
btnclear.grid(row=5,column=1)

Decimal=Button(f3,padx=16,pady=16,bd=4, font=('ariel', 20 ,'bold'),text=".",bg="powder blue",command=lambda:btnclick('.'))
Decimal.grid(row=5,column=2)

Division=Button(f3,padx=16,pady=16,bd=4,font=('ariel', 20 ,'bold'),text="/",bg="powder blue",command=lambda:btnclick('/'))
Division.grid(row=5,column=3)

btnequal=Button(f3,padx=16,pady=16,bd=4,width = 16,font=('ariel', 20 ,'bold'),text="=",bg="powder blue",command=lambda:equals())
btnequal.grid(columnspan=4)

status = Label(f3,font=('aria', 15, 'bold'),width = 16, text="-By Samyak Jain",bd=2)
status.grid(row=7,columnspan=3)
#-------------------------------------------------------------------------------------------------------------------------


lblorder=Label(f2,text="Order No.",font='ariel 15 bold',bd=10)
lblorder.grid(row=0,column=0)
txtorder=Entry(f2,font='Helvetica 13 bold',bd=6,justify='right')
txtorder.grid(row=0,column=1)

lblfries=Label(f2,text="Fries Meal.",font='ariel 15 bold',bd=10)
lblfries.grid(row=1,column=0)
txtfries=Entry(f2,font='Helvetica 13 bold',bd=6,justify='right')
txtfries.grid(row=1,column=1)

lblMeal=Label(f2,text="Lunch Meal",font='ariel 15 bold',bd=10)
lblMeal.grid(row=2,column=0)
txtMeal=Entry(f2,font='Helvetica 13 bold',bd=6,justify='right')
txtMeal.grid(row=2,column=1)

lblBurger=Label(f2,text="Burger",font='ariel 15 bold',bd=10)
lblBurger.grid(row=3,column=0)
txtBurger=Entry(f2,font='Helvetica 13 bold',bd=6,justify='right')
txtBurger.grid(row=3,column=1)

lblPizza=Label(f2,text="Pizza",font='ariel 15 bold',bd=10)
lblPizza.grid(row=4,column=0)
txtPizza=Entry(f2,font='Helvetica 13 bold',bd=6,justify='right')
txtPizza.grid(row=4,column=1)

lblcheese=Label(f2,text="Cheese Burger",font='ariel 15 bold',bd=10)
lblcheese.grid(row=5,column=0)
txtcheese=Entry(f2,font='Helvetica 13 bold',bd=6,justify='right')
txtcheese.grid(row=5,column=1)

lblDrinks=Label(f2,text="Drinks",font='ariel 15 bold',bd=10)
lblDrinks.grid(row=0,column=2)
txtDrinks=Entry(f2,font='Helvetica 13 bold',bd=6,justify='right')
txtDrinks.grid(row=0,column=3)

lblcost=Label(f2,text="Cost",font='ariel 15 bold',bd=10)
lblcost.grid(row=1,column=2)
txtcost=Entry(f2,font='Helvetica 13 bold',bd=6,justify='right')
txtcost.grid(row=1,column=3)

lblservice=Label(f2,text="Service Charge",font='ariel 15 bold',bd=10)
lblservice.grid(row=2,column=2)
txtservice=Entry(f2,font='Helvetica 13 bold',bd=6,justify='right')
txtservice.grid(row=2,column=3)

lblTax=Label(f2,text="Tax",font='ariel 15 bold',bd=10)
lblTax.grid(row=3,column=2)
txtTax=Entry(f2,font='Helvetica 13 bold',bd=6,justify='right')
txtTax.grid(row=3,column=3)

lblSubTotal=Label(f2,text="Sub Total",font='ariel 15 bold',bd=10)
lblSubTotal.grid(row=4,column=2)
txtSubTotal=Entry(f2,font='Helvetica 13 bold',bd=6,justify='right')
txtSubTotal.grid(row=4,column=3)

lblTotal=Label(f2,text="Total",font='ariel 15 bold',bd=10)
lblTotal.grid(row=5,column=2)
txtTotal=Entry(f2,font='Helvetica 13 bold',bd=6,justify='right')
txtTotal.grid(row=5,column=3)

btnprice=Button(f2,text='Price',padx=16,pady=8,bd=10,width=10,font='Arial 16 bold',command=lambda:price())
btnprice.grid(row=7,column=0)

btntotal=Button(f2,text='Total',padx=16,pady=8,bd=10,width=10,font='Arial 16 bold',command=lambda:total())
btntotal.grid(row=7,column=1)

btnreset=Button(f2,text='Reset',padx=16,pady=8,bd=10,width=10,font='Arial 16 bold',command=lambda:reset())
btnreset.grid(row=7,column=2)

btnexit=Button(f2,text='Exit',padx=16,pady=8,bd=10,width=10,font='Arial 16 bold',command=root.destroy)
btnexit.grid(row=7,column=3)

root.mainloop()
