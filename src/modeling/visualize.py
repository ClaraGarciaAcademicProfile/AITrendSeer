import matplotlib.pyplot as plt
import os

#visualize
def save_plot(fig, dataset_name, plot_name):
    os.makedirs(f"visualizations/{dataset_name}", exist_ok=True)
    fig.savefig(f"visualizations/{dataset_name}/{plot_name}.png")
    plt.close()
    print(f"Plot saved to visualizations/{dataset_name}/{plot_name}.png")