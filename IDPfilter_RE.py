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

    def filter_numbers(self, text):
        numbers_pattern = r'\b\d+\b'
        matches = re.findall(numbers_pattern, text)
        count = len(matches)
        self.total_filtered_count += count
        return re.sub(numbers_pattern, '*' * len('number'), text)

    def filter_links(self, text):
        url_pattern = r'https?://\S+|www\.\S+'
        matches = re.findall(url_pattern, text)
        count = len(matches)
        self.total_filtered_count += count
        return re.sub(url_pattern, '*' * len('link'), text)

    def filter_text(self, input_text, user_orb, user_srw, global_srb, categories):
        if categories is None:
            categories = []



        self.total_filtered_count = 0
        srw_words = set(user_srw.split(',')) if user_srw else set()
        orb_words = set(user_orb.split(',')) if user_orb else set()

        # Load CSV files for chosen categories and treat them as SRW


        csv_orb_words = set()
        if categories:
            for category in categories:
                csv_orb_words.update(self.load_csv(category))

        if 'number' in categories:
            input_text = self.filter_numbers(input_text)
        if 'link' in categories:
            input_text = self.filter_links(input_text)

        # Combine SRW from user and CSV
        combined_orb = orb_words.union(csv_orb_words)

        # Remove SRW words from ORB
        combined_orb.difference_update(srw_words)

        # Convert global SRB to set
        global_srb_words = set(global_srb.split(',')) if global_srb else set()

        # Add user-specific SRB to the sensitive words set
        all_sensitive_words = combined_orb.union(global_srb_words)

        # Split the input text into words considering punctuation
        words_and_phrases = re.findall(r'\b[\w\']+\b', input_text)

        # Filter the text
        filtered_text = input_text
        for word in all_sensitive_words:
          #  pattern = re.compile(r'\b{}\b'.format(re.escape(word)))
            pattern = re.compile(r'\b{}\b'.format(re.escape(word)), re.IGNORECASE)
            matches = pattern.findall(filtered_text)
            self.total_filtered_count += len(matches)
            filtered_text = pattern.sub('*' * len(word), filtered_text)

        return filtered_text, self.total_filtered_count