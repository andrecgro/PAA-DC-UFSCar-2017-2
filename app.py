import tkinter as tk


# Interface class
class ApplicationInterface(tk.Frame):
    # Class constructor
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('Max Flow Problem Solver')

        # Widget background area
        self.background = tk.Frame(master, bg="#525659")
        self.background.pack(side="bottom", fill="both", expand="true")
        self.background.master.geometry("600x450")

        self.drawInitialScreen()

    # Draw application's initial screen
    def drawInitialScreen(self):
        # Cleaning background frame
        for widget in self.background.winfo_children():
            widget.destroy()

        self.drawLabel()
        self.drawImageExample()
        self.drawMenu()

    # Draw application's label
    def drawLabel(self):
        self.labelFrame = tk.Frame(self.background, bg="#525659", width="600")
        self.labelFrame.pack(side="top", fill="x")
        # Application's Label
        self.mxl = tk.Label(self.labelFrame, text="Max Flow Problem")
        self.mxl.configure(bg='#525659', font="Helvetica 42 bold", fg="#fff", justify="center")
        self.mxl.pack()

    # Draw application's image example
    def drawImageExample(self):
        self.imageFrame = tk.Frame(
            self.background, bg="#525659", width="330", height="300")
        self.imageFrame.pack(side="top", fill="x")
        # Application's Label
        self.eximg = tk.PhotoImage(file="maxflow.gif")
        self.img = tk.Label(self.imageFrame, image=self.eximg)
        self.img.configure(bg='#525659', justify="center")
        self.img.pack()

    # Draw application's menu
    def drawMenu(self):
        self.menu = tk.Frame(self.background, bg="#525659", width="600")
        self.menu.pack(side="top",fill="x", padx="100p", pady="20p")

        # Menu Buttons
        self.ff = tk.Button(
            self.menu,
            text="Ford Fulkerson",
            font="Helvetica 18 bold",
            highlightbackground='#525659',
            width=18,
            height=5,
            cursor="hand2",
            command=self.drawMethodScreen
        )
        self.ff.pack(side="left", fill="both")

        self.fb = tk.Button(
            self.menu,
            text="Força Bruta",
            font="Helvetica 18 bold",
            highlightbackground='#525659',
            width=18,
            height=5,
            cursor="hand2",
            command=self.drawMethodScreen)
        self.fb.pack(side="right", fill="both")

    # Draw method's screen
    def drawMethodScreen(self):
        # Cleaning background frame
        for widget in self.background.winfo_children():
            widget.destroy()

        self.drawGoBack()
    
    # Drawing a button to go back to initial screen
    def drawGoBack(self):
        self.backBtnImg = tk.PhotoImage(file="reply.gif")

        self.backBtnFrame = tk.Frame(
            self.background, bg="#525659", width="600")
        self.backBtnFrame.pack(side="top", fill="x")
        # Creating the button itself
        self.backBtn = tk.Label(
            self.backBtnFrame,
            bg='#525659',
            width=32,
            height=32,
            image=self.backBtnImg,
            cursor="hand2")
        self.backBtn.pack(side="left", fill="none")
        self.backBtn.bind("<Button-1>", lambda e: self.drawInitialScreen())