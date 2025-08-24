def words_in_book(book_contents):
    book_list = book_contents.split()
    return len(book_list)

def total_characters_used(book_contents):
    character_dict = {}
    lowercase_book_contents = book_contents.lower()
    list_of_characters = list(lowercase_book_contents)
    for character in list_of_characters:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

def book_report(char_dict):
    list_of_chars = []
    for char, num_char in char_dict.items():
        if char.isalpha():
            list_of_chars.append({"char": char, "num": num_char})
    
    def sort_on(characters):
        return characters["num"]
    
    list_of_chars.sort(reverse=True, key=sort_on)

    
    return list_of_chars

