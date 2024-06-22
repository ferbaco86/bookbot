def main ():
    book_text = get_text("books/frankenstein.txt")
    words_amount = get_words_amount(book_text)
    counted_chars_dict = (count_chars(book_text))
    counted_chars_dict_list = get_alpha_chars(counted_chars_dict)
    counted_chars_dict_list.sort(reverse=True, key=lambda x: list(x.values())[0])
    get_report(words_amount, counted_chars_dict_list)

def get_text(file_path):
     with open(file_path) as f:
        text = f.read()
        return text
     
def count_chars(book_text):
    words_dict = {}
    for char in book_text:
        lower_case_word = char.lower()
        if lower_case_word in words_dict:
            words_dict[lower_case_word] += 1
        else:
            words_dict[lower_case_word] = 1
    return words_dict

def get_alpha_chars(dict):
    chars_list = []
    for key in dict:
        if key.isalpha():
            chars_list.append({key: dict[key]})
    return chars_list

def get_words_amount(text):
    words = text.split()
    return len(words)

def get_report(words_amount, sorted_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_amount} words found in the document")
    for item in sorted_list:
        for key, value in item.items():
            print(f"The {key} character was found {value} times")
main()