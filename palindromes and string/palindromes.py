import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase

# This function alters the way of the text from the first index to the second
# removes punctuation 
def remove_punctuation(text):
    text = text.replace(" ", "")
    text = text.replace("?", "")
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("!", "")
    text = text.lower()
    return text


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    text = remove_punctuation(text)
    
    return is_palindrome_recursive(text, 0, len(text) - 1)


def is_palindrome_iterative(text):
    left_index = 0
    right_index = len(text) - 1
    
    while left_index < right_index:
        # Check to see if the left index does not match the right index
        if text[left_index] != text[right_index]:
            return False
        else:
           
            left_index += 1
            right_index -= 1
    return True


def is_palindrome_recursive(text, left=0, right=0):
    # check to see if empty
    if text == "":
        return True

    if left == right:# base case
        return True

    if text[left] != text[right]:
        return False

    if left < right:
        return is_palindrome_recursive(text, left + 1, right - 1)
    return True


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()