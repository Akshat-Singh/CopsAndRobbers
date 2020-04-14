from tkinter import *
from tkinter import messagebox


def nodeClicked(nodeIndex):
    Tk().wm_withdraw()  # to hide the main window
    messagebox.showinfo('Node', 'Node: ' + str(nodeIndex))