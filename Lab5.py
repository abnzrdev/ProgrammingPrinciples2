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
