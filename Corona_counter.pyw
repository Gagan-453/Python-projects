from tkinter import *
from tkinter import messagebox
from covid import *
from time import *

root = Tk()
root.title('Covid Cases')


f = Frame(root, width=700, height=600, bg='yellow')
f.propagate(0)
f.pack()

by = Label(f, text='By Gagan Adithya', bg='yellow', fg='purple', font=('Helvetica', 12, 'italic'))
by.place(x=10, y=560)

tw = Text(f, width=20, height=10, bg='light yellow', wrap=WORD, font=("Times new roman", 10))
tw.place(x=50, y=300)
tw.insert(END, "COVID-19 is a disease caused by a new strain of coronavirus. 'CO' stands for corona, 'VI' for virus, and 'D' for disease. Formerly, this disease was referred to as '2019 novel coronavirus' or '2019-nCoV.")
tw.tag_add('Covid_19', 1.0, 1.8)
tw.config(state=DISABLED)
tw.tag_config('Covid_19', background='gold', foreground='dark blue', font=('Lucida Console', 11, 'bold'))

e = Entry(f, width=15, bg='light green', fg='dark blue', font=('Arial', 20, 'bold'))
e.place(x=240, y=200)

country = Label(f, text='Country name here: ', width=16, bg='yellow', fg='brown', font=('Helvetica', 12, 'italic'))
country.place(x=87, y=203) 

head = Label(f, text='WORLD\'S  COVID', width=30, bg='yellow', fg='dark red', font=('Helvetica', 20, 'bold underline'))
head.pack()

show = Label(f, text='Enter country name and click on Continue\n to get country\'s covid cases', width=40, bg='magenta',  font=('Arial', 13, 'bold'))
show.place(x=120, y=120)

stay_home = Label(f, text='🔒STAY HOME  STAY SAFE🔒', width=25, bg='#E3BE0B', fg='#0E3565', font=('Britannic Bold', 13, 'bold'))
stay_home.place(x=440, y=340)


def display():
    try:
        info = e.get()
        covid = Covid()
        cases = covid.get_status_by_country_name(info)
        active = cases['active']
        confirmed = cases['confirmed']
        deaths = cases['deaths']
        recovered = cases['recovered']
        updated = cases['last_update']
        updated = str(updated).rstrip('0') + '.0'
        t = localtime(float(updated))
        time = '%d : %d : %d' %(t.tm_hour, t.tm_min, t.tm_sec)
        time_updated = Label(f, text='Last updated: '+str(time), width=25, bg='yellow', font=('Calibri', 10, 'italic'))
        time_updated.place(x=500, y=570)
        
        cn = Label(f, text='Covid in '+info, width=20, bg='yellow', fg='#0B800E', font=('Algerian', 15, 'underline'))
        cn.place(x=290, y=420)
        
        lbl = Label(f, text='Confirmed cases: ' + str(confirmed), width=25, bg='blue', font=('Brookman old style', 15, 'bold italic'))
        lbl.place(x=250, y=450)
        
        lbl1 = Label(f, text='Active cases: ' + str(active), width=25, bg='orange', font=('Brookman old style', 15, 'bold italic'))
        lbl1.place(x=250, y=480)
        
        lbl2 = Label(f, text='Recovered cases: ' + str(recovered), width=25, bg='green', font=('Brookman old style', 15, 'bold italic'))
        lbl2.place(x=250, y=510)
        
        lbl3 = Label(f, text='Total deaths: ' + str(deaths), width=25, bg='red', font=('Brookman old style', 15, 'bold italic'))
        lbl3.place(x=250, y=540)
        
    except ValueError:
        messagebox.showinfo('Sorry!', "Country not found. . .")
        
        
b = Button(f, text='CONTINUE', bg='red', width=10, height=2, fg='black', font=('Arial', 10, 'bold'), command=display)
b.place(x=320, y=240)

root.mainloop()