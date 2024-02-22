
print("A man, a plan, a canal: Panama".lower())


def palindrome(s):
    if s == '':
        return True
    str2 = ''
    for i in s.lower():
        if i.isalnum():
            str2 += i
    str3 = str2[::-1]
    return str2 == str3


palindrome("A man, a plan, a canal: Panana")
