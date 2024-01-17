import nltk
from nltk.corpus import words
import random
# 下载NLTK的词汇数据
nltk.download('words')

# 获取英语词汇列表
english_words = set(nltk.corpus.words.words())

# 生成一个随机的有意义句子
def generate_meaningful_sentence():
    sentence = []
    for _ in range(random.randint(5, 15)):  # 随机选择句子长度
        word = random.choice(list(english_words))
        sentence.append(word)
    return ' '.join(sentence)

meaningful_sentence = generate_meaningful_sentence()
print(meaningful_sentence)
