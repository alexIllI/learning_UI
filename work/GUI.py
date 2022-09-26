# Multi-frame tkinter application v2.2
import tkinter as tk
import sys
import tkinter.messagebox
import tkinter.font as tkFont
from tkinter import ttk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
import tkinter


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
LIB_PATH = OUTPUT_PATH / Path("./PackingElf")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(LIB_PATH))

try:
    from PackingElf.Account import LOGIN
except ModuleNotFoundError:
    raise RuntimeError("Couldn't add Account to the PATH.")

from PackingElf import MyACG

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(START_PAGE)       

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class START_PAGE(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, height=566, width=795, bg="#D1E1F0")

        self.master = master
        self.master.title("Packing Elf")
        self.master.iconphoto(False, PhotoImage(
            file=relative_to_assets("icon.png")))
        master.geometry("795x566")

        self.canvas = Canvas(
            self,
            bg="#D1E1F0",
            height=566,
            width=795,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            176.0,
            283.0,
            image=self.image_image_1
        )

        self.canvas.create_text(
            626.0,
            541.0,
            anchor="nw",
            text="Meridian Project",
            fill="#000000",
            font=("Harshita", 16 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: master.switch_frame(LOGIN_METHOD),
            relief="flat"
        )
        button_1.place(
            x=442.0,
            y=226.0,
            width=256.0,
            height=44.0
        )
        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print('bt2'),
            relief="flat"
        )
        button_2.place(
            x=442.0,
            y=334.0,
            width=256.0,
            height=44.0
        )
        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print('bt3'),
            relief="flat"
        )
        button_3.place(
            x=447.0,
            y=441.0,
            width=256.0,
            height=44.0
        )

        self.canvas.create_text(
            452.0,
            102.0,
            anchor="nw",
            text="包貨",
            fill="#3E3E3E",
            font=("SourceHanSerifTW-Medium", 48 * -1)
        )

        self.canvas.create_text(
            552.0,
            102.0,
            anchor="nw",
            text="小精靈",
            fill="#76BAEC",
            font=("SourceHanSerifTW-Medium", 48 * -1)
        )

        self.canvas.pack()

