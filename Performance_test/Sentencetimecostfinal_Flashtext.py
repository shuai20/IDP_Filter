import matplotlib.pyplot as plt
from IDPFilter_Flashtext_initial import IDPFilter
import time

def read_sentences_from_file(filepath):
    """Read sentences from a given file."""
    with open(filepath, 'r') as file:
        sentences = file.readlines()
    return [sentence.strip() for sentence in sentences]

def write_filtered_sentences_to_file(filepath, filtered_sentences, word_counts):
    """Write filtered sentences and their word counts to a file."""
    with open(filepath, 'w') as file:
        for sentence, count in zip(filtered_sentences, word_counts):
            file.write(f"{sentence} (FlshTextFiltered Words: {count})\n")


def filter_sentences_and_measure_individual_times(idp_filter, sentences, categories):
    times_per_sentence = []
    filtered_sentences = []
    word_counts = []
    cumulative_time = 0

    for sentence in sentences:
        start_time = time.time()
        filtered_sentence, count = idp_filter.filter_text(sentence, categories)
        end_time = time.time()

        time_taken = end_time - start_time
        cumulative_time += time_taken
        times_per_sentence.append(cumulative_time)
        filtered_sentences.append(filtered_sentence)
        word_counts.append(count)
    print(cumulative_time)

    return filtered_sentences, word_counts, times_per_sentence

def plot_cumulative_times(times_per_sentence_100, times_per_sentence_200, times_per_sentence_400, xlabel, ylabel, title, xlabel_fontsize=14, ylabel_fontsize=14):
    """Plot cumulative times for three categories on the same axes."""
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(times_per_sentence_100) + 1), times_per_sentence_100,  color='black', marker='o', label='Blacklist Words: 100')
    plt.plot(range(1, len(times_per_sentence_200) + 1), times_per_sentence_200,  color='gray', marker='o', label='Blacklist Words: 200')
    plt.plot(range(1, len(times_per_sentence_400) + 1), times_per_sentence_400,  color='darkgray', marker='o', label='Blacklist Words: 400')
    plt.xlabel(xlabel, fontsize=xlabel_fontsize)
    plt.ylabel(ylabel, fontsize=ylabel_fontsize)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    # Set the limits for x and y axes to start from 0
    plt.xlim(0, max(len(times_per_sentence_100), len(times_per_sentence_200), len(times_per_sentence_400)))
    plt.ylim(0, max(max(times_per_sentence_100), max(times_per_sentence_200), max(times_per_sentence_400)))
    plt.tight_layout()
    plt.show()

def main():
    """Main function to read sentences, filter them, and plot the cumulative times."""
    idp_filter = IDPFilter()

    input_filepath = "sentences_1.txt"
    output_filepath = "plot_filtered_sentences_Flashtext.txt"
    sentences = read_sentences_from_file(input_filepath)

    # Filter sentences for each category and measure times
    filtered_sentences, word_counts, times_per_sentence_100 = filter_sentences_and_measure_individual_times(idp_filter, sentences, ["name100"])

    _, _, times_per_sentence_200 = filter_sentences_and_measure_individual_times(idp_filter, sentences, ["name200"])
    _, _, times_per_sentence_400 = filter_sentences_and_measure_individual_times(idp_filter, sentences, ["name400"])

    # Plot the cumulative times for different blacklist sizes
    plot_cumulative_times(times_per_sentence_100, times_per_sentence_200, times_per_sentence_400,
                          'Number of Sentences', 'Cumulative Filtering Time (seconds)',
                          'Cumulative Filtering Time for Different Sizes of Blacklists(FlashText)', xlabel_fontsize=12,
                          ylabel_fontsize=12)

    # Write filtered sentences to file
    write_filtered_sentences_to_file(output_filepath, filtered_sentences, word_counts)

if __name__ == "__main__":
    main()