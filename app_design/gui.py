from tkinter import *
from check import *
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
from PIL import ImageTk, Image
import subprocess
import os
import cv2


class Intro:
    def __init__(self, root):
        self.root = root
        self.root.title("Road Damage Detector")
        self.width = 764
        self.height = 520
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (self.width, self.height, (screenwidth -
                                                              self.width) / 2, (screenheight - self.height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)
        self.root.configure(bg='#E9EDC9')

        '''Logo Label Button'''
        logo_img = ImageTk.PhotoImage(Image.open('stop.jpg'))
        logo_label = tk.Label(self.root, image=logo_img)
        logo_label.image = logo_img
        logo_label.place(x=150, y=40, width=50, height=53)

        '''Welcome title'''
        welcomeTitle = tk.Label(self.root)
        # welcomeTitle["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=16)
        welcomeTitle["font"] = ft
        # welcomeTitle["fg"] = "#3656b7"
        welcomeTitle["bg"] = "#E9EDC9"
        welcomeTitle["justify"] = "center"
        welcomeTitle["text"] = "Road Damage Detector"
        welcomeTitle.place(x=280, y=40, width=200, height=58)

        '''BIT Logo Label Button'''
        bit_logo_img = ImageTk.PhotoImage(
            Image.open('BIT_logo.jpg'))
        bit_logo_label = tk.Label(self.root, image=bit_logo_img)
        bit_logo_label.image = bit_logo_img
        bit_logo_label.place(x=560, y=40, width=50, height=53)

        '''Team Label'''
        teamLabel = tk.Label(self.root)
        ft = tkFont.Font(family='Times', size=14)
        teamLabel["font"] = ft
        teamLabel["fg"] = "#333333"
        teamLabel["bg"] = "#E9EDC9"
        teamLabel["justify"] = "left"
        teamLabel["text"] = "Developed by"
        teamLabel.place(x=305, y=150, width=150, height=55)

        '''Author Label'''
        co = tk.Label(self.root)
        ft = tkFont.Font(family='Times', size=10)
        co["font"] = ft
        co["fg"] = "#333333"
        co["bg"] = "#E9EDC9"
        co["justify"] = "center"
        co["text"] = "School of Computer Science and Technology\nBeijing Institute of Technology"
        co.place(x=250, y=190, width=260, height=55)

        '''Instruction label'''
        inst_button = tk.Button(self.root)
        inst_button["bg"] = "#E9EDC9"
        ft = tkFont.Font(family='Times', size=10)
        inst_button["font"] = ft
        inst_button["fg"] = "#000000"
        inst_button["justify"] = "center"
        inst_button["text"] = "Check"
        inst_button.place(x=650, y=275, width=75, height=30)
        inst_button["command"] = self.inst_button_command

        '''check_device Dependencies'''
        check_device_button = tk.Label(self.root)
        ft = tkFont.Font(family='Times', size=10)
        check_device_button["font"] = ft
        check_device_button["fg"] = "#333333"
        check_device_button["bg"] = "#e7d8d8"
        check_device_button["justify"] = "center"
        check_device_button["text"] = "Check if the GPU is available or not."
        check_device_button.place(x=90, y=270, width=550, height=38)

        '''Msg Box'''
        msg_frame = tk.Frame(self.root)
        msg_frame.place(x=90, y=330, width=400, height=160)

        self.msg = tk.Text(msg_frame)
        ft = tkFont.Font(family='Times', size=10)
        self.msg["font"] = ft
        self.msg["fg"] = "#333333"
        # self.msg["justify"] = "left"
        self.msg.see("end")
        self.msg.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(msg_frame)
        scrollbar.pack(side="right", fill='y')

        # Bind the mouse wheel event to the text widget
        self.msg.bind("<MouseWheel>", lambda event: scrollbar.yview_scroll(
            int(-1*(event.delta/120)), "units"))

        self.msg.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.msg.yview)

        '''Next Button'''
        next_button = tk.Button(self.root)
        next_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        next_button["font"] = ft
        next_button["fg"] = "#000000"
        next_button["justify"] = "center"
        next_button["text"] = "Next"
        next_button.place(x=582, y=480, width=70, height=25)
        next_button["command"] = self.next_button_command

        '''Quit Button'''
        quit_button = tk.Button(self.root)
        quit_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        quit_button["font"] = ft
        quit_button["fg"] = "#000000"
        quit_button["justify"] = "center"
        quit_button["text"] = "Quit"
        quit_button.place(x=657, y=480, width=70, height=25)
        quit_button["command"] = self.quit_button_command

    def inst_button_command(self):
        self.msg.insert("end", "Please wait...")  # insert wait indicator text
        # self.msg.config(state="disabled")  # disable editing the message box
        self.msg.update()  # force update the UI to show the message

        a = check_dependency()
        self.msg.insert('end', '\n>> '+a)

    def next_button_command(self):
        self.root.destroy()
        root2 = tk.Tk()
        app1 = App(root2)
        root2.mainloop()
        # print("command")

    def quit_button_command(self):
        self.root.destroy()


