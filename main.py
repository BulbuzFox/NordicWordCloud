import argparse
import chat_analysis.parse_chat as parse_chat
import chat_analysis.count_and_tokenize as count_and_tokenize
import chat_analysis.generate_image as image_generator


def parse_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('history_path')
    arg_parser.add_argument('image_path')
    return arg_parser.parse_args()

def main():
    args = parse_args()
    print(f'History path {args.history_path}')
    print(f'Image path {args.image_path}')

    chat_history = parse_chat.open_file(args.history_path)
    all_messages = parse_chat.get_messages(chat_history)

    word_counts = count_and_tokenize.count_words_in_message(all_messages)

    image_generator.generate_image(word_counts, args.image_path)

if __name__ == '__main__':
    main()
