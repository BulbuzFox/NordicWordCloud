import json

def open_file(path):
    with open(path, encoding='utf-8') as f_in:
        return json.load(f_in)

def get_messages(chat_history):
    return chat_history['messages']
