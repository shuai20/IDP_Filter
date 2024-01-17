# from IDP_filter import IDPFilter
# import time
# import matplotlib.pyplot as plt
#
# def read_sentences_from_file(filepath):
#     with open(filepath, 'r') as file:
#         sentences = file.readlines()
#     return [sentence.strip() for sentence in sentences]
#
# def write_filtered_sentences_to_file(filepath, filtered_sentences, word_counts):
#     with open(filepath, 'w') as file:
#         for sentence, count in zip(filtered_sentences, word_counts):
#             file.write(f"{sentence} (Filtered Words: {count})\n")
#
# def filter_sentences_and_measure_time(idp_filter, sentences):
#     start_time = time.time()
#     filtered_sentences = []
#     word_counts = []
#     for sentence in sentences:
#         filtered_sentence, count = idp_filter.filter_text(sentence, "", "", "", ['country'])
#         filtered_sentences.append(filtered_sentence)
#         word_counts.append(count)
#     end_time = time.time()
#     return filtered_sentences, word_counts, end_time - start_time
#
# def main():
#     idp_filter = IDPFilter()
#     file_times = []
#
#     for i in range(1, 11):
#         input_filepath = f"sentences_{i}.txt"
#
#
#         output_filepath = f"filtered_sentences_{i}.txt"
#         sentences = read_sentences_from_file(input_filepath)
#
#         filtered_sentences, word_counts, duration = filter_sentences_and_measure_time(idp_filter, sentences)
#         write_filtered_sentences_to_file(output_filepath, filtered_sentences, word_counts)
#
#         file_times.append(duration)
#         print(f"File {i}: Filtering Time = {duration} seconds")
#
#         # Plotting the results
#     plt.plot(range(1, 11), file_times, marker='o')
#     plt.xlabel('File Number')
#     plt.ylabel('Filtering Time (seconds)')
#     plt.title('Filtering Time for Each File')
#     plt.xticks(range(1, 11))
#     plt.show()
#
#
# if __name__ == "__main__":
#     main()
# Let's modify the script to plot the cumulative time taken for filtering each sentence in each file.
# We will plot a separate graph for each file.

# from IDP_filter import IDPFilter
# import matplotlib.pyplot as plt
# import time
#
#
# def read_sentences_from_file(filepath):
#     with open(filepath, 'r') as file:
#         sentences = file.readlines()
#     return [sentence.strip() for sentence in sentences]
#
#
# def write_filtered_sentences_to_file(filepath, filtered_sentences, word_counts):
#     with open(filepath, 'w') as file:
#         for sentence, count in zip(filtered_sentences, word_counts):
#             file.write(f"{sentence} (Filtered Words: {count})\n")
#
#
# def filter_sentences_and_measure_time(idp_filter, sentences):
#     cumulative_times = []
#     cumulative_duration = 0
#     filtered_sentences = []
#     word_counts = []
#
#     for sentence in sentences:
#         start_time = time.time()
#         filtered_sentence, count = idp_filter.filter_text(sentence, "", "", "", [])
#         end_time = time.time()
#
#         cumulative_duration += (end_time - start_time)
#         cumulative_times.append(cumulative_duration)
#         filtered_sentences.append(filtered_sentence)
#         word_counts.append(count)
#
#     return filtered_sentences, word_counts, cumulative_times
#
#
# def plot_cumulative_times(cumulative_times, file_number):
#     plt.plot(range(1, len(cumulative_times) + 1), cumulative_times, marker='o')
#     plt.xlabel('Number of Sentences')
#     plt.ylabel('Cumulative Filtering Time (seconds)')
#     plt.title(f'File {file_number}: Cumulative Filtering Time vs Number of Sentences')
#     plt.show()
#
#
# def main():
#     idp_filter = IDPFilter()
#
#     for i in range(1, 11):
#         input_filepath = f"sentences_{i}.txt"
#         output_filepath = f"filtered_sentences_{i}.txt"
#         sentences = read_sentences_from_file(input_filepath)
#
#         filtered_sentences, word_counts, cumulative_times = filter_sentences_and_measure_time(idp_filter, sentences)
#         write_filtered_sentences_to_file(output_filepath, filtered_sentences, word_counts)
#         plot_cumulative_times(cumulative_times, i)
#
#
# if __name__ == "__main__":
#     main()

import matplotlib.pyplot as plt
from IDP_filter import IDPFilter
import time


def read_sentences_from_file(filepath):
    with open(filepath, 'r') as file:
        sentences = file.readlines()
    return [sentence.strip() for sentence in sentences]

def write_filtered_sentences_to_file(filepath, filtered_sentences, word_counts):
    with open(filepath, 'w') as file:
        for sentence, count in zip(filtered_sentences, word_counts):
            file.write(f"{sentence} (Filtered Words: {count})\n")


def filter_sentences_and_measure_individual_times(idp_filter, sentences):
    times_per_sentence = []
    filtered_sentences = []
    word_counts = []
    cumulative_time = 0

    for sentence in sentences:
        start_time = time.time()
        filtered_sentence, count = idp_filter.filter_text(sentence, "", "", "", ['name'])
        end_time = time.time()

        time_taken = end_time - start_time
        cumulative_time += time_taken
        times_per_sentence.append(cumulative_time)
        filtered_sentences.append(filtered_sentence)
        word_counts.append(count)

    return filtered_sentences, word_counts, times_per_sentence


def plot_cumulative_times(times_per_sentence, file_number):
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(times_per_sentence) + 1), times_per_sentence, marker='o')
    plt.xlabel('Number of Sentences')
    plt.ylabel('Cumulative Filtering Time (seconds)')
    plt.title(f'Cumulative Filtering Time for File {file_number}')
    plt.grid(False)
    plt.xticks(range(0, len(times_per_sentence) + 1, 1000))
    plt.tight_layout()
    plt.show()


def main():
    idp_filter = IDPFilter()

    for i in range(1, 11):
        input_filepath = f"sentences_{i}.txt"
        output_filepath = f"2.0filtered_sentences_{i}.txt"
        sentences = read_sentences_from_file(input_filepath)

        filtered_sentences, word_counts, times_per_sentence = filter_sentences_and_measure_individual_times(idp_filter, sentences)
        write_filtered_sentences_to_file(output_filepath, filtered_sentences, word_counts)
        plot_cumulative_times(times_per_sentence, i)


if __name__ == "__main__":
    main()


