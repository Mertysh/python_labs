def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
        if nums == []:
            return 'ValueError'
        try:
            mi = 10**10
            ma = 0
            for x in nums:
                  if x < mi: mi = x
                  if x > ma: ma = x
            return (mi, ma)
    
        except Exception as ex:
            return 'ValueError'
               


def unique_sorted(nums: list[float | int]) -> list[float | int]:
        nums = list(set(nums))
        l = len(nums)
        for i in range(l):
            for j in range(0, l - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums
        

def flatten(mat: list[list | tuple]) -> list:
        l = []
        for i in mat:
            if not type(i) is list and not type(i) is tuple:
                return 'TypeError'
            l += i
        return l

print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))

print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
