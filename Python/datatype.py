# list
# add
from collections import deque
letters = []
letters.append("a")
letters.append("b")
letters.append("c")
letters.insert(0, "-")
print(letters)

# find
if 'a' in letters:
    print(letters.index('a'))

# remove
letters.pop()
letters.remove("a")
del letters[0:3]
letters.clear()
print(letters)

numbers = list(range(20))
# print(numbers[::2])

# iterate
# range(1, 12, 2) start, end, increment by
for index, letter in enumerate(letters, 1):
    print(index, letter)


# stacks
browsering_session = []
browsering_session.append(1)
browsering_session.append(2)
top = browsering_session.pop()
print("pop: ", top, browsering_session)
if browsering_session:
    print("top ", browsering_session[-1])

# queue
queue = deque([])
queue.append(1)
queue.append(2)
queue.popleft()
print("queue ", queue)


def findMostRepeatedChar(chars):
    charDict = {}
    for char in chars:
        if char in charDict:
            charDict[char] += 1
        else:
            charDict[char] = 1
    sortedChars = sorted(charDict.items(), key=lambda kv: kv[1])
    return sortedChars[-1]


# print(findMostRepeatedChar("this is the most common interviewtttttt question"))
