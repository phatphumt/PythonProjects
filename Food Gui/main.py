import tkinter as tk
import tkinter.font as tkFont
from tkinter import CENTER, messagebox
import datetime

menusName = {'001': 'Rib-eye Steak', '002': 'Ice-cream'}
menusPrice = {'001': '20', '002': '8'}


class App:
    def __init__(self, mainwin):
        self.totalPrice = 0
        self.showError = None
        self.menuNames = None
        self.menuPrices = None
        self.menu = None
        self.orders = ''
        self.config = None
        self.bills, self.addTimes = 0, 1
        mainwin.title("Food Billing")
        width = 600
        height = 500
        screenwidth = mainwin.winfo_screenwidth()
        screenheight = mainwin.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        mainwin.geometry(alignstr)
        mainwin.resizable(width=False, height=False)

        configBtn = tk.Button(mainwin)
        configBtn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        configBtn["font"] = ft
        configBtn["fg"] = "#000000"
        configBtn["justify"] = "center"
        configBtn["text"] = "Config"
        configBtn.place(x=20, y=20, width=70, height=25)
        configBtn["command"] = self.configClicked

        tileLbl = tk.Label(mainwin)
        ft = tkFont.Font(family='Times', size=28)
        tileLbl["font"] = ft
        tileLbl["fg"] = "#333333"
        tileLbl["justify"] = "center"
        tileLbl["text"] = "Bill Calculator"
        tileLbl.place(x=180, y=70, width=241, height=75)

        self.foodIdEntry = tk.Entry(mainwin)
        self.foodIdEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.foodIdEntry["font"] = ft
        self.foodIdEntry["fg"] = "#333333"
        self.foodIdEntry["justify"] = "center"
        self.foodIdEntry["text"] = "Entry"
        self.foodIdEntry.place(x=290, y=160, width=116, height=30)

        foodIdLbl = tk.Label(mainwin)
        ft = tkFont.Font(family='Times', size=10)
        foodIdLbl["font"] = ft
        foodIdLbl["fg"] = "#333333"
        foodIdLbl["justify"] = "center"
        foodIdLbl["text"] = "Food Id"
        foodIdLbl.place(x=210, y=160, width=75, height=30)

        addBTN = tk.Button(mainwin)
        addBTN["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        addBTN["font"] = ft
        addBTN["fg"] = "#000000"
        addBTN["justify"] = "center"
        addBTN["text"] = "Add"
        addBTN.place(x=270, y=200, width=70, height=25)
        addBTN["command"] = self.addMenu

        self.menuList = tk.Listbox(mainwin)
        ft = tkFont.Font(family='Times', size=10)
        self.menuList.place(x=200, y=240, width=214, height=207)

        doneBTN = tk.Button(mainwin)
        doneBTN["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        doneBTN["font"] = ft
        doneBTN["fg"] = "#000000"
        doneBTN["justify"] = "center"
        doneBTN["text"] = "Done"
        doneBTN.place(x=230, y=460, width=70, height=25)
        doneBTN["command"] = self.exportBill

        self.totalpriceLBL = tk.Label(mainwin)
        ft = tkFont.Font(family='Times', size=10)
        self.totalpriceLBL["font"] = ft
        self.totalpriceLBL["fg"] = "#333333"
        self.totalpriceLBL["justify"] = "center"
        self.totalpriceLBL["text"] = "Total: ${}".format(self.totalPrice)
        self.totalpriceLBL.place(x=310, y=460, width=70, height=25)

    def configClicked(self):

        configWindow = tk.Toplevel()
        configWindow.geometry("400x300")

        passwordInput = tk.Entry(configWindow, show='*')
        passwordInput.place(x=160, y=20, width=70, height=25)

        def verify():
            password = passwordInput.get()
            if password == '1234':
                print('password correct')

        passwordlbl = tk.Label(configWindow)
        ft = tkFont.Font(family='Times', size=10)
        passwordlbl["font"] = ft
        passwordlbl["fg"] = "#333333"
        passwordlbl["justify"] = "center"
        passwordlbl["text"] = "Password"
        passwordlbl.place(x=90, y=20, width=70, height=25)

        verifyButton = tk.Button(configWindow)
        verifyButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        verifyButton["font"] = ft
        verifyButton["fg"] = "#000000"
        verifyButton["justify"] = "center"
        verifyButton["text"] = "Verify"
        verifyButton.place(x=240, y=20, width=70, height=25)
        verifyButton["command"] = verify



    def verify(self):
        pass

    def addMenu(self):
        a = 0
        foodid = self.foodIdEntry.get()
        try:
            currentfoodM = '{}'.format(menusName[foodid])
            currentfoodP = '{}'.format(menusPrice[foodid])
            currentfood = '{}\n${}\n--------\n'.format(currentfoodM, currentfoodP)
            if self.addTimes == 1:
                currentfood = '--------\n{}\n${}\n--------\n'.format(currentfoodM, currentfoodP)
            self.menuList.insert(self.addTimes, '{} | Price: ${}'.format(currentfoodM, currentfoodP))
            print(currentfood, end='')
            self.orders += currentfood
            self.addTimes += 1
            self.totalPrice += int(currentfoodP)
            self.totalpriceLBL["text"] = "Total: ${}".format(self.totalPrice)
            self.foodIdEntry.delete(0, len(foodid))
        except KeyError:
            if foodid == '':
                messagebox.showerror('Error', 'Provide an Id')
            else:
                messagebox.showerror("Error", "The Id '{}' doesn't exists".format(foodid))

    def exportBill(self):
        if self.orders == '':
            messagebox.showerror('Error', 'No Items')
        else:
            self.bills += 1
            datet = datetime.datetime.now()
            f = open('bill{}.txt'.format(self.bills), 'w')
            f.write('{}Total Price : ${}\nDate: {}'.format(self.orders, self.totalPrice, datet))
            print('Total Price : ${}'.format(self.totalPrice))
            messagebox.showinfo('Done', 'File Save Successfully')


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
