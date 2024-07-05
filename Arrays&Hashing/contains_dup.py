def contain_dup(nums: list) -> bool:

    set_ = set()
    for num in nums:
        set_.add(num)
        
    set_ = sorted(set_)
    print(set_, sorted(nums))
    if set_ == nums:
        return False
    return True

print(contain_dup([3,1]))