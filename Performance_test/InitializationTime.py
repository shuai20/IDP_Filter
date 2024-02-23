import csv
import time
import matplotlib.pyplot as plt

def load_csv(filepath):
    start_time = time.perf_counter()
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        words = [row[0].strip() for row in reader if row]
    end_time = time.perf_counter()
    return words, end_time - start_time

def plot_loading_times(filepaths):
    total_words_count = 0
    total_loading_time = 0
    cumulative_word_counts = []
    cumulative_loading_times = []

    for filepath in filepaths:
        words, duration = load_csv(filepath)
        total_words_count += len(words)
        total_loading_time += duration
        cumulative_word_counts.append(total_words_count)
        cumulative_loading_times.append(total_loading_time)
        print(f"File: {filepath}, Total Words: {total_words_count}, Total Time: {total_loading_time}")

    plt.plot(cumulative_word_counts, cumulative_loading_times,  color='black',  marker='o')
    plt.xlabel('Cumulative Number of Blacklist Words')
    plt.ylabel('Cumulative Initialization Time (seconds)')
    plt.title('Cumulative Initialization Time vs Cumulative IDPWord Count')



    plt.show()




# dont forget to change the filepath
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
plot_loading_times(filepaths)
