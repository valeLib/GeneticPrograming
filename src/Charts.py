from matplotlib import pyplot as plt

def lineChart(xdata, ydata, xlabel, ylabel, title):
    plt.plot(xdata, ydata)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
