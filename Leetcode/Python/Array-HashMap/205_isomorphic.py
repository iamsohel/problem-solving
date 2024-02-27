def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    map_s_to_t = {}
    map_t_to_s = {}
    for i in range(len(s)):
        if s[i] in map_s_to_t and t[i] != map_s_to_t[s[i]]:
            return False
        else:
            map_s_to_t[s[i]] = t[i]
        if t[i] in map_t_to_s and s[i] != map_t_to_s[t[i]]:
            return False
        else:
            map_t_to_s[t[i]] = s[i]
    return True


print(isIsomorphic('badc', 'baba'))
