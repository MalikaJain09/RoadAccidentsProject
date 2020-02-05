from tkinter import *
from  File2 import *

class Gui:
    
    def DataFunction(self):
        window = Tk()
        window.config(background="light green")
        window.geometry("300x500")
        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()
        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()
        state = Label(window, text="Enter State:",bg="light green").pack()
        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()
        self.enterState = Entry(window)
        self.enterState.pack()
        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()
        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()

        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()
        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()

        btnPie = Button(window, text="Display Pie Chart", bg="black", fg="white", command=self.askYear).pack()

        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()
        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()
        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()

        btnGraph = Button(window, text="Display Graph", bg="black", fg="white", command=self.execute).pack()


        window.mainloop()
    def execute(self):
        y=self.enterState.get()
        print(y,type(y))
        aRef=Accidents()
        aRef.dataAccidents(y)

    def DataFunction2(self):
        window = Tk()
        window.config(background="light green")
        window.geometry("400x400")
        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()
        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()
        state1 = Label(window, text="Enter State1:", bg="light green").pack()
        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()
        self.enterState1 = Entry(window)
        self.enterState1.pack()
        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()
        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()
        state2 = Label(window, text="Enter State2:", bg="light green").pack()
        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()
        self.enterState2 = Entry(window)
        self.enterState2.pack()
        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()
        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()

        btnOneState = Button(window, text="Show", bg="black", fg="white", command=self.execute2, height=1,
                             width=7).pack()

        window.mainloop()

    def execute2(self):
        state1 = self.enterState1.get()
        state2 = self.enterState2.get()
        print("========================")

        aRef = Accidents()
        aRef.dataTwoAccidents(state1, state2)

    def execute3(self):
        state = self.enterState.get()
        year = int(self.enterYear.get())

        print(state, year)
        aRef = Accidents()
        aRef.Pie(state, year)
    def askYear(self):
        window = Tk()
        window.config(background="light green")
        window.geometry("300x300")
        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()
        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()
        year = Label(window, text="Enter Year:", bg="light green").pack()
        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()
        self.enterYear = Entry(window)
        self.enterYear.pack()
        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()
        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()

        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()
        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()

        btnShow = Button(window, text="Show", bg="black", fg="white", command=self.execute3, height=1,
                             width=7).pack()

    def askYear1(self):
        window = Tk()
        window.config(background="light green")
        window.geometry("300x300")
        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()
        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()
        year = Label(window, text="Enter Year:", bg="light green").pack()
        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()
        self.enterYear = Entry(window)
        self.enterYear.pack()
        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()
        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()

        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()
        labelEmpty = Label(window, text=" ", font=30, bg="light green").pack()

        btnShow = Button(window, text="Show", bg="black", fg="white", command=self.execute4, height=1,
                         width=7).pack()


    def execute4(self):
        y = int(self.enterYear.get())
        aRef = Accidents()
        aRef.YearWise(y)





    def MainWindow(self):
        window = Tk()
        window.title("Road Accidents")
        window.geometry("490x450")
        window.resizable(0, 0)

        back = Frame(master=window, bg='light green')
        back.grid(row=0, column=0, )
        back.pack_propagate(0)
        back.pack(fill=BOTH, expand=1)
        labelHeading=Label(back,text="Welcome",bg="light green",fg ="black",font=("Arial Bold",80)).grid(row=0,column=1)

        labelEmpty = Label(master=back, text=" ", font=30, bg="light green").grid(row=1, column=0)
        labelEmpty = Label(master=back, text=" ", font=30, bg="light green").grid(row=2, column=0)

        btnState=Button(back,text="View One State",bg="black",fg="white",command=self.DataFunction).grid(row=3,column=1)

        labelEmpty = Label(master=back, text=" ", font=30, bg="light green").grid(row=4, column=0)
        labelEmpty = Label(master=back, text=" ", font=30, bg="light green").grid(row=4, column=0)
        labelEmpty = Label(master=back, text=" ", font=30, bg="light green").grid(row=4, column=0)

        btnState1=Button(back,text="Compare two states",bg="black",fg="white",command=self.DataFunction2).grid(row=5,column=1)


        labelEmpty = Label(master=back, text=" ", font=30, bg="light green").grid(row=6, column=0)
        
        btnIndia=Button(back,text=" Overall year Wise Comparison",bg="black",fg="white",command=self.askYear1).grid(row=9,column=1)


        window.mainloop()

wRef=Gui()
wRef.MainWindow()