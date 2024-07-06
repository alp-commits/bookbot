def main():
    
    def word_counter(book_string):
        words = book_string.split()
        word_count = len(words)
        return word_count
    
    def char_counter(book_string):
        book = book_string.lower()
        char_dictionary = {}
        for char in book:
            if char in char_dictionary:
                char_dictionary[char] += 1
            else:
                char_dictionary[char] = 1
        return char_dictionary
    
    def sort_on(dict):
        return next(iter(dict.values()))

    def dictionary_to_list(dictionary): #this one is ok
        resulting_list = []
        for each_key in dictionary:
            temp_dictionary = {}
            temp_dictionary[each_key] = dictionary[each_key]
            resulting_list.append(temp_dictionary)
        return resulting_list
    
    def list_sorter(list_to_sort):
        sorted_list = list_to_sort
        sorted_list.sort(reverse=True, key=sort_on)
        return sorted_list

    def book_to_string(book_path):
        with open(book_path) as f:
            book_string = f.read()
            return book_string
        
    def list_printer(sorted_list): #this one is ok
        for dictionary in sorted_list:
            for key in dictionary.keys():
                if key.isalpha():
                    print(f"The {key} character was found {dictionary[key]} times\n")
            
        
    def make_report(book_path, sorted_list):
        print(f"--- Begin report of {book_path} ---")
        book = book_to_string(book_path)
        word_count = word_counter(book)
        print(f"{word_count} words found in the document")
        print()
        list_printer(sorted_list)
        print("--- End report ---")
    
    book_path = "books/frankenstein.txt"
    book_string = book_to_string(book_path)
    char_dictionary = char_counter(book_string)
    list_of_char_dicts = dictionary_to_list(char_dictionary)
    sorted_list = list_sorter(list_of_char_dicts)

    make_report(book_path, sorted_list)
    

main()