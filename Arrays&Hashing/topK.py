def topKFrequent(nums: list[int], k: int) -> list[int]:
    nums = sorted(nums)

    x = sorted([x for x in set(nums)])
    res = {}
    cnt = 1
    counter = 0
    for i in range(0, len(nums)):
        res[nums[i]] = cnt
        print(res)
        try:
            if x[-1] == nums[i] or ((x[counter] == nums[i]) and (nums[i+1] != x[counter+1])):
                cnt += 1
            else:
                cnt = 1
                counter += 1
        except IndexError:
            pass
    print(res)
    [24,12,8,6]

    val = sorted(res.values())
    val = list(val)[-k:]
    z = []
    for keys in res:
        if res[keys] in val:
            z.append(keys)
    return z

# print(topKFrequent([1,2,2,1,1,3], 2))
# print(topKFrequent([2,2,2,2,2,2,10,10,10,10,10,10,10,10,11,11,4,4,4,4,4,4,6,6,6,6], 2))
print(topKFrequent([4,1,-1,2,-1,2,3], 2))
# print(topKFrequent([1,1,1,2,2,3], 2))
# print(topKFrequent([1,1,1,2,2,2,3,3,3], 2))
# print(topKFrequent([1], 1))