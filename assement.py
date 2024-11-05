def find_non_repeated(s):
    counts = [0] * 256
    for char in s:
        counts[ord(char)] += 1
    for char in s:
        if counts[ord(char)] == 1:
            return char  
    return None

input_strings = ["swiss", "aabb", "racecar", "hello", "teeter"]

for input_string in input_strings:
    result = find_non_repeated(input_string)
    
    if result:
        print(f"The non-repeated character in '{input_string}' is: '{result}'")
    else:
        print(f"There are no non-repeating characters in '{input_string}'")
