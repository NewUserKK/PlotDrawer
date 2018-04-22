"""
plot_drawer.py: Module for drawing 2D plots with given coordinates
"""

import matplotlib.pyplot as plt


def draw_plot(x_set: list, y_set: list, filename=None,
              title=None, xlabel=None, ylabel=None, legend=None,
              min_x=None, max_x=None, min_y=None, max_y=None,
              grid=True) -> None:
    """
    Draws a plot from a given lists of x and y points

    :param x_set: list of x coordinates
    :param y_set: lsit of y coordinates
    :param filename: name of file used for output. Opens a window with plot if not specified
    :param title: title of plot displayed on top of it
    :param xlabel: name for x axis
    :param ylabel: name for y axis
    :param legend: name of line
    :param min_x: minimum x value displayed. Minimum of x_set by default
    :param max_x: maximum x value displayed. Maximum of y_set by default
    :param min_y: minimum y value displayed. Minimum of x_set by default
    :param max_y: maximum y value displayed. Maximum of y_set by default
    :param grid: toggles grid drawing
    """
    # TODO: support of multiple coordinate sets
    # f = (lambda *x: list(x))(x_set)
    # print(f)

    # TODO: handle properly
    assert len(x_set) == len(y_set)
    line = plt.plot(x_set, y_set)

    # Max and min values for axis
    if not min_x:
        min_x = min(x_set)
    if not max_x:
        max_x = max(x_set)
    if not min_y:
        min_y = min(y_set)
    if not max_y:
        max_y = max(y_set)
    plt.axis([min_x, max_x, min_y, max_y])

    # Title of a plot
    if title:
        plt.title(title)

    # Set X and Y labels
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)

    # Legend - description for a line on plot
    if legend:
        plt.legend(line, legend, loc='best')

    # Toggles grid painting
    if grid:
        plt.grid()

    if filename:
        try:
            plt.savefig(filename)
        except ValueError:
            print("Unsupported output format! Supported formats: eps, pdf, pgf, png, ps, raw, rgba, svg, svgz")
    else:
        plt.show()


def get_xs(min_value, max_value, precision=1.0) -> list:
    """
    Return list of x values from min to max with a given precision

    :param min_value: minimum value in range
    :param max_value: maximum value in range
    :param precision: precision for calculation, must be power of 10.
                      Less value means more accurate calculation
    :return: list contains x coordinates
    """
    multiplier = int(precision ** (-1))
    return [x / multiplier for x in range(int(min_value * multiplier), int(max_value * multiplier) + multiplier)]


def get_ys(x_set: list, func) -> list:
    """
    Return list of y values calculated by provided function

    :param x_set: list of x coordinate values
    :param func: function used to calculate y
    :return: list contains y coordinates
    """
    return [func(x) for x in x_set]


if __name__ == "__main__":

    def f(x):
        return 6 * (1 - (x / -1.5)) ** 2

    xs = get_xs(-1.8, 0, 0.01)
    ys = get_ys(xs, f)

    draw_plot(xs, ys, filename=None,
              title="Title", xlabel="x", ylabel="y", legend="line")
