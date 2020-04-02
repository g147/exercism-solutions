import re
from collections import Counter

def count_words(sentence):
  words = re.findall(r"[a-zA-Z\d]+(?:\'t)?", sentence)
  return Counter(map(str.lower, words))