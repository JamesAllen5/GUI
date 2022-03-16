import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry("600x300")

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.tb_val1 = tkinter.IntVar()
        self.tb_val2 = tkinter.IntVar()
        self.tb_val3 = tkinter.IntVar()

        # set the intVar objects to 0
        self.tb_val1.set(0)
        self.tb_val2.set(0)
        self.tb_val3.set(0)

        self.prompt_label1 = tkinter.Label(
            self.top_frame, text="Enter the score for test 1:"
        )

        self.tb1 = tkinter.Entry(self.top_frame, width=10)
        # text="Enter the score for test 1:",
        # variable=self.tb_val1,

        self.prompt_label2 = tkinter.Label(
            self.top_frame, text="Enter the score for test 2:"
        )

        self.tb2 = tkinter.Entry(
            self.top_frame,
            # text="Enter the score for test 2:",
            # variable=self.tb_val2,
            width=10,
        )

        self.prompt_label3 = tkinter.Label(
            self.top_frame, text="Enter the score for test 3:"
        )

        self.tb3 = tkinter.Entry(
            self.top_frame,
            # text="Enter the score for test 3:",
            # variable=self.tb_val3,
            width=10,
        )

        self.prompt_label1.pack(side="left")
        self.prompt_label2.pack(side="left")
        self.prompt_label3.pack(side="left")

        self.tb1.pack()
        self.tb2.pack()
        self.tb3.pack()

        self.top_frame.pack(side="top")
        self.bottom_frame.pack(side="top")

        self.calcbutton = tkinter.Button(
            self.main_window, text="Average", command=self.convert
        )

        self.quit_button = tkinter.Button(
            self.main_window, text="Quit", command=self.main_window.destroy
        )

        self.calcbutton.pack(side="left")
        self.quit_button.pack(side="right")

        tkinter.mainloop()

    def convert(self):
        score1 = float(self.self.tb_val1.get())
        score2 = float(self.self.tb_val2.get())
        score3 = float(self.self.tb_val3.get())

        average = round((score1 + score2 + score3) / 3, 2)

        tkinter.messagebox.showinfo("Average: ", str(average))


my_gui = MyGUI()
