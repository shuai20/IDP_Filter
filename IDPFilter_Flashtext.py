# import os
# import csv
# from flashtext import KeywordProcessor
# import re
#
#
# class IDPFilter:
#     DATASET_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'datasets')
#
#     def __init__(self):
#         self.keyword_processor = KeywordProcessor(case_sensitive=True)
#         self.total_filtered_count = 0
#
#     def load_csv(self, filename):
#         filepath = os.path.join(self.DATASET_PATH, filename + '.csv')
#         if not os.path.exists(filepath):
#             print(f"Warning: File {filepath} does not exist.")
#             return []
#         with open(filepath, 'r') as file:
#             reader = csv.reader(file)
#             for row in reader:
#                 if row:
#                     keyword = row[0].strip()
#                     self.keyword_processor.add_keyword(keyword, '*' * len(keyword))
#
#     def filter_numbers_and_links(self, text, categories):
#         number_count = link_count = 0
#         if 'number' in categories:
#             number_pattern = r'\b\d+\b'
#             number_matches = re.findall(number_pattern, text)
#             number_count = len(number_matches)
#             text = re.sub(number_pattern, '*' * len('number'), text)
#
#         if 'link' in categories:
#             link_pattern = r'https?://\S+|www\.\S+'
#             link_matches = re.findall(link_pattern, text)
#             link_count = len(link_matches)
#             text = re.sub(link_pattern, '*' * len('link'), text)
#
#         return text, number_count + link_count
#
#     def filter_text(self, input_text, user_orb, user_srw, global_srb, categories):
#         if categories is None:
#             categories = []
#
#         self.total_filtered_count = 0
#         srw_words = set(user_srw.split(',')) if user_srw else set()
#
#         # Resetting FlashText processor to clear previous state
#         self.keyword_processor = KeywordProcessor(case_sensitive=True)
#
#         # Load CSV files for chosen categories
#         for category in categories:
#             self.load_csv(category)
#
#         # Filter numbers and links and update count
#         input_text, num_link_count = self.filter_numbers_and_links(input_text, categories)
#         self.total_filtered_count += num_link_count
#
#         # Combine ORB from user and CSV, remove SRW words
#         combined_orb = set(user_orb.split(',')).union(set()).difference(srw_words)
#
#         # Add global SRB words
#         global_srb_words = set(global_srb.split(','))
#
#         # Filter the text using FlashText for ORB and SRB, excluding SRW
#         for word in combined_orb.union(global_srb_words):
#             if word not in srw_words:
#                 self.keyword_processor.add_keyword(word, '*' * len(word))
#
#         # Update total filtered count including keywords
#         self.total_filtered_count += len(self.keyword_processor.extract_keywords(input_text))
#
#         filtered_text = self.keyword_processor.replace_keywords(input_text)
#
#
#
#         return filtered_text, self.total_filtered_count
#
# # Example usage
# # idp_filter = IDPFilter()
# # filtered_text, count = idp_filter.filter_text("Sample text", "user_orb_words", "user_srw_words", "global_srb_words", ["number", "link"])
import os
import csv
from flashtext import KeywordProcessor
import re


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
        words = []
        with open(filepath, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    words.append(row[0].strip())
        return words

    def filter_numbers_and_links(self, text, categories):
        number_count = link_count = 0
        if 'number' in categories:
            number_pattern = r'\b\d+\b'
            number_matches = re.findall(number_pattern, text)
            number_count = len(number_matches)
            text = re.sub(number_pattern, '*' * len('number'), text)

        if 'link' in categories:
            link_pattern = r'https?://\S+|www\.\S+'
            link_matches = re.findall(link_pattern, text)
            link_count = len(link_matches)
            text = re.sub(link_pattern, '*' * len('link'), text)

        return text, number_count + link_count

    def filter_text(self, input_text, user_orb, user_srw, global_srb, categories):
        if categories is None:
            categories = []

        self.total_filtered_count = 0
        srw_words = set(user_srw.split(',')) if user_srw else set()

        # Resetting FlashText processor
        self.keyword_processor = KeywordProcessor(case_sensitive=False)

        # Load words from CSV files for chosen categories
        all_csv_words = []
        for category in categories:
            all_csv_words.extend(self.load_csv(category))

        # Filter numbers and links
        input_text, num_link_count = self.filter_numbers_and_links(input_text, categories)
        self.total_filtered_count += num_link_count

        # Combine ORB, SRB, and CSV words, excluding SRW
        combined_words = set(user_orb.split(',')) | set(global_srb.split(',')) | set(all_csv_words)
        combined_words -= srw_words

        # Add combined words to FlashText
        for word in combined_words:
            self.keyword_processor.add_keyword(word, '*' * len(word))

        # Count filtered words before actual filtering
        self.total_filtered_count += len(self.keyword_processor.extract_keywords(input_text))

        filtered_text = self.keyword_processor.replace_keywords(input_text)

        return filtered_text, self.total_filtered_count

# Example usage
# idp_filter = IDPFilter()
# filtered_text, count = idp_filter.filter_text("Sample text", "user_orb_words", "user_srw_words", "global_srb_words", ["number", "link"])
