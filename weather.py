import requests,math
from tkinter import *
from tkinter import ttk

re=""

def findWeath(): 
    city=e1.get()
    if city=="":
        return
    
    res.insert(0,"Loading..")
    
    try :
        p  = requests.get(f"https://api.openweathermap.org/geo/1.0/direct?q={city}&appid=cf65d0c5f5cfffb9e7c92e59ec5e2e80")
        if not p:
            raise Exception("Invalid Input")
        j = p.json()[0]
        print(j)
        print(j['lat'], j['lon'])
        lat=j['lat']
        lon=j['lon']
        url = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=cf65d0c5f5cfffb9e7c92e59ec5e2e80").json()
        if not url:
            raise Exception("Invalid Input")
        print(url)
        temp = math.ceil(url['main']['temp']-273)
        weath= url['weather'][0]['main']
        print(f"{weath} {temp}")
        re=f"{weath} {temp} ' C"
        res.delete(0,END)
        res.insert(0,re)
        ct.delete(0,END)
        ct.insert(0,f"{j['state']}, {j['country']}")
    except:
        print("Invalid")
        re="Invalid"
        res.delete(0,END)
        res.insert(0,re)
        ct.delete(0,END)
        ct.insert(0,re)

#print(findWeath("kolkata"))

root=Tk()
root.title("Weather")
root.minsize(250,150)
root.resizable(1,1)
frm=ttk.Frame(root,padding=10)
frm.grid()

l1=Label(frm,text="Weather",font=("Arial",25))
l1.grid(row=0,column=0,columnspan=3)

l2=Label(frm,text="Enter the Place ",font=("Arial",18))
l2.grid(row=1,column=0)

ttk.Label(frm,text="Temperature: ",padding=10,font=("Arial",18)).grid(row=3,column=0)

res=Entry(frm,text="",font=("Arial",18))
res.grid(row=3,column=1)

ttk.Label(frm,text="Place: ",padding=10,font=("Arial",18)).grid(row=4,column=0)

ct=Entry(frm,text="",font=("Arial",18))
ct.grid(row=4,column=1)


e1_val=StringVar()
e1=Entry(frm,textvariable=e1_val,font=("Arial",18))
e1.grid(row=1,column=1)

b=Button(frm,text="Submit",font=("Arial",14),command=findWeath,)
b.grid(row=2,column=0,columnspan=3)




root.mainloop()
    

