from copilot_workshop import sort_string_by_frequency

def test_sort_string_by_frequency():
    # Test case 1: Empty string
    assert sort_string_by_frequency("") == ""
    
    # Test case 2: String with one character
    assert sort_string_by_frequency("a") == "a"
    
    # Test case 3: String with multiple characters, all unique
    assert sort_string_by_frequency("abcdefg") == "abcdefg"
    
    # Test case 4: String with multiple characters, some repeated
    assert sort_string_by_frequency("abcaabbcc") == "aabbbccca"
    
    # Test case 5: String with multiple characters, all repeated
    assert sort_string_by_frequency("aaaaaabbbbbbcccccc") == "aaaaaabbbbbbcccccc"
