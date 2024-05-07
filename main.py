def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters = get_character_count(text)
    print(characters)

def get_character_count(text):
    character_count = {}
    for i in text.lower():
        if i in character_count:
            character_count[i] += 1
        else:
            character_count[i] = 1
    return character_count

def get_num_words(text):
    words = text.split()
    return len(words)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

    

main()

