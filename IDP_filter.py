import os
import csv
import re


class IDPFilter:
    # set the dataset path when initialize IDPFilter object
    DATASET_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'datasets')

    def load_csv(self, filename):
        filepath = os.path.join(self.DATASET_PATH, filename + '.csv')
        if not os.path.exists(filepath):
            print(f"Warning: File {filepath} does not exist.")
            return []

        with open(filepath, 'r') as file:
            reader = csv.reader(file)
            return [row[0].strip() for row in reader if row]

    def filter_text(self, input_text, user_orb, user_srw, global_srb, categories):
        """filter the text based on the sensitive words and non-sensitive words desginated by users"""
        #srb_words = set(user_srb.split(',')) if user_srb else set()
        srw_words = set(user_srw.split(',')) if user_srw else set()
        orb_words = set(user_orb.split(',')) if user_orb else set()

        # Load CSV files for chosen categories and treat them as SRW
        csv_orb_words = set()
        if categories:
            for category in categories:
                csv_orb_words.update(self.load_csv(category))

        # Combine SRW from user and CSV
        combined_orb = orb_words.union(csv_orb_words)

        # Remove SRW words from ORB
        combined_orb.difference_update(srw_words)
        print(combined_orb)

        # Convert global SRB to set
        global_srb_words = set(global_srb.split(',')) if global_srb else set()

        # Add user-specific SRB to the sensitive words set
        all_sensitive_words = combined_orb.union(global_srb_words)

        # Split the input text into words considering punctuation
        words = re.findall(r'\b\w+\b', input_text)

        # Filter the text
        filtered_count = 0
        for word in words:
            if word in all_sensitive_words:
                filtered_count += 1
                input_text = input_text.replace(word, '*' * len(word))

        return input_text, filtered_count

        # # 从ORB中移除SRW中的词汇
        # orb_words.difference_update(srw_words)
        #
        # all_sensitive_words = set()
        #
        # # load the CSV file if users choose this category
        # if categories:
        #     for category in categories:
        #         filename = category + ".csv"
        #         all_sensitive_words.update(self.load_csv(category))
        #
        # # add the sensitive words customized by users
        #
        # all_sensitive_words.update(user_sensitive_words)
        #
        # # remove the non-sensitive words defined by users
        # all_sensitive_words.difference_update(user_non_sensitive_words)
        #
        #
        #
        #
        # # To make sure the filtering won't be affected by the punctuation, use RE to replace spilt() methods
        # import re
        # words = re.findall(r'\b\w+\b', input_text)
        #
        # for index, word in enumerate(words):
        #     if word in all_sensitive_words:
        #         input_text = input_text.replace(word, '*' * len(word))
        #
        # print(all_sensitive_words)
        #
        # filtered_count = 0
        #
        # if global_srb in input_text:
        #     input_text = input_text.replace(global_srb, '*' * len(global_srb))
        #     filtered_count += 1
        #
        #     # 处理ORW
        # if user_orw and user_orw in input_text:
        #     # 如果文本中包含ORW中的词，那么从ORB中移除该词
        #     user_sensitive_words.discard(user_orw)
        # for index, word in enumerate(words):
        #     if word in all_sensitive_words:
        #         filtered_count += 1
        #         input_text = input_text.replace(word, '*' * len(word))
        # return input_text, filtered_count
