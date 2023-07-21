import tkinter as tk
from tkinter import *

class ScrollableTextBar:
    # variables
    __root = Tk()

    # default window width and height
    __thisWidth = 600
    __thisHeight = 100
    font_size = tk.IntVar()
    font_size.set(18)
    __thisTextArea = Text(__root, font=("Calibri", font_size.get()))
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None
    def __init__(self):
        # center the window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        left = (screenWidth / 2) - (self.__thisWidth / 2)
        top = 0

        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, left, top))

        # to make the textarea auto resizable
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        # add controls (widget)

        self.__thisTextArea.grid(sticky=N + E + S + W)

        # Bind keyboard shortcuts to increase/decrease font size
        self.__root.bind('<Command-Up>', self.increase_font)
        self.__root.bind('<Command-Down>', self.decrease_font)

        self.__root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=RIGHT, fill=Y)
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
        self.__root.attributes('-topmost', 1)

    def increase_font(self, event=None):
        self.font_size.set(self.font_size.get() + 1)
        self.__thisTextArea.configure(font=("Calibri", self.font_size.get()))

    def decrease_font(self, event=None):
        if self.font_size.get() > 1:  # Ensure font size stays positive
            self.font_size.set(self.font_size.get() - 1)
        self.__thisTextArea.configure(font=("Calibri", self.font_size.get()))

    def run(self):
        self.__root.mainloop()

# Run the application
app = ScrollableTextBar()
app.run()
