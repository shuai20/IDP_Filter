import nltk
import numpy as np
import random

# Download necessary NLTK resources
nltk.download('brown')
nltk.download('punkt')

# Import the Brown corpus
from nltk.corpus import brown

# Define the distribution function
def distribution_function(L):
    return 1.1 * L * (0.90 ** L)

# Get a list of sentences from the Brown corpus
brown_sentences = [' '.join(sent) for sent in brown.sents()]

# Generate sentence lengths based on the distribution
sentence_lengths = np.random.choice(np.arange(1, 100), p=distribution_function(np.arange(1, 100)) / distribution_function(np.arange(1, 100)).sum(), size=10000)

# Function to select sentences of a given length
def select_sentence_of_length(sentences, length):
    suitable_sentences = [s for s in sentences if len(s.split()) == length]
    return random.choice(suitable_sentences) if suitable_sentences else None

# Function to generate and save sentences to a file
def generate_and_save_sentences(file_name, num_sentences, sentence_lengths):
    with open(file_name, 'w') as file:
        for _ in range(num_sentences):
            sentence_length = random.choice(sentence_lengths)
            sentence = select_sentence_of_length(brown_sentences, sentence_length)
            if sentence:
                file.write(sentence + '\n')

# Generate 10 files each with 10,000 sentences
for i in range(10):
    file_name = f'sentences_{i+1}.txt'
    generate_and_save_sentences(file_name, 10000, sentence_lengths)
    print(f'Generated {file_name}')
