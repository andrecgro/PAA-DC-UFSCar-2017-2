import tkinter as tk

import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import matplotlib.pyplot as plt

import maxflow


# Interface class
class ApplicationInterface(tk.Frame):
    # Class constructor
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('Max Flow Problem Solver')

        self.counterStep = 0
        self.stepQnty = 0
        self.maxFlow = 0

        # Widget background area
        self.background = tk.Frame(master, bg="#525659", padx="15p")
        self.background.pack(side="bottom", fill="both", expand="true")
        self.background.master.geometry("700x550")

        self.figure = Figure(figsize=(7, 4), dpi=100, tight_layout=True)
        self.axes = self.figure.add_subplot(111)
        self.axes.set_axis_off()

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
        self.mxl.configure(
            bg='#525659',
            font="Helvetica 42 bold",
            fg="#fff",
            justify="center")
        self.mxl.pack()

    # Draw application's image example
    def drawImageExample(self):
        self.imageFrame = tk.Frame(
            self.background, bg="#525659", width="330", height="450")
        self.imageFrame.pack(side="top", fill="x")
        # Application's Label
        self.eximg = tk.PhotoImage(file="maxflow.gif")
        self.img = tk.Label(self.imageFrame, image=self.eximg)
        self.img.configure(bg='#525659', justify="center")
        self.img.pack()

    # Draw application's menu
    def drawMenu(self):
        self.menu = tk.Frame(self.background, bg="#525659", width="600")
        self.menu.pack(side="top", fill="x", padx="100p", pady="20p")

        # Menu Buttons
        self.ff = tk.Button(
            self.menu,
            text="Ford Fulkerson",
            font="Helvetica 18 bold",
            highlightbackground='#525659',
            width=18,
            height=5,
            cursor="hand2",
            command=lambda: self.drawMethodScreen(1))
        self.ff.pack(side="left", fill="both")

        self.fb = tk.Button(
            self.menu,
            text="Brute Force",
            font="Helvetica 18 bold",
            highlightbackground='#525659',
            width=18,
            height=5,
            cursor="hand2",
            command=lambda: self.drawMethodScreen(0))
        self.fb.pack(side="right", fill="both")

    # Draw method's screen
    def drawMethodScreen(self, type):
        # Cleaning background frame
        for widget in self.background.winfo_children():
            widget.destroy()
        # Drawing the go back button
        self.drawGoBack()
        # Method's Label
        self.mtdLabelFrame = tk.Frame(
            self.background, bg="#525659", width="600")
        self.mtdLabelFrame.pack(side="top", fill="x")
        if type:
            self.mtdLabel = tk.Label(
                self.mtdLabelFrame, text="Ford Fulkerson Approach")
        else:
            self.mtdLabel = tk.Label(
                self.mtdLabelFrame, text="Brute Force Approach")

        self.mtdLabel.configure(
            bg='#525659', font="Helvetica 24 bold", fg="#fff")
        self.mtdLabel.pack()
        # Drawing the canvas frame to plot the graph
        #self.canvasFrame = tk.Frame(
        #self.background, bg='white', width="450", height="350")
        #self.canvasFrame.pack(side="top", fill="x")

        self.canvasFrame = tk.Frame(self.background, bg='white')
        self.canvasFrame.pack()

        self.plt_canvas = FigureCanvasTkAgg(self.figure, self.canvasFrame)
        self.plt_canvas.show()
        self.plt_canvas.get_tk_widget().pack(side='bottom', expand=True)

        # Drawing the method's menu
        self.methodMenuFrame = tk.Frame(
            self.background, bg='#525659', width="300", pady="10p")
        self.methodMenuFrame.pack(side='top')

        self.resetButton = tk.Button(
            self.methodMenuFrame,
            highlightbackground='#525659',
            text="Reset",
            font="Helvetica 18 bold",
            command=self.drawGraph)
        self.resetButton.pack(side="left")

        self.stepButton = tk.Button(
            self.methodMenuFrame,
            highlightbackground='#525659',
            text="Run",
            font="Helvetica 18 bold")
        self.stepButton.pack(side="left")

        self.stepCounter = tk.Label(
            self.methodMenuFrame,
            text="Steps: " + str(self.counterStep) + "/" + str(self.stepQnty),
            font="Helvetica 18 bold",
            foreground="#fff",
            background="#525659")
        self.stepCounter.pack(side="left")

        self.maxFlowCounter = tk.Label(
            self.methodMenuFrame,
            text="Max Flow: " + str(self.maxFlow),
            font="Helvetica 18 bold",
            foreground="#fff",
            background="#525659")
        self.maxFlowCounter.pack(side="left")

    # Testing Function
    def incrementStep(self):
        self.counterStep += 1
        self.stepCounter.config(
            text="Steps: " + str(self.counterStep) + "/" + str(self.stepQnty))

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

    def drawGraph(self):
        self.axes.cla()
        self.axes.set_axis_off()

        G = nx.DiGraph()
        G.add_weighted_edges_from(
            [['a', 'b', 3.0],
            ['b', 'c', 5.0],
            ['c', 'd', 1.0],
            ['d', 'e', 2.0],
            ['a', 'd', 1.5],
            ['e', 'f', 3.0],
            ['e', 'c', 2.0]]
        )
    
        pos = nx.spring_layout(G)
        weight_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx(G, pos, ax=self.axes, with_labels=True)
        nx.draw_networkx_edge_labels(
            G, pos, ax=self.axes, edge_labels=weight_labels)
        self.plt_canvas.show()