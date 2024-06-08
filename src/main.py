
def find_words(input_string, dictionary):
    """
    This function returns an array of words from the dictionary that can be formed by rearranging some or 
    all of the letters in the input string.

    Args:
        input_string (str): The input string.
        dictionary (list): The list of words to check against.

    Returns:
        list: A list of words that can be formed from the input string.
    """
    result = []

    # If string is empty return empty result
    if not input_string:
        return result
    
    letter_map = build_frequency_map(input_string)

    # For every word in dictionary, check if word can be formed and if so, add to the result 
    for word in dictionary:
        if can_form_word(word, letter_map):
            result.append(word)

    return result


def can_form_word(word, letter_map):
    """ 
    This function checks if a word can be formed given the restrictions with the input string.

    Args:
        word (str): The word to check.
        letter_map (dict): The frequency map of letters from the input string.

    Returns:
        bool: True if the word can be formed, False otherwise.
    """
    # Make shallow copy of map for frequency manipulation
    temp_map = letter_map.copy()

    # If letter not found or frequency not enough, word cannot be formed
    for letter in word:
        if letter in temp_map and temp_map[letter] > 0 :
            temp_map[letter] -= 1
        else:
            return False  

    return True    


def build_frequency_map(input_string):
    """
    This function builds a frequency map of letters from the input string.

    Args:
        input_string (str): The input string.

    Returns:
        dict: A dictionary with letters as keys and their frequencies as values.
    """

    letter_map = {}

    # For empty string or spaces return empty hash
    if(len(input_string.rstrip())==0):
        return letter_map
    
    # Build letter map with frequency of letters
    for letter in input_string:
        if letter in letter_map:
            letter_map[letter] += 1
        else:
            letter_map[letter] = 1

    return letter_map