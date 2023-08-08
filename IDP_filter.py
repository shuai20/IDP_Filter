import os
import csv
import re


class IDPFilter:
    # 初始化IDPFilter对象时定义数据集路径
    DATASET_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'datasets')

    def load_csv(self, filename):
        filepath = os.path.join(self.DATASET_PATH, filename + '.csv')
        if not os.path.exists(filepath):
            print(f"Warning: File {filepath} does not exist.")
            return []

        with open(filepath, 'r') as file:
            reader = csv.reader(file)
            return [row[0].strip() for row in reader if row]

    def filter_text(self, input_text, user_sensitive_words, user_non_sensitive_words, categories):
        """基于用户指定的敏感词、非敏感词和类别来过滤文本"""

        all_sensitive_words = set()

        # 如果用户选择了类别，加载相应类别的CSV文件
        if categories:
            for category in categories:
                filename = category + ".csv"
                all_sensitive_words.update(self.load_csv(category))

        # 加入用户自定义的敏感词

        all_sensitive_words.update(user_sensitive_words)

        # 移除用户定义的非敏感词
        all_sensitive_words.difference_update(user_non_sensitive_words)

        # 为了确保过滤不受标点符号的影响，我们可以用正则表达式替代split()方法
        import re
        words = re.findall(r'\b\w+\b', input_text)

        for index, word in enumerate(words):
            if word in all_sensitive_words:
                input_text = input_text.replace(word, '*' * len(word))

        print(all_sensitive_words)
        return input_text
