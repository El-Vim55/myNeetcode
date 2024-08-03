
def twoSum(numbers: list[int], target: int) -> list[int]:
    i = 0
    j = len(numbers) - 1

    while True:
        if (numbers[i] + numbers[j]) < target:
            i += 1
        elif (numbers[i] + numbers[j]) > target:
            j -= 1
        else:
            n1, n2 = numbers[i], numbers[j]
            break
    
    n1 = numbers.index(n1) + 1
    numbers[n1-1] = 'a'
    n2 = numbers.index(n2) + 1
    return [n1,n2]

# print(twoSum([2,7,11,15], 9))  # OUtput -> [1,2]
print(twoSum([0,0,3,4], 0))