import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Graph:
    """
    This class represents a graphical component that
    displays a mood and stress graph
    using Matplotlib integrated with Tkinter.
    """
    def __init__(self, master, props):
        """
        Initializes the Graph object.

        Parameters:
        master (tkinter widget): The parent widget.
        props (object): An object containing various properties
        like screen dimensions and colors.
        """
        self.master = master
        self.props = props
        dpi = self.get_dpi()
        self.fig = Figure(figsize=(7, 5), dpi=dpi)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.widget = self.canvas.get_tk_widget()
        self.fig.subplots_adjust(bottom=0.2)
        self.show_graph()

    def get_dpi(self):
        """
        Determines the dots per inch (DPI) for the
        graph based on screen width.

        Returns:
        int: DPI value.
        """
        if self.props.screen_width >= 1700:
            return 100
        else:
            return 50

    def show_graph(self):
        """
        Configures the initial appearance and settings for the graph,
        including axis labels, ticks, and background colors.
        """
        # Set background colors and base settings for the graph
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
        """
        Plots the mood and stress data on the graph.

        Parameters:
        mood_y (list): List of mood values for the past 7 days.
        stress_y (list): List of stress values for the past 7 days.
        """
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
        self.logger.log('Graph updated')

    def display(self):
        """
        Places the graph widget within the parent widget.
        """
        self.widget.place(relx=0.5, rely=0.48, anchor='center')
