s = 'azcbobobegghakl'
n = 0

for i in range(1, len(s)):
    if s[n:i] == ''.join(sorted(s[n:i])):
        longest = s[n:i]
    else:
        n += 1

print(longest)