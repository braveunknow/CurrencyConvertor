from tkinter import *                                                     
from tkinter import ttk
from PIL import Image,ImageTk
from datetime import date 
from tkinter import messagebox
from forex_python.converter import CurrencyRates,CurrencyCodes
import datetime
import requests                 #just for error
import forex_python             #just for error

c = CurrencyRates()
d = CurrencyCodes()


#functions of buttons
def convert () :
    
    #error handling
    
    if str(fc.get()) in countries :
        pass
            
        if str(tc.get()) in countries : 
            pass

        else :
            messagebox.showerror("ERROR!!! Invalid Currency", "Please Select A Valid Currency In Which The Ammount Needs To be Converted ")
    else :
        messagebox.showerror("ERROR!!! Invalid Currency", "Please Select A Valid Currency To Convert ")

  
    try :
        a=float(n1.get())
    except ValueError :
        messagebox.showerror("ERROR!!! Invalid Ammount", "Please Enter Ammount In Number")
        
    try :
        b=str(n3.get())
        y,m,l=map(int,b.split('-'))
        b=datetime.date(y,m,l)
    except :
        messagebox.showerror("ERROR!!! Invalid Date", "Please Enter The Date In  YYYY-MM-DD Format")

    try :
        cammount = c.convert(fc.get(),tc.get(),a,b)
    except forex_python.converter.RatesNotAvailableError :
        messagebox.showerror("ERROR!!! Rates Not Available", " Currency Rates Source Not Ready For The Enterd Currencies  On The Specific Date ")
    except requests.exceptions.ConnectionError :
        messagebox.showerror("ERROR!!! Unable to connect With API", "Turn On The Internet Connection ")

    # actual converstion and outupt 

    c2.configure(state=NORMAL)                  #enebling text
    text1.configure(state=NORMAL)               #enebling text
    
    c2.delete(0.1,'end')                        #clearing text
    text1.delete(0.1,'end')                     #clearing text

    a=float(n1.get())                           #input of ammount

    b=str(n3.get())                             #input of date
    y,m,l=map(int,b.split('-'))
    b=datetime.date(y,m,l)

    symbf = d.get_symbol(fc.get())              #symbol of fc
    symbt = d.get_symbol(tc.get())              #symbol of tc
    namef = d.get_currency_name(fc.get())       #name of fc
    namet = d.get_currency_name(tc.get())       #name of tc

    rate = c.get_rate(fc.get(),tc.get(),b)      #rate
    rate = round(rate,4)  
                             
    cammount = c.convert(fc.get(),tc.get(),a,b) #conversion
    cammount=round(cammount, 4)

    #displaying converted ammount
    g = str(cammount)+ "("+symbt+")"
    c2.insert(0.1,g)

    #displaying data in testbox 
    text1.insert("0.1", "On Date " + str(b) + " The Rate For Entered Currencies Is \n" + "1  "+ namef + " ("+ symbf + ")  " + "=  " + str(rate)+"  " + namet + " ("+symbt+")  " + "\n\n" + "Therefore According To The Rate :\n" + str(a) +"  " + namef + " (" + symbf + ")  " + "=  " + str(cammount) + "  "+ namet + " ("+symbt+")  " + "\n\n -x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-")
    dataw=open("data1",'a',encoding='utf-8')                #openingfile
    dataw.write("\n" + text1.get(0.1,'end') + "\n")         #closing file

    text1.configure(state=DISABLED)                         #disabling text
    c2.configure(state=DISABLED)                            #disabling text   

       
def clear() :
    c2.configure(state=NORMAL)
    text1.configure(state=NORMAL)
    fc.set("INR")
    tc.set("USD")
    c1.delete(0,'end')
    c2.delete(0.1,'end')
    text1.delete(0.1,'end')
    n3.set(date.today())
    text1.configure(state=DISABLED)
    c2.configure(state=DISABLED)

def swap() :
    f=fc.get()
    t=tc.get()
    fc.set(t)
    tc.set(f)

def history () :
    text1.configure(state=NORMAL)     
    if text1.get(0.1,'end') == "\n" :
        datar = open("data1",'r',encoding='utf-8')
        hist = datar.read()
        datar.close()
        text1.insert(0.1,hist)
        text1.configure(state=DISABLED)
    else :
         clear()


root = Tk()
root.title("BCOE PYTHON MINIPROJECT")   #changing title
root.iconbitmap(r"bcoeiconnnn.ico")     #changing icon
root.geometry("900x600")
root.maxsize(900,600)
root.minsize(900,600)
root.state("zoomed")   #to open window in maximized mode


