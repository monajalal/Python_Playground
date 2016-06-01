def clean_string(string):
    result = []
    str_list = string.split()
    for word in str_list:
        result.append(''.join(ch for ch in word if ch.isalnum()))
    return "".join(result).lower()

def palindrome(string):
    cleaned = clean_string(string)
    print(cleaned)
    if cleaned[::-1]==cleaned:
        return True
    return False

str = "A man, a plan, a canal: Panama"

print(palindrome(str))