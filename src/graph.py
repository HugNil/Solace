# import numpy as np
from matplotlib.figure import Figure
# from matplotlib.backends.backend_agg import FigureCanvasAgg
# from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Graph:
    def __init__(self, master, props):
        self.master = master
        self.props = props
        self.fig = Figure(figsize=(7, 6), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.widget = self.canvas.get_tk_widget()

    def plot_data(self, x, y):
        y = [None] + y
        x = range(len(y))
        fg_color = self.props.BACKGROUND_LIGHT

        self.ax.clear()
        self.ax.plot(x, y, color=fg_color, linewidth=2)
        self.ax.set_title(
            "Stress och Humöranalys", color=fg_color, fontsize=20)
        self.ax.set_xlabel("", color=fg_color, fontsize=20)
        self.ax.set_ylabel("Level", color=fg_color, fontsize=20)
        self.ax.set_xticks(x)
        self.ax.set_xticklabels(
            ['', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            color=fg_color,
            fontsize=18)
        self.ax.set_yticks(range(1, 11))
        self.ax.set_yticklabels(
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
            color=fg_color,
            fontsize=18)

        self.ax.tick_params(axis='both', which='major', labelsize=18)
        self.ax.spines['top'].set_color(fg_color)
        self.ax.spines['right'].set_color(fg_color)
        self.ax.spines['bottom'].set_color(fg_color)
        self.ax.spines['left'].set_color(fg_color)
        self.fig.patch.set_facecolor('#014F86')
        self.ax.set_facecolor(self.props.BACKGROUND_DARK)
        self.canvas.draw()

    def display(self):
        self.widget.pack(
            side="top",
            fill="both",
            expand=True,
            pady=(20, 0))
