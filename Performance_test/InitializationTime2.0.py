import csv
import time
import matplotlib.pyplot as plt
import numpy as np
#from IDP_filter import IDPFilter
from IDPFilter_Flashtext_initial import IDPFilter

def load_csv(filepath):
    """Function to load words from a CSV file."""
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        return [row[0].strip() for row in reader if row]

def test_loading_times(filepaths, idp_filter):
    """Function to test loading times of ORB words into IDPFilter."""
    cumulative_loading_times = []
    cumulative_duration = 0

    for filepath in filepaths:
        words = load_csv(filepath)
        start_time = time.time()
        # Simulate filtering text which will load words into ORB
        filtered_text, _ = idp_filter.filter_text(
            input_text="",
            user_orb=",".join(words),
            user_srw="",
            global_srb="",
         #   categories=["number", "link"]
            categories=""

        )
        end_time = time.time()
        cumulative_duration += (end_time - start_time)
        cumulative_loading_times.append(cumulative_duration)
        print(cumulative_loading_times)

    return cumulative_loading_times

def plot_loading_times(cumulative_loading_times):
    """Function to plot loading times."""
    x_axis = np.arange(10000, 110000, 10000)
    plt.plot(x_axis, cumulative_loading_times, color='black', marker='o')
    plt.xlabel('Number of Blacklist words', fontsize=12)
    plt.ylabel('Initialization time (seconds)', fontsize=12)
    plt.title('Initialization Time vs Blacklist Words')
    plt.grid(False)
    plt.xticks(x_axis)  # Adjusting the x-ticks for 10 intervals
    plt.yticks(np.arange(0, max(cumulative_loading_times) + 0.1, 0.05))
    plt.show()

# Instantiate the IDPFilter
idp_filter = IDPFilter()

# Filepaths to the CSV files - replace with the actual file paths
filepaths = [
    'IDPwords1.csv',
    'IDPwords2.csv',
    'IDPwords3.csv',
    'IDPwords4.csv',
    'IDPwords5.csv',
    'IDPwords6.csv',
    'IDPwords7.csv',
    'IDPwords8.csv',
    'IDPwords9.csv',
    'IDPwords10.csv'

]

# Run the loading time test and plot the results
cumulative_times = test_loading_times(filepaths, idp_filter)
plot_loading_times(cumulative_times)


# Filepaths to your CSV files






