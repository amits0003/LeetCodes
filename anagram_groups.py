def group_anagrams(words):
    anagram_groups = {}

    # Iterate through each word in the list
    for word in words:
        # Sort the word and use it as a key
        sorted_word = tuple(sorted(word))

        # Check if the sorted word is already a key in the dictionary
        if sorted_word in anagram_groups:
            # Append the word to the existing list
            anagram_groups[sorted_word].append(word)
        else:
            # If the key doesn't exist, create a new entry
            anagram_groups[sorted_word] = [word]

    # Return the grouped anagrams as a list of lists
    return list(anagram_groups.values())


# Example usage
words = ['as', 'sa', 'drf', 'frd', 'gfgg', 'gggf']
result = group_anagrams(words)
print(result)
