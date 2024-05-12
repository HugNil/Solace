import numpy as np
from matplotlib.figure import Figure
# from matplotlib.backends.backend_agg import FigureCanvasAgg
# from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Graph:
    def __init__(self, master, props):
        self.master = master
        self.props = props
        self.fig = Figure(figsize=(7, 5), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.widget = self.canvas.get_tk_widget()
        self.fig.subplots_adjust(bottom=0.2)
        self.show_graph()

    def show_graph(self):
        # Ställ in bakgrundsfärger och basinställningar för grafen
        fg_color = self.props.BACKGROUND_LIGHT
        self.ax.clear()
        self.ax.set_xlabel("Day", color=fg_color, fontsize=20)
        self.ax.set_ylabel("Level", color=fg_color, fontsize=20)
        self.ax.set_xticks(range(8))
        self.ax.set_xticklabels(
            ['', '1', '2', '3', '4', '5', '6', '7'],
            color=fg_color,
            fontsize=18)
        self.ax.set_yticks(range(1, 11))
        self.ax.set_yticklabels(
            ['', '2', '', '4', '', '6', '', '8', '', '10'],
            color=fg_color,
            fontsize=18)
        self.ax.tick_params(axis='both', which='major', labelsize=18)
        self.ax.spines['top'].set_color(fg_color)
        self.ax.spines['right'].set_color(fg_color)
        self.ax.spines['bottom'].set_color(fg_color)
        self.ax.spines['left'].set_color(fg_color)
        self.fig.patch.set_facecolor(self.props.BACKGROUND_DARK)
        self.ax.set_facecolor(self.props.BACKGROUND_DARK)
        self.ax.xaxis.label.set_position((0.5, -0.1))
        self.canvas.draw()
        self.display()

    def plot_data(self, mood_y, stress_y):
        x = np.array(list(range(1, len(mood_y) + 1)))

        mood_y = np.array([y if y is not None else np.nan for y in mood_y])
        stress_y = np.array([y if y is not None else np.nan for y in stress_y])

        valid_mood = ~np.isnan(mood_y)
        valid_stress = ~np.isnan(stress_y)

        self.ax.clear()
        self.show_graph()

        self.ax.plot(
            x[valid_mood],
            mood_y[valid_mood],
            label='Mood',
            color='darkorange',
            linewidth=3)
        self.ax.plot(
            x[valid_stress],
            stress_y[valid_stress],
            label='Stress',
            color='lightgreen',
            linewidth=3)

        self.ax.legend(
            loc='upper left',
            fontsize=18,
            facecolor=self.props.BACKGROUND_DARK,
            edgecolor=self.props.BACKGROUND_LIGHT,
            labelcolor='white'
            )

        self.canvas.draw()

    def display(self):
        self.widget.place(relx=0.5, rely=0.48, anchor='center')