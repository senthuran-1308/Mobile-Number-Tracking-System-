from tkinter import *
from tkinter import messagebox
import phonenumbers
from phonenumbers import carrier,geocoder,timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz
from PIL import Image,ImageTk


sweety=Tk()
sweety.title("MOBILE TRACKING")
sweety.geometry("600x750")
sweety.resizable(False,False)
sweety.configure(bg='black')
##icon image
icon = PhotoImage(file="icon.png")
sweety.iconphoto(False,icon)




def finder():
    if len(entry.get())==10:
        messagebox.showwarning("Not Valid!","Enter The Number With Country Code")
        print("Not Valid!","Enter The Number With Country Code")
    elif entry.get()=="":
        messagebox.showwarning("Required","Enter The Number")
        print("Required","Enter The Number")
    else:
        ent_numb=entry.get()
        print(ent_numb)



        
    num=phonenumbers.parse(ent_numb)

    locate=geocoder.description_for_number(num, 'en')
    country.config(text=locate)


    operator=carrier.name_for_number(num, 'en')
    sim.configure(text=operator)


    time=timezone.time_zones_for_number(num)
    zone.configure(text=time)


    geolocator=Nominatim(user_agent='geoapiExercises')
    location= geolocator.geocode(locate)


    lng=location.longitude
    lat=location.latitude
    longitude.config(text=lng)
    latitude.config(text=lat)


    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)


    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M:%p")
    clock.config(text=current_time)
    


    
##logo image
bgimg=ImageTk.PhotoImage(file="logo image.png")
bgp=Label(sweety,bg='black',image=bgimg)
bgp.place(relx=0.65,rely=0.08)

cimg=ImageTk.PhotoImage(file='search png.png')
cgp=Label(sweety,bg='black',image=cimg)
cgp.place(relx=0.2,rely=0.3)


##heading
head1=Label(sweety,text='MOBILE NUMBER',bg="black",fg='white',font=('arial',20,'bold'))
head1.place(relx=0.15,rely=0.1)

head2=Label(sweety,text='TRACKING SYSTEM',bg="black",fg='white',font=('arial',20,'bold'))
head2.place(relx=0.15,rely=0.17)

##button box
##box=ImageTk.PhotoImage(file='button png.png')
##Label(sweety,bg='black',image=box).place(relx=0.4,rely=0.6)


##entry

entry=StringVar()
ent=Entry(sweety,textvariable=entry,width=19,justify='center',bd=0,font=('arial',18))
ent.place(relx=0.257,rely=0.35)

##search buttton


but=Button(sweety,text='search',width=15,relief='solid',activebackground='green',activeforeground='white',bg='green',fg='white',bd=0,command=finder,font=('arial',20,'bold'))
but.place(relx=0.261,rely=0.44)

frame=Frame(sweety,width=600,height=400,bg='light cyan')
frame.place(relx=0.0,rely=0.53)


##label info

country=Label(frame,text='Country',bg='light cyan',fg='black',font=('arial',15,'bold'))
country.place(relx=0.15,rely=0.1)

sim=Label(frame,text='SIM',bg='light cyan',fg='black',font=('arial',15,'bold'))
sim.place(relx=0.15,rely=0.28)

zone=Label(frame,text='TimeZone',bg='light cyan',fg='black',font=('arial',15,'bold'))
zone.place(relx=0.63,rely=0.1)

clock=Label(frame,text='PhoneTime',bg='light cyan',fg='black',font=('arial',15,'bold'))
clock.place(relx=0.63,rely=0.28)

longitude=Label(frame,text='Longitude',bg='light cyan',fg='black',font=('arial',15,'bold'))
longitude.place(relx=0.15,rely=0.43)

latitude=Label(frame,text='Latitude',bg='light cyan',fg='black',font=('arial',15,'bold'))
latitude.place(relx=0.63,rely=0.43)


Button(frame,text='EXIT',bg='light cyan',fg='blue2',font=('arial',15,'bold'),activebackground='light cyan',
       bd=0,command= sweety.destroy,activeforeground='blue2').place(relx=0.45,rely=0.67)

sweety.mainloop()



