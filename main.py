import json, string
from collections import Counter, defaultdict


SUMMARY = {
    'Letters count': {},
    'Total words quantity': 0,
    'Words count': {},
    'Top-5 words': []
}


def validate_word(word: str):
    return word.strip(string.punctuation).lower()


def read_and_get_data():
    src_file_name = input('Please enter a name or full path of the source file: ').strip()
    print()

    try:
        with open(src_file_name, 'r', encoding='utf-8') as f:
            data = f.read()
    except FileNotFoundError:
        print('No such file in this directory.\n')
        return None

    return data


def count_letters(text=None, verbose=False):
    if not text:
        data = read_and_get_data()
    else:
        data = text

    if data:
        spaces = (' ', '\n')
        letters_counter = Counter(letter.lower() for letter in data if letter not in string.punctuation and letter not in spaces)

        if verbose:
            for l, c in letters_counter.items():
                print(l + ' - ' + str(c))

        SUMMARY['Letters count'] = dict(letters_counter)
        return letters_counter

    return None


def get_total_words_qty(text=None, verbose=False):
    if not text:
        data = read_and_get_data()
    else:
        data = text

    if data:
        new_data = data.split()
        total = len(new_data)

        if verbose:
            print(f'Total quantity of words - {total}')

        SUMMARY['Total words quantity'] = total
        return total

    return None


def count_words(text=None, verbose=False):
    if not text:
        data = read_and_get_data()
    else:
        data = text

    if data:
        new_data = data.split()
        new_data_validated = []

        for word in new_data:
            new_data_validated.append(validate_word(word))

        if verbose:
            for w, c in Counter(new_data_validated).items():
                print(w + ' - ' + str(c))

        words_count = Counter(new_data_validated)

        SUMMARY['Words count'] = dict(words_count)
        return words_count

    return None


def get_top_5_words(text=None, verbose=False):
    if not text:
        data = count_words()
    else:
        data = count_words(text)

    if data:
        top_5_words = data.most_common(5)

        if verbose:
            print('Top-5 words')

            for w, c in top_5_words:
                print(w + ' - ' + str(c))

        SUMMARY['Top-5 words'] = top_5_words
        return top_5_words

    return None


def get_summary(text=None, verbose=False):
    if not text:
        data = read_and_get_data()
    else:
        data = text

    if data:
        count_letters(text=data)
        get_total_words_qty(text=data)
        count_words(text=data)
        get_top_5_words(text=data)

        with open('summary.json', 'w', encoding='utf-8') as f:
            json.dump(SUMMARY, f, ensure_ascii=False, indent=4)

        if verbose:
            print(SUMMARY)

        return None

    print('No data found.\n')
    return None


def main():
    session_data = read_and_get_data()

    if not session_data:
        if_launch_again = input('Do you want to try again? ').strip().lower()
        print()

        if if_launch_again == 'yes':
            main()

        return

    while True:
        user_choice = input('To count letters frequency (1)\tTo count all words click (2)\tTo count words frequency click (3)\tTo calculate full summary and save to json file click (4)\tTo exit click (5) ').strip()

        if user_choice == '1':
            count_letters(session_data, True)
        elif user_choice == '2':
            get_total_words_qty(session_data, True)
        elif user_choice == '3':
            count_words(session_data, True)
        elif user_choice == '4':
            get_summary(session_data, True)
        elif user_choice == '5':
            break
        else:
            print('Unknown command. Please try again.\n')


if __name__ == '__main__':
    main()
