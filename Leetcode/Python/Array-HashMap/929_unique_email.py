def numUniqueEmails(emails):
    realEmails = []
    for email in emails:
        e = ""
        splittedEmail = email.split("@")
        for c in splittedEmail[0]:
            if c == "+":
                break
            if c.isalnum():
                e += c
        print(e)
        added = e + '@' + splittedEmail[1]
        realEmails.append(added)
    print(realEmails, set(realEmails))
    return len(set(realEmails))


# print(numUniqueEmails(["test.email+alex@leetcode.com",
#       "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))


def numUniqueEmails2(emails):
    unique = set()
    for email in emails:
        local, domain = email.split("@")
        local = local.split("+")[0]
        local = local.replace(".", "")
        unique.add((local, domain))
    print(unique)
    return len(unique)


print(numUniqueEmails2(["test.email+alex@leetcode.com",
      "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))


for i in range(10):
    if i == 2:
        break
    print(i)
