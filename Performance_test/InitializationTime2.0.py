import csv
import time
import matplotlib.pyplot as plt
from IDP_filter import IDPFilter

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
            categories=["number", "link"]
        )
        end_time = time.time()
        cumulative_duration += (end_time - start_time)
        cumulative_loading_times.append(cumulative_duration)

    return cumulative_loading_times

def plot_loading_times(cumulative_loading_times):
    """Function to plot loading times."""
    plt.plot(range(1, len(cumulative_loading_times) + 1), cumulative_loading_times, marker='o')
    plt.xlabel('Number of Documents')
    plt.ylabel('Cumulative Loading Time into IDPFilter ORB (seconds)')
    plt.title('Cumulative Loading Time vs Document Number')
    plt.grid(False)
    plt.xticks(range(1, len(cumulative_loading_times) + 1))
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






