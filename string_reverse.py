
def reverse(str1):
    revstr = ""
    for ch in str1:
        revstr = ch + revstr
    print(revstr)

    for ch in str1[::-1]:
        print(ch, end="")
    print("")

reverse("abcd")
reverse("abcdef")




