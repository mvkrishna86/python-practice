# ord()

def strtoint(s):
    isNegative = False
    num = 0
    if s[0] == "-":
        isNegative = True
        s = s[1:]
    for ch in s:
        i = ord(ch) - ord("0")
        if i < 0 or i > 9:
            print(f"Invalid number: {s}")
        else:
            num = num * 10 + i
    if isNegative:
        num = -num
    return num

print(strtoint("457"))
print(strtoint("-457"))
print(strtoint("4a57"))


