
from tkinter import Tk, Frame, Menu, Label, Text, Button, ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

class GUI(Frame):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.master.title("TOPAS exporter")

        # Create text widget and specify size.
        T = Text(self.master)
        pb = ttk.Progressbar(length='550')
        b1 = Button(self.master, text = 'Open', command= self.openFile)

        T.pack()
        b1.pack(side='left')
        pb.pack(side='left')

    def openFile(self):
        filetypes = (
        ('PX databases', '*.DB *.VAL'),
        ('All files', '*.*')
        )

        filenames= fd.askopenfilename(
            title='Open files',
            initialdir='./',
            filetypes=filetypes)

        return filenames


def main():
    root = Tk()
    root.geometry("640x480+300+300")
    app = GUI()
    root.mainloop()

if __name__ == '__main__':
    main()