class App:

    def __init__(self, root):
        self.root = root
        self.root.title("Road Damage Detector")
        self.width = 764
        self.height = 520
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (self.width, self.height, (screenwidth -
                                                              self.width) / 2, (screenheight - self.height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)
        self.root.configure(bg='#E9EDC9')

        '''Logo Label Button'''
        logo_img = ImageTk.PhotoImage(Image.open('stop.jpg'))
        logo_label = tk.Label(self.root, image=logo_img)
        logo_label.image = logo_img
        logo_label.place(x=150, y=40, width=50, height=53)

        '''Welcome title'''
        welcomeTitle = tk.Label(self.root)
        # welcomeTitle["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=16)
        welcomeTitle["font"] = ft
        # welcomeTitle["fg"] = "#3656b7"
        welcomeTitle["bg"] = "#E9EDC9"
        welcomeTitle["justify"] = "center"
        welcomeTitle["text"] = "Road Damage Detector"
        welcomeTitle.place(x=280, y=40, width=200, height=58)

        '''BIT Logo Label Button'''
        bit_logo_img = ImageTk.PhotoImage(
            Image.open('BIT_logo.jpg'))
        bit_logo_label = tk.Label(self.root, image=bit_logo_img)
        bit_logo_label.image = bit_logo_img
        bit_logo_label.place(x=560, y=40, width=50, height=53)

        '''Another Instruction Label'''
        inst2_label = tk.Label(self.root)
        inst2_label["bg"] = "#E9EDC9"
        ft = tkFont.Font(family='Times', size=14)
        inst2_label["font"] = ft
        inst2_label["fg"] = "#333333"
        inst2_label["justify"] = "left"
        inst2_label["text"] = "Choose your processing method"
        inst2_label.place(x=250, y=150, width=270, height=45)

        '''Select Label'''
        select_label = tk.Label(self.root)
        select_label["bg"] = "#E9EDC9"
        ft = tkFont.Font(family='Times', size=14)
        select_label["font"] = ft
        select_label["fg"] = "#333333"
        select_label["justify"] = "left"
        select_label["text"] = "Select :"
        select_label.place(x=100, y=198, width=60, height=30)

        '''Test Button'''
        test_button = tk.Button(self.root)
        test_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        test_button["font"] = ft
        test_button["fg"] = "#000000"
        test_button["justify"] = "center"
        test_button["text"] = "Test"
        test_button.place(x=582, y=480, width=70, height=25)
        test_button["command"] = self.test_button_command

        '''Quit Button'''
        quit_button = tk.Button(self.root)
        quit_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        quit_button["font"] = ft
        quit_button["fg"] = "#000000"
        quit_button["justify"] = "center"
        quit_button["text"] = "Quit"
        quit_button.place(x=657, y=480, width=70, height=25)
        quit_button["command"] = self.quit_button_command

        '''Back Button'''
        back_button = tk.Button(self.root)
        back_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        back_button["font"] = ft
        back_button["fg"] = "#000000"
        back_button["justify"] = "center"
        back_button["text"] = "Back"
        back_button.place(x=505, y=480, width=70, height=25)
        back_button["command"] = self.back_button_command

        '''Check Box. 
        webcam1, 
        webcam2,
        Video, 
        Image'''

        self.webcam1_checked = tk.BooleanVar()
        self.webcam2_checked = tk.BooleanVar()
        self.video_checked = tk.BooleanVar()
        self.image_checked = tk.BooleanVar()

        webcam1_check = tk.Checkbutton(
            self.root, variable=self.webcam1_checked, command=self.on_checkbox_clicked)
        webcam1_check["bg"] = "#E9EDC9"
        ft = tkFont.Font(family='Times', size=12)
        webcam1_check["font"] = ft
        webcam1_check["fg"] = "#333333"
        webcam1_check["justify"] = "center"
        webcam1_check["text"] = "Webcam1"
        webcam1_check.place(x=200, y=200, width=85, height=25)
        webcam1_check["offvalue"] = "0"
        webcam1_check["onvalue"] = "1"
        webcam1_check["command"] = self.on_checkbox_clicked

        webcam2_check = tk.Checkbutton(
            self.root, variable=self.webcam2_checked, command=self.on_checkbox_clicked)
        webcam2_check["bg"] = "#E9EDC9"
        ft = tkFont.Font(family='Times', size=12)
        webcam2_check["font"] = ft
        webcam2_check["fg"] = "#333333"
        webcam2_check["justify"] = "center"
        webcam2_check["text"] = "Webcam2"
        webcam2_check.place(x=330, y=200, width=85, height=25)
        webcam2_check["offvalue"] = "0"
        webcam2_check["onvalue"] = "1"
        webcam2_check["command"] = self.on_checkbox_clicked

        video_check = tk.Checkbutton(
            self.root, variable=self.video_checked, command=self.on_checkbox_clicked)
        video_check["bg"] = "#E9EDC9"
        ft = tkFont.Font(family='Times', size=12)
        video_check["font"] = ft
        video_check["fg"] = "#333333"
        video_check["justify"] = "center"
        video_check["text"] = "Video"
        video_check.place(x=455, y=200, width=70, height=25)
        video_check["offvalue"] = "0"
        video_check["onvalue"] = "1"
        video_check["command"] = self.on_checkbox_clicked

        image_check = tk.Checkbutton(
            self.root, variable=self.image_checked, command=self.on_checkbox_clicked)
        image_check["bg"] = "#E9EDC9"
        ft = tkFont.Font(family='Times', size=12)
        image_check["font"] = ft
        image_check["fg"] = "#333333"
        image_check["justify"] = "center"
        image_check["text"] = "Image"
        image_check.place(x=575, y=200, width=70, height=25)
        image_check["offvalue"] = "0"
        image_check["onvalue"] = "1"
        image_check["command"] = self.on_checkbox_clicked

    def back_button_command(self):
        self.root.destroy()
        root1 = tk.Tk()
        app1 = Intro(root1)
        root1.mainloop()

    def test_button_command(self):
        resultLabel = tk.Label(self.root)
        resultLabel["anchor"] = "n"
        ft = tkFont.Font(family='Times', size=8)
        resultLabel["font"] = ft
        resultLabel["fg"] = "#333333"
        resultLabel["justify"] = "left"
        resultLabel.place(x=130, y=310, width=480, height=90)

        '''View Label'''
        view_Label = tk.Button(self.root)
        view_Label["anchor"] = "n"
        ft = tkFont.Font(family='Times', size=8)
        view_Label["font"] = ft
        view_Label["fg"] = "#333333"
        view_Label["justify"] = "left"
        view_Label['text'] = 'Result'
        view_Label.place(x=560, y=410, width=50, height=30)

        if self.webcam1_checked.get():
            path = str(0)
            output = test_model(path)
            a = output.strip('\\').split('\n')[-3:-2][0]
            resultLabel["text"] = a.replace("\\", '/')
            # resultLabel["text"] = output.strip('\\').split('\n')[-3:-2]
        elif self.webcam2_checked.get():
            path = str(1)
            output = test_model(path)
            a = output.strip('\\').split('\n')[-3:-2][0]
            resultLabel["text"] = a.replace("\\", '/')
            # resultLabel["text"] = output.strip('\\').split('\n')[-3:-2]
        else:
            path = self.file_path()
            output = test_model(path)
            # resultLabel["text"] = output.strip('\\').split('\n')[-3:-2]
            a = output.strip('\\').split('\n')[-3:-2][0]
            resultLabel["text"] = a.replace("\\", '/')

        if a.replace("\\", '/').strip('\r').split(':')[-1].split('.')[-1] == 'jpg':
            path = './{}'.format(a.replace("\\",
                                 '/').strip('\r').split(':')[-1].strip())
            view_Label['command'] = lambda: self.show_image(self.root, path)
        elif a.replace("\\", '/').strip('\r').split(':')[-1].split('.')[-1] == 'mp4':
            path = './{}'.format(a.replace("\\", '/').strip('\r').split(':')[-1].strip())
            view_Label['command'] = lambda: self.show_video( path)

    def show_image(self, root, path):
        top = Toplevel(root)
        image = Image.open(path)
        photo = ImageTk.PhotoImage(image)
        top.title('Image Preview')
        label = tk.Label(top, image=photo)
        label.image = photo
        label.pack()
        top.mainloop()

    def show_video(self, path):
        video = cv2.VideoCapture(path)

        frame_width = 720
        frame_height = 720

        cv2.namedWindow("{}".format(path.split("/")[-1]), cv2.WINDOW_NORMAL)
        cv2.resizeWindow("{}".format(path.split("/")[-1]), frame_width, frame_height)

        while True:
            # Read the current frame
            ret, frame = video.read()

            # Check if a frame was successfully read
            if not ret:
                break

            # Display the frame in a window named "Video"
            cv2.imshow("{}".format(path.split("/")[-1]), frame)

            # Exit the loop if the 'q' key is pressed
            if cv2.waitKey(1) == ord('q'):
                break

        # Release the video object and close the window
        video.release()
        cv2.destroyAllWindows()

    # def show_video(self, root, path):
    #     top = Toplevel((root))

    #     top.title('Video Preview')

    #     video = cv2.VideoCapture(path)

    #     ret, frame = video.read()

    #     label = tk.Label(top)
    #     label.pack()

    #     def update_frame():
    #         nonlocal frame

    #         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #         image = Image.fromarray(frame_rgb)
    #         photo = ImageTk.PhotoImage((image))

    #         label.configure(image=photo)
    #         label.image = photo

    #         ret, frame = video.read()

    #         if ret:
    #             label.after(1, update_frame)
    #         else:
    #             video.release()
    #     update_frame()
    #     top.mainloop()


    def quit_button_command(self):
        self.root.destroy()

    def file_browse(self, condition):
        if condition:
            # save the reference to the widget as an instance attribute
            self.browseLabel = tk.Label(self.root)
            ft = tkFont.Font(family='Times', size=10)
            self.browseLabel["font"] = ft
            self.browseLabel["fg"] = "#ae9696"
            self.browseLabel["justify"] = "center"
            self.browseLabel["text"] = "Select your file"
            self.browseLabel.place(x=130, y=260, width=480, height=30)

            # save the reference to the widget as an instance attribute
            self.browseButton = tk.Button(self.root)
            self.browseButton["bg"] = "#f0f0f0"
            ft = tkFont.Font(family='Times', size=10)
            self.browseButton["font"] = ft
            self.browseButton["fg"] = "#000000"
            self.browseButton["justify"] = "center"
            self.browseButton["text"] = "Browse"
            self.browseButton.place(x=620, y=260, width=52, height=30)
        else:
            # check if the widget has been created before attempting to destroy it
            if hasattr(self, 'browseLabel'):
                self.browseLabel.destroy()
                del self.browseLabel  # remove the instance attribute reference
            if hasattr(self, 'browseButton'):
                self.browseButton.destroy()
                del self.browseButton

    def on_checkbox_clicked(self):
        if self.webcam1_checked.get():
            self.webcam2_checked.set(False)
            self.video_checked.set(False)
            self.image_checked.set(False)
            self.file_browse(False)

        elif self.webcam2_checked.get():
            self.webcam1_checked.set(False)
            self.video_checked.set(False)
            self.image_checked.set(False)
            self.file_browse(False)

        elif self.video_checked.get():
            self.webcam1_checked.set(False)
            self.webcam2_checked.set(False)
            self.image_checked.set(False)
            self.file_browse(self.video_checked.get())
            self.browseButton["command"] = self.browseButton_command_video

        elif self.image_checked.get():
            self.webcam1_checked.set(False)
            self.webcam2_checked.set(False)
            self.video_checked.set(False)
            self.file_browse(self.image_checked.get())
            self.browseButton["command"] = self.browseButton_command_photo
        else:
            self.file_browse(False)

        if not self.webcam1_checked.get() and not self.webcam2_checked.get() and not self.video_checked.get() and not self.image_checked.get():
            self.file_browse(False)

    def browseButton_command_video(self):
        # For all file type use ("all files", "*.*") in the filetypes tuple
        self.filepath = filedialog.askopenfilename(
            title="Open file", filetypes=(("video files", "*.mp4"), ("all files", "*.*")))

        if self.filepath != "":
            self.browseLabel.config(text=self.filepath)

    def browseButton_command_photo(self):
        # For all file type use ("all files", "*.*") in the filetypes tuple
        self.filepath = filedialog.askopenfilename(
            title="Open file", filetypes=(("Image files", "*.jpg"), ("all files", "*.*")))

        if self.filepath != "":
            self.browseLabel.config(text=self.filepath)

    def file_path(self):
        return self.filepath


if __name__ == "__main__":
    root1 = tk.Tk()
    app1 = Intro(root1)
    root1.mainloop()
