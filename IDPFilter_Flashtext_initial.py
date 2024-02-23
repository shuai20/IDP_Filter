import os
import csv
from flashtext import KeywordProcessor

class IDPFilter:
    DATASET_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'datasets')

    def __init__(self):
        self.keyword_processor = KeywordProcessor(case_sensitive=True)
        self.total_filtered_count = 0

    def load_csv(self, filename):
        filepath = os.path.join(self.DATASET_PATH, filename + '.csv')
        if not os.path.exists(filepath):
            print(f"Warning: File {filepath} does not exist.")
            return []
        with open(filepath, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    keyword = row[0].strip()
                    self.keyword_processor.add_keyword(keyword, '*' * len(keyword))

    def filter_numbers(self, text):
        self.keyword_processor.add_keyword(r'\b\d+\b', '*' * len('number'))
        return self.keyword_processor.replace_keywords(text)

    def filter_links(self, text):
        self.keyword_processor.add_keyword(r'https?://\S+|www\.\S+', '*' * len('link'))
        return self.keyword_processor.replace_keywords(text)

    def filter_text(self, input_text, user_orb, user_srw, global_srb, categories):
        self.total_filtered_count = 0

        # Load CSV files for chosen categories
        for category in categories:
            self.load_csv(category)

        # Filter numbers and links if they are in categories
        if 'number' in categories:
            input_text = self.filter_numbers(input_text)
        if 'link' in categories:
            input_text = self.filter_links(input_text)

        # Add user-specific ORB and SRB words to FlashText
        for word in user_orb.split(','):
            self.keyword_processor.add_keyword(word, '*' * len(word))

        for word in global_srb.split(','):
            self.keyword_processor.add_keyword(word, '*' * len(word))

        # Filter the text
        filtered_text = self.keyword_processor.replace_keywords(input_text)

        # Calculate the count of filtered words
        self.total_filtered_count = len(self.keyword_processor.extract_keywords(input_text))
        return filtered_text, self.total_filtered_count

# Example usage:
# idp_filter = IDPFilter()
# filtered_text, count = idp_filter.filter_text("Sample text", "user_orb_words", "user_srw_words", "global_srb_words", ["number", "link"])
