import re

in_str = input("Послідовність: ")
re_pattern = r"(?:[A-Za-z]+\.)"
re_match = re.findall(re_pattern, in_str)[0]
latin = {s for s in re_match}

print(latin)