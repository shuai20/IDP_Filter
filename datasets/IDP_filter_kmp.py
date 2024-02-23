import os
import csv
import re

class IDPFilter:
    # Set the dataset path when initializing the IDPFilter object
    DATASET_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'datasets')

    def __init__(self):
        self.total_filtered_count = 0

    def load_csv(self, filename):
        filepath = os.path.join(self.DATASET_PATH, filename + '.csv')
        if not os.path.exists(filepath):
            print(f"Warning: File {filepath} does not exist.")
            return []
        with open(filepath, 'r') as file:
            reader = csv.reader(file)
            return [row[0].strip() for row in reader if row]

    # KMP search algorithm for a pattern in a text
    def kmp_search(self, text, pattern):
        if pattern == "":
            return -1

        # Create longest prefix suffix (lps) array
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        # KMP search
        i = j = 0
        while i < len(text):
            if pattern[j] == text[i]:
                i += 1
                j += 1
            if j == len(pattern):
                return i - j
            elif i < len(text) and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1

    def filter_text(self, input_text, user_orb, user_srw, global_srb, categories):
        self.total_filtered_count = 0

        # Existing filtering logic
        srw_words = set(user_srw.split(',')) if user_srw else set()
        orb_words = set(user_orb.split(',')) if user_orb else set()
        csv_orb_words = set()

        if categories:
            for category in categories:
                csv_orb_words.update(self.load_csv(category))

        combined_orb = orb_words.union(csv_orb_words).difference(srw_words)
        global_srb_words = set(global_srb.split(',')) if global_srb else set()
        all_sensitive_words = combined_orb.union(global_srb_words)

        # Use KMP to search and filter
        for word in all_sensitive_words:
            match_index = self.kmp_search(input_text, word)
            while match_index != -1:
                input_text = input_text[:match_index] + '*' * len(word) + input_text[match_index + len(word):]
                match_index = self.kmp_search(input_text, word)
                self.total_filtered_count += 1

        return input_text, self.total_filtered_count