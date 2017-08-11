from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as pt
import os


class wallet:

    #Show positive values
    def maxima(self):
        #Fetch movement details
        with open('std.txt','r') as p:
            points = p.readlines()
        p.close()

        #Debugging print(points)    
        #Filter
        filtered = []
        for item in points:
            filtered.append(float(item[:-1]))
            
        maxV = max(filtered)
        sumV = sum(filtered)
        lenV = len(filtered)
        minV = min(filtered)

        avg = sumV/lenV

        #Plot values bigger than the average        
        newList = []
        for item in filtered:
            if item > avg:
                newList.append(item)

        pt.plot(newList)
        pt.show()
   
    #Ripple movement of balance
    def analysisGraph(self):
        #Fetch movement details
        with open('std.txt','r') as p:
            points = p.readlines()
        p.close()

        #Debugging print(points)
        
        #Filter
        filtered = []
        for item in points:
            filtered.append(float(item[:-1]))

        #Debugging print(filtered)

        #General Movement Linear-Graph
        pt.plot(filtered)
        pt.show()


    ##  Check for files inside
    ##  Create if necessary
    def createLog(self):        
        #Create movement file
        if not os.path.exists('std.txt'):
            self.std = open('std.txt','w')     
        
        if not os.path.exists('log.txt') and not os.path.exists('account.txt'):
            self.log = open('log.txt','w')
            self.acount = open('account.txt','w')
            
            #Initialize sample balance
            init = 0.0
            with open('account.txt','w') as f:
                f.write(str(init))
            f.close()  

            with open('account.txt','r') as ac:
                item = ac.readlines()
            ac.close()

            #Return value to interface 
            amount = float(item[0])
            return amount
        else:

            #If balance exists, read file and
            #return corresponding value
            with open('account.txt','r') as ac:
                item = ac.readlines()
            ac.close()
            amount = float(item[0])
            return amount
            
           

    
    ##  Save balance to account.txt / Rewrite
    def saveBalance(self):
        with open('account.txt','w') as acc:
            acc.write(str(self.balance))
        acc.close()
        messagebox.showinfo("Balance Report","Balance saved successfully.")




    ##  Add amount to balance
    ##  One layer verification required
    def addAmount(self):
        amount = self.insAmount.get()
        if amount > 0 and isinstance(amount,float):
                confirm = messagebox.askyesno('Balance Update','Are you sure that you want to update your balance?')
                if confirm == True:
                    self.balance += amount
                    messagebox.showinfo('Balance Update','An amount of '+str(amount)+' has been added\nto your balance.')
                    self.balance = round(self.balance,2)

                    #Write to movement file
                    with open('std.txt','a') as std:
                        std.write(str(self.balance)+'\n')
                    std.close()
                    
                    if self.balance > 0:
                        self.labelBalV = Label(self.window, text='$\t'+str(self.balance),fg='green').grid(row=1,column=2)
                    else:
                        self.labelBalV = Label(self.window, text='$\t'+str(self.balance),fg='red').grid(row=1,column=2)
                        
                    self.insAmount.set(float(0))
                else:
                    messagebox.showinfo('Balance Update','Action Cancelled.')
                    self.insAmount.set(float(0))
        else:
            messagebox.showinfo('Balance Update','Invalid amount. Try again.')
            self.insAmount.set(float(0))



    ##  Remove amount from balance
    ##  One layer verification required   
    def removeAmount(self):
        amount = self.remAmount.get()
        if amount > 0 and isinstance(amount,float):
                confirm = messagebox.askyesno('Balance Update','Are you sure that you want to update your balance?')
                if confirm == True:
                    self.balance -= amount
                    messagebox.showinfo('Balance Update','An amount of '+str(amount)+' has been removed from your balance.')
                    self.balance = round(self.balance,2)
                    
                    #Write to movement file
                    with open('std.txt','a') as std:
                        std.write(str(self.balance)+'\n')
                    std.close()
                    
                    if self.balance > 0:
                        self.labelBalV = Label(self.window, text='$\t'+str(self.balance),fg='green').grid(row=1,column=2)
                    else:
                        self.labelBalV = Label(self.window, text='$\t'+str(self.balance),fg='red').grid(row=1,column=2)
                        
                    self.remAmount.set(float(0))
                else:
                    messagebox.showinfo('Balance Update','Action Cancelled.')
                    self.remAmount.set(float(0))
        else:
            messagebox.showinfo('Balance Update','Invalid amount. Try again.')
            self.remAmount.set(float(0))
   


    ##  Records Keeper
    def insertEvent(self):
        name = self.eventName.get()
        if ((name != '' or name != ' ') and len(name) > 5):
            self.listBox.insert(END, str(name))
            with open('log.txt','a') as file:
                file.write(str(name)+'\n')
                file.close()
            self.eventName.set('')
        else:
            messagebox.showinfo('PyWallet Event','Try again')




    ##  Login &
    ##  Validation
    def login(self): 
        #Password Label and Entry
        self.app = Tk()
        self.password = StringVar()
        self.labelPass = Label(self.app, text='Enter Pin').grid(row=1,column=1)
        self.entryPass = Entry(self.app, textvariable=self.password, show='*').grid(row=2,column=1)
        self.validate = Button(self.app, text='Validate Action',command=self.validateLogin, width='18').grid(row=2,column=2)
        self.serialLabel = Label(self.app, text='Insert the licenced serial pin\nthat you\'ve received upon purchase.').grid(row=3,column=1)
        
        #Other Login Info
        self.app.title('PyWallet v1.9.5 - Login')
        self.app.resizable(0,0)
        self.app.mainloop()


    def validateLogin(self):
        password = self.password.get()  
        if password == "95":
            messagebox.showinfo('PyWallet v1.9.5','Environment Loaded Successfully')
            self.interface()
        else:
            messagebox.showinfo('PyWallet v1.9.5','Serial Key doesn\'t a match. Try again.')


    def __init__(self):
        self.login()

        
    def interface(self):        
        #Main App
        self.balance = self.createLog() 
        
        #Destroy Login
        self.app.destroy()


        self.window = Tk()
        
        #Entry Variables 
        self.insAmount = DoubleVar()
        self.remAmount = DoubleVar()

        
        #Adding Amount
        self.labelBal = Label(self.window, text='Current Balance').grid(row=1, column=1)

        #If balance is negative use red color
        #If balance is positive use green color
        if self.balance > 0:
            self.labelBalV = Label(self.window, text='$\t'+str(self.balance),fg='green').grid(row=1,column=2)
        else:
            self.labelBalV = Label(self.window, text='$\t'+str(self.balance),fg='red').grid(row=1,column=2)
            
        self.saveBalance = Button(self.window, text='Save Balance',command=self.saveBalance,width='15').grid(row=1,column=3)
        
        self.labelAdd = Label(self.window, text='Insert to balance').grid(row=2,column=1)
        self.labelRem = Label(self.window, text='Remove from balance').grid(row=3,column=1)

        #Entries
        self.insAm = Entry(self.window, textvariable=self.insAmount).grid(row=2,column=2)
        self.remAm = Entry(self.window, textvariable=self.remAmount).grid(row=3,column=2)

        #Buttons
        self.ins = Button(self.window, text='Add Ammount',command=self.addAmount,width='15').grid(row=2,column=3)
        self.rem = Button(self.window, text='Remove Amount',command=self.removeAmount,width='15').grid(row=3,column=3)

        #Schedule
        self.listBox = Listbox(self.window)
        self.listBox.grid(row=4,column=1)
        self.listBoxLabel = Label(self.window,text='Recorded actions for wallet.\nRecords help you '+\
                                  'manage the use of\nyour badget, providing cost analysis\nand efficiency ripples.')
        self.listBoxLabel.grid(row=4,column=2)

            
        #Events's Log
        self.eventName = StringVar()
        self.eventEntry = Entry(self.window, textvariable=self.eventName).grid(row=5,column=1)
        self.eventButton = Button(self.window, text='Add New Event Log',command=self.insertEvent,width='15').grid(row=5,column=2)


        #Graph movement of balance
        #Ripples Movement
        self.graph = Button(self.window, text='Ripple-M-Graph',command=self.analysisGraph,width='15').grid(row=5,column=3)
        #Above Average Graph
        self.avgGraph = Button(self.window, text='AA-Graph',command=self.maxima,width='15').grid(row=6,column=3)

        #Populate listBox using logs
        with open('log.txt','r') as file:
            status = file.readlines()
            for item in status:
                self.listBox.insert(END,str(item))

        self.window.title('PyWallet v1.9.5 - Dashboard')
        self.window.resizable(0,0)
        self.window.mainloop()
        
obj = wallet()

