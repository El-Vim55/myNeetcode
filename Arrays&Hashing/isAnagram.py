def isAnagram(s:str, t:str) -> bool:

    if len(s) != len(t):
        return False

    cnt = 0
    # l = sorted(t)
    for i, j in zip(sorted(s),sorted(t)):
        print(i,j)
        if i == j:
            cnt += 1
        # if sorted(t[i]) in sorted(s):
            # cnt += 1
    # print(cnt)
    if cnt == len(s):
        return True


    return False

print(isAnagram("anagram", "nagaram"))
# print(isAnagram("rat", "car"))
# print(isAnagram("aacc", "ccac"))