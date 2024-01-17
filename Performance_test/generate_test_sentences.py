# generate_test_sentences.py

import random

def generate_sentence():
    words = ["apple", "banana", "city", "dog", "elephant", "flower", "Czech Republic"]
    return " ".join(random.choice(words) for _ in range(random.randint(5, 15)))

def generate_test_sentences(number_of_sentences):
    return [generate_sentence() for _ in range(number_of_sentences)]

def save_sentences_to_file(sentences, filename):
    with open(filename, "w") as file:
        for sentence in sentences:
            file.write(sentence + "\n")

def main():
    for count in [1000, 5000, 10000]:
        sentences = generate_test_sentences(count)
        filename = f"test_sentences_{count}.txt"
        save_sentences_to_file(sentences, filename)
        print(f"Generated {count} sentences in {filename}")

if __name__ == "__main__":
    main()
