from tkinter import *

class Fullscreen_Window:
    def __init__(self):
        self.tk = Tk()
        frame = Frame(self.tk, width=1000, heigh=600)
        frame.pack()
        frame.pack_propagate(False)
        button = Button(frame, text='hello world', width=20, height=2)
        button.pack()
        self.state = False
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.exit)
        self.tk.mainloop()

    def toggle_fullscreen(self, event=None):
        self.state = not self.state
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def exit(self, event=None):
        return sys.exit(0)

if __name__ == '__main__':
    window = Fullscreen_Window()