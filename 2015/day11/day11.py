# https://adventofcode.com/2015/day/11

def has_no_iol(s):
    return 'i' not in s and 'o' not in s and 'l' not in s

def has_straight(s):
    for i in range(len(s) - 2):
        if ord(s[i]) + 1 == ord(s[i+1]) and ord(s[i]) + 2 == ord(s[i+2]):
            return True
    return False

def has_two_pairs(s):
    pairs = set()
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            pairs.add(s[i])
            i += 2
        else:
            i += 1
    return len(pairs) >= 2

def is_valid_password(s):
    return has_no_iol(s) and has_straight(s) and has_two_pairs(s)

def increment_password(s):
    s = list(s)
    i = len(s) - 1
    while i >= 0:
        if s[i] == 'z':
            s[i] = 'a'
            i -= 1
        else:
            s[i] = chr(ord(s[i]) + 1)
            break
    return ''.join(s)

def find_next_password(s):
    while True:
        s = increment_password(s)
        if is_valid_password(s):
            return s

s = find_next_password("hxbxwxba")
print(s)
print(find_next_password(s))