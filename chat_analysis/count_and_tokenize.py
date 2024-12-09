import re
from collections import Counter

tokenize_re = re.compile(r'\w+')

def count_words_in_message(messages):
    all_tokens = {}
    for message in messages:

        tokens = Counter(tokenize(message['text']))
        all_tokens = merge_counter(all_tokens, tokens)
    return all_tokens

def merge_counter(ca, cb):
    res = Counter(ca) + Counter(cb)
    return res

def tokenize(text):
    if isinstance(text, str):
        return tokenize_re.findall(text.lower())
