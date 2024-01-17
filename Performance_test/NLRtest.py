import spacy
import time
import matplotlib.pyplot as plt

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

def filter_sentences(file_path, filter_categories):
    with open(file_path, 'r', encoding='utf-8') as file:
        sentences = [line.strip() for line in file]

    filtered_sentences = []
    cumulative_times = []
    cumulative_time = 0
    word_counts = []
    word_count_sum = 0

    for sentence in sentences:
        start_time = time.time()
        doc = nlp(sentence)
        filtered = sentence
        word_count = 0


        for ent in doc.ents:
            if ent.label_ in filter_categories:
                filtered = filtered.replace(ent.text, "[FILTERED]")
                word_count += 1
                word_count_sum += 1

        end_time = time.time()
        time_taken = end_time - start_time
        cumulative_time += time_taken
        cumulative_times.append(cumulative_time)
        filtered_sentences.append(filtered)
        word_counts.append(word_count)
    print(word_count_sum)

    return sentences, filtered_sentences, cumulative_times, word_counts

def plot_cumulative_times(cumulative_times, title):
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, len(cumulative_times) + 1), cumulative_times, marker='o')
    plt.xlabel('Number of Sentences')
    plt.ylabel('Cumulative Time (seconds)')
    plt.title(title)
    plt.show()

def write_output(file_path, filtered_sentences, word_counts):
    with open(file_path, 'w', encoding='utf-8') as file:
        for sentence, count in zip(filtered_sentences, word_counts):
            file.write(f"{sentence} (Filtered Words: {count})\n")
#, "ORG", "DATE", "TIME", "MONEY", "QUANTITY", "ORDINAL", "CARDINAL", "GPE"
def main():
    filter_categories = {"PERSON" }
    for i in range(1, 11):
        input_file = f"sentences_{i}.txt"
        output_file = f"NLPfilteredsentence_{i}.txt"
        _, filtered_sentences, cumulative_times, word_counts = filter_sentences(input_file, filter_categories)
        plot_cumulative_times(cumulative_times, f"Cumulative Filtering Time for {input_file}")
        write_output(output_file, filtered_sentences, word_counts)

if __name__ == "__main__":
    main()
