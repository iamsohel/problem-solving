
def longestCommonPrefix(strs):
    result = ""
    for i in range(len(strs[0])):
        for c in strs:
            print(i, len(c))
            if i == len(c) or c[i] != strs[0][i]:
                return result
        result += strs[0][i]
    return result


print(longestCommonPrefix(["flower", "flowe", "floweight"]))
