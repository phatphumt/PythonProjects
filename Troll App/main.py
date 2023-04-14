from tkinter import *
import pyautogui
import webbrowser
import random
import time

width, height = pyautogui.size()


class MainWindow:
    def __init__(self, win):
        self.a = 0
        self.window = None
        btn = Button(self.window, text="Yes", fg='blue', command=self.clickyes)
        btn.place(x=80, y=100)
        self.btnNo = Button(self.window, text="No", fg='red', command=self.clickno)
        self.btnNo.place(x=180, y=100)
        lbl = Label(self.window, text="Do you want to see virus?", font=("Helvetica", 16))
        lbl.place(x=30, y=40)

    def clickyes(self):
        mediaWindow = Toplevel(self.window)
        mediaWindow.geometry("{}x{}".format(width, height))
        btn = Button(mediaWindow, text="Sure, Click Here to Proceed", font=("Helvetica", 100), command=self.openWeb)
        btn.place(relx=0.5, rely=0.5, anchor=CENTER)

    def clickno(self):
        ya = random.randint(50, 100)
        xa = random.randint(50, 200)
        self.btnNo.place(x=xa, y=ya)
        self.a += 1
        if self.a == 5:
            webbrowser.open('https://bit.ly/3MfC9ew')

    def openWeb(self):
        webbrowser.open('https://bit.ly/3MfC9ew')
        time.sleep(1)
        webbrowser.open('https://bit.ly/416aosO')


window = Tk()
windows = MainWindow(window)
window.title('By Phatphum')
window.geometry("300x150")
window.mainloop()
