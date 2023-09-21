def sort_string_by_frequency(string):
    # Create a dictionary to store the frequency of each character
    freq_dict = {}
    for char in string:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    
    # Sort the characters in the string based on their frequency in descending order
    sorted_chars = sorted(string, key=lambda x: freq_dict[x], reverse=True)
    
    # Create a new string by concatenating the sorted characters
    sorted_string = ''.join(sorted_chars)
    
    return sorted_string


