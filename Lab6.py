import re

def extract_emails(data):
    regex = r'[\w.-]+@[\w.-]+\.(?:com|org|net)'
    return re.findall(regex, data)

# 1. Email extraction
text_block = "Contact us at info@example.com or support@mydomain.org and admin@abc.net"
print("Extracted Emails:", extract_emails(text_block))

# 2. Log parsing for IP and timestamp
def parse_log(entry):
    return re.findall(r'(\d{1,3}(?:\.\d{1,3}){3})\s.*\[(.*?)\]', entry)

log_sample = '123.45.67.89 - - [10/Oct/2022:13:55:36 -0700] "GET /index.html HTTP/1.1" 200 2326'
print("Log IP and Date:", parse_log(log_sample))

# 3. Password validation
def validate_password(pwd):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
    return bool(re.fullmatch(pattern, pwd))

print("Password valid?", validate_password("StrongPass1"))

# 4. Hashtag extraction
def get_hashtags(s):
    return re.findall(r'#\w[\w\ufe0f\u200d]*', s)

tweet_text = "Loving the new #Python3.11 update! #💻 #Code_Newbie"
print("Tweet Hashtags:", get_hashtags(tweet_text))

# 5. Phone normalization

def normalize_phones(raw):
    pat = r'(?:\+?7|8)[\s-]?(\d{3})[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})'
    return [f'+7 ({a}) {b}-{c}-{d}' for a, b, c, d in re.findall(pat, raw)]

phones_input = "Call us at +7 701 123 4567 or 87011234567 or 7-701-123-45-67."
print("Standardized Phones:", normalize_phones(phones_input))
