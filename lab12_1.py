import re


def to_string(number):
    return "{}".format(number)


def repeat_substr(substr, n):
    res = ""
    for i in range(n):
        res += substr
    return res


def get_las(s):
    for i in range(len(s)):
        for j in range(i + 1):
            substr = s[j:j + len(s) - i + 1]
            entries = [m.start() for m in re.finditer('(?=' + substr + ')', s)]
            if len(entries) > 1:
                return substr
