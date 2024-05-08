def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters = get_character_count(text)
    char_list = dict_list(characters)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    print(char_list)
    

def get_character_count(text):
    character_count = {}
    for i in text.lower():
        if i in character_count:
            character_count[i] += 1
        else:
            character_count[i] = 1
    return character_count       

def dict_list(characters):
    char_list = []
    for key, val in characters.items():
        char_list.append({key, val})
    return char_list

def get_num_words(text):
    words = text.split()
    return len(words)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

    

main()