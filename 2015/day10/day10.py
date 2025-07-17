# https://adventofcode.com/2015/day/10

def look_and_say(s):
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(str(count))
            result.append(s[i - 1])
            count = 1
    result.append(str(count))
    result.append(s[-1])
    return ''.join(result)

# part 1
s = "3113322113"
for _ in range(40):
    s = look_and_say(s)
print(len(s))

# part 2
s = "3113322113"
for _ in range(50):
    s = look_and_say(s)
print(len(s))