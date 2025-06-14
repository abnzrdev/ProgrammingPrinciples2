import re

# Match a string that has an 'a' followed by zero or more 'b's
def match_a_followed_by_b(s):
    pattern = r"a(b*)"
    return re.fullmatch(pattern, s) is not None

print(match_a_followed_by_b("a"))        # True
print(match_a_followed_by_b("ab"))       # True
print(match_a_followed_by_b("abb"))      # True
print(match_a_followed_by_b("ac"))       # False

# Match a string that has an 'a' followed by two to three 'b's
def match_a_followed_by_two_to_three_b(s):
    pattern = r"ab{2,3}"
    return re.fullmatch(pattern, s) is not None

print(match_a_followed_by_two_to_three_b("abb"))    # True
print(match_a_followed_by_two_to_three_b("abbb"))   # True
print(match_a_followed_by_two_to_three_b("abbbb"))  # False

# Match a string that has an 'a' followed by anything and ends with 'b'
def match_a_followed_by_anything_ending_in_b(s):
    pattern = r"a.*b$"
    return re.fullmatch(pattern, s) is not None

print(match_a_followed_by_anything_ending_in_b("a quick brown fox jumps over the lazy dog b"))  # True
print(match_a_followed_by_anything_ending_in_b("a quick brown fox"))  # False

# Find sequences of lowercase letters joined with an underscore
def find_lowercase_with_underscore(s):
    pattern = r"[a-z]+(_[a-z]+)+"
    return re.findall(pattern, s)

print(find_lowercase_with_underscore("hello_world_this_is_python"))  # ['hello_world', 'world_this', 'this_is']

# Find sequences of uppercase letter followed by lowercase letters
def find_uppercase_followed_by_lowercase(s):
    pattern = r"[A-Z][a-z]+"
    return re.findall(pattern, s)

print(find_uppercase_followed_by_lowercase("Hello World"))  # ['Hello', 'World']