# variables
n1=StringVar() 
n3=StringVar()
fc = StringVar()
tc = StringVar()
# default values
n3.set(date.today())
fc.set("USD")
tc.set("INR")


#images used
img=Image.open("bg1.png")
img=img.resize((300,500),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(img)
 
conv=Image.open("convert1.png")
conv=conv.resize((20,20),Image.ANTIALIAS)
im1=ImageTk.PhotoImage(conv)

res=Image.open("reset1.png")
res=res.resize((25,25),Image.ANTIALIAS)
im2=ImageTk.PhotoImage(res)

exi=Image.open("exit1.png")
exi=exi.resize((30,30),Image.ANTIALIAS)
im3=ImageTk.PhotoImage(exi)

swa=Image.open("swap1.png")
swa=swa.resize((28,28),Image.ANTIALIAS)
im4=ImageTk.PhotoImage(swa)

his=Image.open("history1.png")
his=his.resize((20,20),Image.ANTIALIAS)
im5=ImageTk.PhotoImage(his)


#lables 
bg1=Label(image=photo)
bg1.pack(side=LEFT)
l1=Label(root, text="Currency Converter", fg="navy", font="Arial 30 bold")
l1.place(x=280,y=8)
l2=Label(root, text="From Currency -->", fg="navy", font="Castellar 12 bold")
l2.place(x=340,y=90)
l3=Label(root, text="Enter Ammount :", fg="navy", font="Castellar 12 bold")
l3.place(x=340,y=130)
l4=Label(root, text="To Currency -->", fg="navy", font="Castellar 12 bold")
l4.place(x=340,y=210)
l5=Label(root, text="Date  [yyyy-mm-dd] : ",fg="navy", font="Castellar 12 bold",width=25, anchor="w")
l5.place(x=340,y=250)
l6=Label(root, text="Converted Ammount :", fg="navy", font="Castellar 12 bold")
l6.place(x=340,y=300)


#menu box lists
countries = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']

# menu box
fcountry = ttk.Combobox(root,height=6, width = 20, textvariable = fc, value=countries, state='normal', font=('verdana',11,'bold'))
fcountry.place(x=610,y=90)
tcountry = ttk.Combobox(root,height=6, width = 20, textvariable = tc, value=countries, state='normal', font=('verdana',11,'bold'))
tcountry.place(x=610,y=210)

# entrys
c1=Entry(root,textvariable = n1 , width=20,borderwidth=1,font=('verdana',11,'bold'))
c1.place(x=610,y=130)

c3=Entry(root,textvariable = n3 , width=20,borderwidth=1,font=('verdana',11,'bold'))
c3.place(x=610,y=250)


#text box
c2=Text(root, width=20, height=1,borderwidth=1,font=('verdana',11,'bold'),state=DISABLED)
c2.place(x=610,y=300)

text1 = Text(root,height=8,width=57,font=('verdana','10','bold'),state=DISABLED)
text1.place(x=340,y=410)

# Buttons showdata command removed
clearb = Button(root,image=im2,text=" Reset",compound=LEFT,font=('verdana','11','bold'),borderwidth=2,bg="white",fg="navy",relief="raised",bd=6,command=clear)
clearb.place(x=340,y=350,relheight=0.067,relwidth=0.1638)

convertb = Button(root,image=im1,text=" Convert",compound=LEFT,font=('verdana','11','bold'),borderwidth=2,bg="navy",fg="white",relief="raised",bd=6,command=convert)
convertb.place(x=523,y=350,relheight=0.067,relwidth=0.1638)

exitb = Button(root,image=im3,text=" Exit",compound=LEFT,font=('verdana','11','bold'),borderwidth=2,bg="red",fg="white",relief="raised",bd=6,command=root.destroy)
exitb.place(x=708,y=350,relheight=0.067,relwidth=0.1638)

swapb = Button(root,image=im4,font=('verdana','11','bold'),borderwidth=2,bg="white",fg="black",relief="raised",bd=6,command=swap)
swapb.place(x=705,y=160,relheight=0.067,relwidth=0.057)

histroyb= Button(root,image=im5,text=" History",compound=LEFT,font=('verdana','8','bold'),borderwidth=2,bg="white",fg="black",relief="raised",bd=6,command=history)
histroyb.place(x=730,y=550,relheight=0.06,relwidth=0.14)

root.mainloop()

