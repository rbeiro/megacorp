def count_words(string):
    return len(string.split())

def count_character(string):
    normalized_string = string.lower()
    characters_count = {}

    for character in normalized_string:
        if character in characters_count:
            characters_count[character] += 1
        else:
            characters_count[character] = 1

    return characters_count

def sort_dicts(dict_char_count):
    unsorted_list = []
    for dict in dict_char_count:

        new_dict = {
            "char": dict,
            "num": dict_char_count[dict]
        }

        unsorted_list.append(new_dict)

    def sort_on(dict):
        return dict["num"]

    unsorted_list.sort(reverse=True, key=sort_on)
    return unsorted_list

