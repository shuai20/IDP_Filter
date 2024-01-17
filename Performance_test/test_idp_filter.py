# test_idp_filter.py

import time
from IDP_filter import IDPFilter

def load_sentences_from_file(filename):
    with open(filename, "r") as file:
        return file.readlines()

def test_filter_performance(idp_filter, sentences, user_orb, user_srw, user_srb, categories):
    start_time = time.time()
    for sentence in sentences:
        idp_filter.filter_text(sentence, user_orb, user_srw, user_srb, categories)
    end_time = time.time()
    return end_time - start_time

def main():
    idp_filter = IDPFilter()

    # 示例：这些敏感词汇和类别应根据您的实际测试需求调整
    user_orb = "apple,banana"
    user_srw = "dog"
    user_srb = "city"
    categories = ["country"]

    for count in [1, 2, 3]:
        filename = f"sentences_{count}.txt"
        sentences = load_sentences_from_file(filename)
        duration = test_filter_performance(idp_filter, sentences, user_orb, user_srw, user_srb, categories)
        print(f"Processed {count} sentences in {duration:.2f} seconds.")

if __name__ == "__main__":
    main()
