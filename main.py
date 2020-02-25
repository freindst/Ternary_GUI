from tkinter import *
from tkinter import ttk


class ternary:

    def __init__(self):
        self.ordinary = {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0
        }
    def set_ordinary(self, key, value):
        self.ordinary[key] = value

    def toInt(self):
        result = 0
        mul = 0
        for i in range(5):
            if (mul == 0):
                mul = 1
            else:
                mul = mul * 3
            result = result + mul * self.ordinary[4 - i]
        return result
    
    def toBalanced(self):
        temp = []
        carry = 0
        for i in range(5):
            index = 4 - i
            num = self.ordinary[index]
            current = num + carry + 1
            if current > 2:
                carry = 1
                current = current - 3
            else:
                carry = 0
            temp.insert(0, current)
        if carry == 1:
            temp.insert(0, 2)
        result = ''
        enum = {
            0: "1'",
            1: '0',
            2: '1'
        }
        for element in temp:
            result = result + enum[element]
        return result

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.inputs = []
        self.init_window()
        self.ternary_driver = ternary()

    def init_window(self):
        self.master.title("Ternary Converter")

        self.pack(fill=BOTH, expand=1)

        # 1
        frame_top = Frame(self, highlightbackground='black', highlightthickness=2)
        frame_top.pack(fill=BOTH, expand=1)
        label_top = Label(frame_top, text='Normal Ternary (0, 1, 2)', font=('Helvetica', 24))
        label_top.pack()

        frame_grid = Frame(frame_top)
        frame_grid.pack(fill=BOTH, expand=1)

        for i in range(5):
            frame_grid_cell = Frame(frame_grid)
            frame_grid_cell.grid(column=i,row=0,sticky=W,padx=5,pady=5)
            combo = ttk.Combobox(frame_grid_cell, values=[0,1,2], width=5)
            combo.grid(column=0,row=0)
            combo.current(0)
            combo.bind("<<ComboboxSelected>>", self.update_display_event)
            self.inputs.append(combo)

        frame_grid_cell_int = Frame(frame_grid)
        frame_grid_cell_int.grid(column=5,row=0,sticky=W,padx=5,pady=5)
        self.label_int = Label(frame_grid_cell_int, text='= 0')
        self.label_int.grid(column=0,row=0)

        # 2
        frame_middle = Frame(self, padx=5, pady=5)
        frame_middle.pack()
        button_convert = Button(frame_middle, text='CONVERT', font=('Helvetica', 12), command=self.update_display)
        button_convert.pack()

        # 3
        frame_bottom = Frame(self, highlightbackground='black', highlightthickness=2)
        frame_bottom.pack(fill=BOTH, expand=1)
        label_bottom = Label(frame_bottom, text="Balanced Ternary (1', 0, 1)", font=('Helvetica', 24))
        label_bottom.pack()

        frame_answer = Frame(frame_bottom)
        frame_answer.pack(fill=BOTH, expand=1)

        self.label_answer = Label(frame_answer, text='00000', font=('Helvetica', 30))
        self.label_answer.pack(fill=BOTH, expand=1)

    def update_display_event(self, event):
        self.update_display()

    def update_display(self):
        for i in range(5):
            combo = self.inputs[i]
            self.ternary_driver.set_ordinary(i, combo.current())
        self.label_int.configure(text='= {0}'.format(self.ternary_driver.toInt()))
        self.label_answer.configure(text=self.ternary_driver.toBalanced())

root = Tk()

app = Window(root)

root.geometry('400x300')

root.mainloop()

        

            





    