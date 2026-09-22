def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
        try:
            return (min(nums), max(nums))
        except Exception as ex:
            return 'ValueError'
               


def unique_sorted(nums: list[float | int]) -> list[float | int]:
        return sorted(set(nums))
        

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