class LOGIN_METHOD(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, height=566, width=795, bg="#D1E1F0")

        self.master = master
        self.master.title("Packing Elf")
        self.master.iconphoto(False, PhotoImage(
            file=relative_to_assets("icon.png")))
        master.geometry("795x566")

        self.canvas = Canvas(
            self,
            bg="#D1E1F0",
            height=566,
            width=795,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.create_text(
            626.0,
            541.0,
            anchor="nw",
            text="Meridian Project",
            fill="#000000",
            font=("Harshita", 16 * -1)
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            443.0,
            566.0,
            fill="#D1E1F0",
            outline="")

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5 = Button(
            self,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: master.switch_frame(START_PAGE),
            relief="flat"
        )
        button_5.place(
            x=502.0,
            y=486.0,
            width=148.0,
            height=44.0
        )
        self.button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        button_6 = Button(
            self,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: master.switch_frame(CHOOSE_ACCOUNT),
            relief="flat"
        )
        button_6.place(
            x=417.0,
            y=129.0,
            width=303.0,
            height=53.0
        )
        self.button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        button_7 = Button(
            self,
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: master.switch_frame(ADD_ACCOUNT),
            relief="flat"
        )
        button_7.place(
            x=417.0,
            y=214.0,
            width=303.0,
            height=53.0
        )
        self.button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        button_8 = Button(
            self,
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_8 clicked"),
            relief="flat"
        )
        button_8.place(
            x=417.0,
            y=299.0,
            width=303.0,
            height=53.0
        )
        self.button_image_9 = PhotoImage(
            file=relative_to_assets("button_9.png"))
        button_9 = Button(
            self,
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_9 clicked"),
            relief="flat"
        )
        button_9.place(
            x=417.0,
            y=384.0,
            width=303.0,
            height=53.0
        )

        self.canvas.create_text(
            460.0,
            55.0,
            anchor="nw",
            text="選擇登入方式",
            fill="#000000",
            font=("ShadowsIntoLight", 36 * -1)
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
            
        image_1 = self.canvas.create_image(
            176.0,
            283.0,
            image=self.image_image_1
        )

        self.canvas.pack()

class CHOOSE_ACCOUNT(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, height=566, width=795, bg="#D1E1F0")
        
        self.G_account_name = 'NONE'
        self.M_account_name = ''
        self.INFO = []

        self.master = master
        self.master.title("Packing Elf")
        self.master.iconphoto(False, PhotoImage(
            file=relative_to_assets("icon.png")))
        master.geometry("795x566")
        
        self.account = LOGIN()

        self.canvas = Canvas(
            self,
            bg="#D1E1F0",
            height=566,
            width=795,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.create_text(
            626.0,
            541.0,
            anchor="nw",
            text="Meridian Project",
            fill="#000000",
            font=("Harshita", 16 * -1)
        )

        def show_data_1(*args):
            print("Event: Combobox_1_Selected") 
            print(self.cbx_1.get())
            self.G_account_name = self.cbx_1.get()

        def show_data_2(*args):
            print("Event: Combobox_2_Selected")
            print(self.cbx_2.get())
            self.M_account_name = self.cbx_2.get()

        self.entry_getURL = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0,
            font=bigfont
        )
        self.entry_getURL.place(
            x=393.0,
            y=404.0,
            width=345.0,
            height=40.0
        ) 

        self.cbx_1 = ttk.Combobox(self ,width = 17, height = 4, font = ("SegoeUI",30))
        self.cbx_1.place(x = 393.0, y = 156.0)
        self.cbx_1["values"] = self.account.READ_GOOGLE(login_info='NAME')

        self.cbx_2 = ttk.Combobox(self ,width = 17, height = 4, font = ("SegoeUI",30))
        self.cbx_2.place(x = 393.0, y = 279.0)
        self.cbx_2["values"] = self.account.READ_MYACG(login_info='NAME')

        self.cbx_1.configure(state = "readonly")
        self.cbx_1.current(0)
        self.cbx_1.bind("<<ComboboxSelected>>",show_data_1)
        self.cbx_2.configure(state = "readonly")
        self.cbx_2.current(0)
        self.cbx_2.bind("<<ComboboxSelected>>",show_data_2)

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(
            570.0,
            124.0,
            image=self.image_image_3
        )

        self.button_image_10 = PhotoImage(
            file=relative_to_assets("button_10.png"))
        button_10 = Button(
            self,
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.OK_pressed(),
            relief="flat"
        )
        button_10.place(
            x=399.0,
            y=486.0,
            width=148.0,
            height=44.0
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5 = Button(
            self,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: master.switch_frame(START_PAGE),
            relief="flat"
        )
        button_5.place(
            x=600.0,
            y=486.0,
            width=148.0,
            height=44.0
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        image_4 = self.canvas.create_image(
            570.0,
            243.0,
            image=self.image_image_4
        )

        self.image_image_7 = PhotoImage(
            file=relative_to_assets("image_7.png"))
        image_7 = self.canvas.create_image(
            570.0,
            372.0,
            image=self.image_image_7
        )

        self.canvas.create_text(
            465.0,
            32.0,
            anchor="nw",
            text="選擇登入帳號",
            fill="#000000",
            font=("SeoulNamsan CL", 36 * -1)
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
            
        image_1 = self.canvas.create_image(
            176.0,
            283.0,
            image=self.image_image_1
        )

        self.canvas.pack()

    def OK_pressed(self):
        #if self.G_account_name == 'NONE':
        self.INFO = self.account.READ_MYACG(name = self.M_account_name)

        self.master.withdraw()
        toplevel=tk.Toplevel(self.master)
        toplevel.iconphoto(False, PhotoImage(
                file=relative_to_assets("icon.png")))
        toplevel.title('離開包貨小精靈')

        tk.Button(toplevel, text="Exit the program",
                  command=lambda: self.Exit_pressed()).pack()

        self.newWindow = tk.Toplevel(app)
        self.newWindow.bind('<Return>', self.Print_order)
        self.newWindow.geometry("354x105")
        self.newWindow.title('Enter Order Numbers')
        self.newWindow.iconphoto(False, PhotoImage(
                file=relative_to_assets("icon.png")))

        self.newWindow.attributes("-topmost", True)

        self.newWindow_canvas = Canvas(
                self.newWindow,
                bg = "#FFFFFF",
                height = 105,
                width = 354,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
        )
        self.newWindow_canvas.place(x = 0, y = 0)
        self.newWindow_canvas.create_rectangle(
        0.0,
        0.0,
        352.0,
        105.0,
        fill="#FFFFFF",
        outline="")

        self.entry_image_1 = PhotoImage(
                file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.newWindow_canvas.create_image(
                177.0,
                45.0,
                image = self.entry_image_1
        )
        self.entry_1 = Entry(
                self.newWindow,
                bd=0,
                bg="#D9D9D9",
                highlightthickness=0
        )
        self.entry_1.place(
                x=30.0,
                y=40.0,
                width=250.0,
                height=20.0
        )
        self.entry_1.focus_set()

        self.button_image_4 = PhotoImage(
                file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
                self.newWindow,
                image=self.button_image_4,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.Print_order(),
                relief="flat"
        )
        self.button_4.place(
                x=136.0,
                y=79.0,
                width=81.0,
                height=20.0
        )
  
        self.myacg = MyACG.MYACG(self.INFO[0], self.INFO[1])

    def Exit_pressed(self):
        self.master.quit()
        self.myacg.quit()

    def Print_order(self, *args):
        nums = self.entry_1.get()

        if not nums:
                tkinter.messagebox.showinfo(
                title="Empty Fields!", message="Please enter Order Numbers.")
        elif not nums.isdigit():
                tkinter.messagebox.showinfo(
                title="Syntax Error!", message="Please enter ONLY Numbers.")                             
        elif len(nums) != 5:
                tkinter.messagebox.showinfo(
                title="Wrong Length!", message="Please enter ONLY 5 Numbers.")
        else:          
            print(nums)
            self.myacg.put_order_num(order_num= nums)
            
            self.entry_1.delete(0, 'end')


class ADD_ACCOUNT(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, height=566, width=795, bg="#D1E1F0")

        self.Method = 'NONE'
        
        self.master = master
        self.master.title("Packing Elf")
        self.master.iconphoto(False, PhotoImage(
            file=relative_to_assets("icon.png")))
        master.geometry("795x566")

        self.canvas = Canvas(
            self,
            bg="#D1E1F0",
            height=566,
            width=795,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.create_text(
            626.0,
            541.0,
            anchor="nw",
            text="Meridian Project",
            fill="#000000",
            font=("Harshita", 16 * -1)
        )

        self.button_image_10 = PhotoImage(
            file=relative_to_assets("button_10.png"))
        button_10 = Button(
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.BTN_clicked('OK'),
            relief="flat"
        )
        button_10.place(
            x=399.0,
            y=487.0,
            width=148.0,
            height=44.0
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.BTN_clicked('CANCEL'),
            relief="flat"
        )
        button_5.place(
            x=600.0,
            y=487.0,
            width=148.0,
            height=44.0
        )

        self.button_image_11 = PhotoImage(
            file=relative_to_assets("button_11.png"))
        button_11 = Button(
            image=self.button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.BTN_clicked('GOOGLE'),
            relief="flat"
        )
        button_11.place(
            x=422.0,
            y=223.0,
            width=304.0,
            height=44.0
        )

        self.button_image_12 = PhotoImage(
            file=relative_to_assets("button_12.png"))
        button_12 = Button(
            image=self.button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.BTN_clicked('MYACG'),
            relief="flat"
        )

        button_12.place(
            x=422.0,
            y=387.0,
            width=304.0,
            height=44.0
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        image_5 = self.canvas.create_image(
            570.0,
            171.0,
            image=self.image_image_5
        )

        self.canvas.create_text(
            457.0,
            54.0,
            anchor="nw",
            text="新建帳號網站",
            fill="#000000",
            font=("ShadowsIntoLight", 36 * -1)
        )

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        image_6 = self.canvas.create_image(
            570.0,
            345.0,
            image=self.image_image_6
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
            
        image_1 = self.canvas.create_image(
            176.0,
            283.0,
            image=self.image_image_1
        )

        self.canvas.pack()

    def BTN_clicked(self, btn):
        
        match btn:
            case 'GOOGLE':
                self.Method = 'GOOGLE'

            case 'MYACG':
                self.Method = 'MYACG'

            case 'OK':
                if self.Method == 'NONE':
                    tkinter.messagebox.showinfo(
                        title="Empty Selection", message="Please select website.")
                    return

                elif self.Method == 'GOOGLE':
                    tkinter.messagebox.showinfo(
                        title="Choose website", message="新增Google帳號")
                    self.master.switch_frame(NEW_G_ACCOUNT_INFO)

                elif self.Method == 'MYACG':
                    tkinter.messagebox.showinfo(
                        title="Choose website", message="新增買動漫帳號")
                    self.master.switch_frame(NEW_M_ACCOUNT_INFO)

            case 'CANCEL':
                self.Method = 'NONE'
                self.master.switch_frame(START_PAGE)

class NEW_G_ACCOUNT_INFO(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, height=566, width=795, bg="#D1E1F0")

        self.master = master
        master.title("Packing Elf")
        master.iconphoto(False, PhotoImage(
            file=relative_to_assets("icon.png")))
        master.geometry("795x566")

        print('this is google')

        self.canvas = Canvas(
            self,
            bg="#D1E1F0",
            height=566,
            width=795,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.create_text(
            626.0,
            541.0,
            anchor="nw",
            text="Meridian Project",
            fill="#000000",
            font=("Harshita", 16 * -1)
        )

        self.button_image_10 = PhotoImage(
            file=relative_to_assets("button_10.png"))
        button_10 = Button(
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.OK_clicked(),
            relief="flat"
        )
        button_10.place(
            x=399.0,
            y=486.0,
            width=148.0,
            height=44.0
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5 = Button(
            self,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: master.switch_frame(START_PAGE),
            relief="flat"
        )
        button_5.place(
            x=600.0,
            y=486.0,
            width=148.0,
            height=44.0
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            568.0,
            160.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#E5E4E4",
            highlightthickness=0
        )
        self.entry_2.place(
            x=427.0,
            y=154.0,
            width=252.0,
            height=20.0
        )

        self.canvas.create_text(
            426.0,
            119.0,
            anchor="nw",
            text="NAME",
            fill="#000000",
            font=("SegoeUI", 12 * -1)
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(
            568.0,
            245.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#E5E4E4",
            highlightthickness=0
        )
        self.entry_3.place(
            x=427.0,
            y=239.0,
            width=252.0,
            height=20.0
        )

        self.canvas.create_text(
            426.0,
            204.0,
            anchor="nw",
            text="ACCOUNT",
            fill="#000000",
            font=("SegoeUI", 12 * -1)
        )

        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image(
            568.0,
            330.0,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#E5E4E4",
            highlightthickness=0,
            show= '*'
        )
        self.entry_4.place(
            x=427.0,
            y=324.0,
            width=252.0,
            height=20.0
        )

        self.canvas.create_text(
            426.0,
            289.0,
            anchor="nw",
            text="PASSWORD",
            fill="#000000",
            font=("SegoeUI", 12 * -1)
        )

        self.entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_5.png"))
        entry_bg_5 = self.canvas.create_image(
            568.0,
            415.0,
            image=self.entry_image_5
        )
        self.entry_5 = Entry(
            bd=0,
            bg="#E5E4E4",
            highlightthickness=0,
            show= '*'
        )
        self.entry_5.place(
            x=427.0,
            y=409.0,
            width=252.0,
            height=20.0
        )

        self.canvas.create_text(
            426.0,
            374.0,
            anchor="nw",
            text="CONFIRM PASSWORD",
            fill="#000000",
            font=("SegoeUI", 12 * -1)
        )

        self.canvas.create_text(
            460.0,
            49.0,
            anchor="nw",
            text="輸入登入資訊",
            fill="#000000",
            font=("ShadowsIntoLight", 36 * -1)
        )


        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
            
        image_1 = self.canvas.create_image(
            176.0,
            283.0,
            image=self.image_image_1
        )

        self.canvas.pack()

    def OK_clicked(self):
        name = self.entry_2.get()
        account = self.entry_3.get()
        password = self.entry_4.get()
        confirmation = self.entry_5.get()

        if not name:
            tkinter.messagebox.showinfo(
                title="Empty Name!", message="Please enter account Name.")

        elif not account:
            tkinter.messagebox.showinfo(
                title="Empty Account!", message="Please enter Account.")

        elif not password:
            tkinter.messagebox.showinfo(

                title="Empty Password!", message="Please enter Password.")
        elif not confirmation:
            tkinter.messagebox.showinfo(
                title="Empty Password Confirmation!", message="Please Confirm Password.")

        elif password != confirmation:
            tkinter.messagebox.showinfo(
                title="Wrong Confirmation!", message="Please enter Confirmation Password again.")
            self.entry_5.delete(0, 'end')
        else:
            Store_ = LOGIN()
            Store_.WRITE_GOOGLE(name, account, password)
            self.entry_2.delete(0, 'end')
            self.entry_3.delete(0, 'end')
            self.entry_4.delete(0, 'end')
            self.entry_5.delete(0, 'end')
            tkinter.messagebox.showinfo(
                title="Saving Login Info", message="SUCESS!")
            self.master.switch_frame(START_PAGE)

class NEW_M_ACCOUNT_INFO(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, height=566, width=795, bg="#D1E1F0")

        self.master = master
        master.title("Packing Elf")
        master.iconphoto(False, PhotoImage(
            file=relative_to_assets("icon.png")))
        master.geometry("795x566")

        print('this is myacg')

        self.canvas = Canvas(
            self,
            bg="#D1E1F0",
            height=566,
            width=795,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.create_text(
            626.0,
            541.0,
            anchor="nw",
            text="Meridian Project",
            fill="#000000",
            font=("Harshita", 16 * -1)
        )

        self.button_image_10 = PhotoImage(
            file=relative_to_assets("button_10.png"))
        button_10 = Button(
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.OK_clicked(),
            relief="flat"
        )
        button_10.place(
            x=399.0,
            y=486.0,
            width=148.0,
            height=44.0
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5 = Button(
            self,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: master.switch_frame(START_PAGE),
            relief="flat"
        )
        button_5.place(
            x=600.0,
            y=486.0,
            width=148.0,
            height=44.0
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            568.0,
            160.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#E5E4E4",
            highlightthickness=0
        )
        self.entry_2.place(
            x=427.0,
            y=154.0,
            width=252.0,
            height=20.0
        )

        self.canvas.create_text(
            426.0,
            119.0,
            anchor="nw",
            text="NAME",
            fill="#000000",
            font=("SegoeUI", 12 * -1)
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(
            568.0,
            245.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#E5E4E4",
            highlightthickness=0
        )
        self.entry_3.place(
            x=427.0,
            y=239.0,
            width=252.0,
            height=20.0
        )

        self.canvas.create_text(
            426.0,
            204.0,
            anchor="nw",
            text="ACCOUNT",
            fill="#000000",
            font=("SegoeUI", 12 * -1)
        )

        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image(
            568.0,
            330.0,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#E5E4E4",
            highlightthickness=0,
            show= '*'
        )
        self.entry_4.place(
            x=427.0,
            y=324.0,
            width=252.0,
            height=20.0
        )

        self.canvas.create_text(
            426.0,
            289.0,
            anchor="nw",
            text="PASSWORD",
            fill="#000000",
            font=("SegoeUI", 12 * -1)
        )

        self.entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_5.png"))
        entry_bg_5 = self.canvas.create_image(
            568.0,
            415.0,
            image=self.entry_image_5
        )
        self.entry_5 = Entry(
            bd=0,
            bg="#E5E4E4",
            highlightthickness=0,
            show= '*'
        )
        self.entry_5.place(
            x=427.0,
            y=409.0,
            width=252.0,
            height=20.0
        )

        self.canvas.create_text(
            426.0,
            374.0,
            anchor="nw",
            text="CONFIRM PASSWORD",
            fill="#000000",
            font=("SegoeUI", 12 * -1)
        )

        self.canvas.create_text(
            460.0,
            49.0,
            anchor="nw",
            text="輸入登入資訊",
            fill="#000000",
            font=("ShadowsIntoLight", 36 * -1)
        )


        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
            
        image_1 = self.canvas.create_image(
            176.0,
            283.0,
            image=self.image_image_1
        )

        self.canvas.pack()
    
    def OK_clicked(self):
        name = self.entry_2.get()
        account = self.entry_3.get()
        password = self.entry_4.get()
        confirmation = self.entry_5.get()

        if not name:
            tkinter.messagebox.showinfo(
                title="Empty Name!", message="Please enter account Name.")

        elif not account:
            tkinter.messagebox.showinfo(
                title="Empty Account!", message="Please enter Account.")

        elif not password:
            tkinter.messagebox.showinfo(

                title="Empty Password!", message="Please enter Password.")
        elif not confirmation:
            tkinter.messagebox.showinfo(
                title="Empty Password Confirmation!", message="Please Confirm Password.")

        elif password != confirmation:
            tkinter.messagebox.showinfo(
                title="Wrong Confirmation!", message="Please enter Confirmation Password again.")
            self.entry_5.delete(0, 'end')
        else:
            Store_ = LOGIN()
            Store_.WRITE_MYACG(name, account, password)
            self.entry_2.delete(0, 'end')
            self.entry_3.delete(0, 'end')
            self.entry_4.delete(0, 'end')
            self.entry_5.delete(0, 'end')
            tkinter.messagebox.showinfo(
                title="Saving Login Info", message="SUCESS!")
            self.master.switch_frame(START_PAGE)

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, height=566, width=795, bg="#D1E1F0")

        self.master = master
        self.master.title("Packing Elf")
        self.master.iconphoto(False, PhotoImage(
            file=relative_to_assets("icon.png")))
        master.geometry("795x566")

        self.canvas = Canvas(
            self,
            bg="#D1E1F0",
            height=566,
            width=795,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.create_text(
            626.0,
            541.0,
            anchor="nw",
            text="Meridian Project",
            fill="#000000",
            font=("Harshita", 16 * -1)
        )




        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
            
        image_1 = self.canvas.create_image(
            176.0,
            283.0,
            image=self.image_image_1
        )

        self.canvas.pack()


if __name__ == "__main__":
    app = App()
    bigfont = tkFont.Font(family="SegoeUI",size=20)
    app.option_add("*TCombobox*Listbox*Font", bigfont)
    app.resizable(False,False)
    app.mainloop()
