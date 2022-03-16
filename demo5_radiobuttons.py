import tkinter
import tkinter.messagebox


class KiloConverterGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()

        # set the interVar object to 1
        self.radio_var.set(2)

        self.rb1 = tkinter.Radiobutton(
            self.top_frame, text="Option1", variable=self.radio_var, value=1
        )

        self.rb2 = tkinter.Radiobutton(
            self.top_frame, text="Option2", variable=self.radio_var, value=2
        )

        self.rb3 = tkinter.Radiobutton(
            self.top_frame, text="Option3", variable=self.radio_var, value=3
        )

        # set the default button
        self.rb2.select()

        # Pack the radiobuttons
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.ok_button = tkinter.Button(
            self.bottom_frame, text="OK", command=self.show_choice
        )

        self.reset_button = tkinter.Button(
            self.bottom_frame, text="Reset", command=self.rb1.select
        )

        self.quit_button = tkinter.Button(
            self.bottom_frame, text="Quit!", command=self.main_window.destroy
        )

        self.ok_button.pack(side="left")
        self.reset_button.pack(side="left")
        self.quit_button.pack(side="left")

        # Yes, we have to pack the frames too!
        self.top_frame.pack(side="top")
        self.bottom_frame.pack(side="top")

        tkinter.mainloop()

    def show_choice(self):
        tkinter.messagebox.showinfo(
            "Selection", "You have selected option" + str(self.radio_var.get())
        )


my_gui = KiloConverterGUI()
