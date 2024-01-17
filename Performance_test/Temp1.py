from IDP_filter import IDPFilter
import time
import matplotlib.pyplot as plt

def read_sentences_from_file(filepath):
    with open(filepath, 'r') as file:
        sentences = file.readlines()
    return [sentence.strip() for sentence in sentences]

def write_filtered_sentences_to_file(filepath, filtered_sentences, word_counts):
    with open(filepath, 'w') as file:
        for sentence, count in zip(filtered_sentences, word_counts):
            file.write(f"{sentence} (Filtered Words: {count})\n")

def filter_sentences_and_measure_time(idp_filter, sentences):
    start_time = time.time()
    filtered_sentences = []
    word_counts = []
    for sentence in sentences:
        filtered_sentence, count = idp_filter.filter_text(sentence, "", "", "", ['country'])
        filtered_sentences.append(filtered_sentence)
        word_counts.append(count)
    end_time = time.time()
    return filtered_sentences, word_counts, end_time - start_time

def main():
    idp_filter = IDPFilter()
    file_times = []

    for i in range(1, 11):
        input_filepath = f"sentences_{i}.txt"


        output_filepath = f"filtered_sentences_{i}.txt"
        sentences = read_sentences_from_file(input_filepath)

        filtered_sentences, word_counts, duration = filter_sentences_and_measure_time(idp_filter, sentences)
        write_filtered_sentences_to_file(output_filepath, filtered_sentences, word_counts)

        file_times.append(duration)
        print(f"File {i}: Filtering Time = {duration} seconds")

        # Plotting the results
    plt.plot(range(1, 11), file_times, marker='o')
    plt.xlabel('File Number')
    plt.ylabel('Filtering Time (seconds)')
    plt.title('Filtering Time for Each File')
    plt.xticks(range(1, 11))
    plt.show()


if __name__ == "__main__":
    main()
