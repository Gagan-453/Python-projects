from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class height_counter:
    def __init__(self, root):
        self.height = root.winfo_screenheight()
        self.width = root.winfo_screenwidth()
        self.f = Frame(root, height=self.height, width=self.width, bg='light green')
        self.f.propagate(0)
        self.f.pack()
        
        self.lbl = Label(self.f, text='HEIGHT 🚶 PREDICTER', width=20, bg='light green', fg='#D51232', font=('Arial', 25, 'bold underline'))
        self.lbl.pack()
        
        self.e1 = Entry(self.f, width=20, bg='white', fg='dark green',  font=('Helvetica', 15, 'bold'))
        self.e1.place(x=300, y=200)
        
        self.e2 = Entry(self.f, width=20, bg='white', fg='red',  font=('Helvetica', 15, 'bold'))
        self.e2.place(x=300, y=300)
        
        self.b1 = Button(self.f, text='Calculate', width=15, height=2, bg='pink', fg='blue', font=('Arial', 10, 'bold'), command=self.calculate)
        self.b1.place(x=350, y=550)
        
        self.lbl1 = Label(self.f, text='Your name here: ', bg='light green', fg='#343C91', font=('Brookman old style', 15, 'italic'))
        self.lbl1.place(x=100, y=200)
        
        self.lbl2 = Label(self.f, text='Your current height(in cm): ', bg='light green', fg='#343C91', font=('Brookman old style', 15, 'italic'))
        self.lbl2.place(x=50, y=300)
        
        self.lbl3 = Label(self.f, text='Your current age: ', bg='light green', fg='#343C91', font=('Brookman old style', 15, 'italic'))
        self.lbl3.place(x=100, y=400)
        
        self.lbl4 = Label(self.f, text='Gender: ', bg='light green', fg='#343C91', font=('Brookman old style', 15, 'italic'))
        self.lbl4.place(x=130, y=480)
        
        self.n = IntVar()
        self.cb = ttk.Combobox(root, width=30, textvariable=self.n, font=('Arial', 10, 'bold'))
        self.cb.place(x=300, y=400)
        self.cb['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18)
        
        self.n1 = StringVar()
        self.cb1 = ttk.Combobox(root, width=30, textvariable=self.n1, font=('Arial', 10, 'bold'))
        self.cb1.place(x=300, y=480)
        self.cb1['values'] = ('Male', 'Female')
        
        self.lbl5 = Label(self.f, text='Made by Gagan Adithya', bg='light green', fg='#591361', font=('Calibri', 13, 'italic'))
        self.lbl5.place(x=720, y=650)
        
        self.help = Button(self.f, text='❓ HELP', bg='#F08EB7', fg='#102B07', width=10, height=2, font=('Arial', 10, 'bold'), command=self.help)
        self.help.place(x=0, y=0)
        
    def help(self):
        self.cb.destroy()
        self.cb1.destroy()
        self.hf = Frame(self.f, height=700, width=self.width, bg='light yellow')
        self.hf.propagate(0)
        self.hf.pack(side=TOP)
        
        self.back = Button(self.hf, text='Back', bg='#E4F20F', fg='dark green', width=15, font=('Arial', 15, 'bold'), command=self.back_to_home)
        self.back.pack()
        
        self.text = "This is made to check the total height of a person.Total height means the height of the person at 18 years(almost maximum age in which person's height stops growing).. This is made by Gagan Adithya by reference of a science class called chapter 'Adolescence' where sir was teaching about \t\t\tage and growth percentage."
        
        self.info = Message(self.hf, text=self.text, width=700, bg='light yellow', fg='#119C14', font=('Arial', 15, 'bold'))
        self.info.place(x=120, y=200)
        
        self.note = Label(self.hf, text='NOTE that this shows only approximate height, no one can predict exact height!!', bg='light yellow', fg='#0D4F26', font=('Arial', 15, 'bold'))
        self.note.place(x=100, y=530)
        
    def back_to_home(self):
        self.hf.destroy()
        self.n = IntVar()
        self.cb = ttk.Combobox(root, width=30, textvariable=self.n, font=('Arial', 10, 'bold'))
        self.cb.place(x=300, y=400)
        self.cb['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18)
        
        self.n1 = StringVar()
        self.cb1 = ttk.Combobox(root, width=30, textvariable=self.n1, font=('Arial', 10, 'bold'))
        self.cb1.place(x=300, y=480)
        self.cb1['values'] = ('Male', 'Female')
        
    def calculate(self):
        self.show = Frame(self.f, width=400, height=200, bg='#F9CE11')
        self.show.propagate(0)
        self.show.place(x=600, y=200)
        
        self.sci = Label(self.show, text='(According to Science)', width=20, bg='#F9CE11', fg='black')
        self.sci.pack(side=BOTTOM)
        
        self.name = self.e1.get()
        try:
            self.height=float(self.e2.get())
        except Exception:
            self.show.destroy()
            messagebox.showinfo("ERROR", "Invalid height")
        self.age = self.n.get()
        self.gender = self.n1.get()
        
        self.lst = ['Male', 'Female']
        
        self.age_height_boys = {8 : 72, 9 : 75, 10 : 78, 11 : 81, 12 : 84, 13 : 88, 14 : 92, 15 : 95, 16 : 98, 17 : 99, 18 : 100}
        self.age_height_girls = {8 : 77, 9 : 81, 10 : 84, 11 : 88, 12 : 91, 13 : 95, 14 : 98, 15 : 99, 16 : 99.5, 17 : 100, 18 : 100}
        
        
        if self.name == '':
            self.show.destroy()
            messagebox.showinfo("Empty!", "Name cannot be empty!")
            
        if (self.age<8 or self.age>18):
            self.show.destroy()
            messagebox.showinfo("Wrong", "Invalid age")
            
        if (self.gender not in self.lst):
            self.show.destroy()
            messagebox.showinfo("ERROR", "Invalid Gender!")
            
        else:
            self.name_show = Label(self.show, text=self.name+"'s total predicted height", bg='#F9CE11', fg='#37812F', font=('Arial', 15, 'bold underline'))
            self.name_show.pack()
            self.approx = Label(self.show, text='(Approx)',bg='#F9CE11', fg='#37812F', font=('Arial', 15, 'bold'))
            self.approx.pack()
            
            if self.gender == 'Male':
                self.val = self.age_height_boys[self.age]
                self.th = self.height/self.val*100
                self.predict = Label(self.show, text=('Total predicted height = %.2f cm' %self.th), bg='#DEF70D', fg='#256873', width=35, font=('Berlin Sans FB Demi', 15))
                self.predict.pack(pady=10)
                
                self.he = (self.th*0.0328084)
                self.feet = Label(self.show, text=('Height in feet = %.1f' %self.he), bg='#DEF70D', fg='#256873', width=35, font=('Berlin Sans FB Demi', 15))
                self.feet.pack(pady=10)
            
            if self.gender == 'Female':
                self.val = self.age_height_girls[self.age]
                self.th = self.height/self.val*100
                self.predict = Label(self.show, text=('Total predicted height = %.2f cm' %self.th), bg='#DEF70D', fg='#256873', width=35, font=('Berlin Sans FB Demi', 15))
                self.predict.pack(pady=10)
                
                self.he = (self.th*0.0328084)
                self.feet = Label(self.show, text=('Height in feet = %.1f' %self.he), bg='#DEF70D', fg='#256873', width=35, font=('Berlin Sans FB Demi', 15))
                self.feet.pack(pady=10)
                
root = Tk()
root.title("Your Height")
h = height_counter(root)
root.mainloop()