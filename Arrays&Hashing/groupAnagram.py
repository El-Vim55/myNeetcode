def groupAnagram(strs: list[str]) -> list[list[str]]:

    res = {}
    for i in strs:
        x = sorted(i)
        y = ''.join(x)
        if y not in res:
            res[y] = []
        res[y].append(i)
        # print(res[y])
    # print(res)
    a = []
    for string, group in res.items():
        a.append(group)
    print(a)
        # x = sorted(i)
        # x = i
        # y = ''.join(x)
        
    
    # return res

print(groupAnagram(["eat","tea","tan","ate","nat","bat"]))
# print(groupAnagram(["rate", "bate", "late", "fake", "gyat"]))