def transpose(mat: list[list[float | int]]) -> list[list]:
    if mat == []: return []
    ln_stl = len(mat[0])
    ls = [[] for _ in range(ln_stl)]
    for l in mat:
        if len(l) != ln_stl:
            return 'ValueError'
        for i in range(ln_stl):
            ls[i].append(l[i])
    return ls


def row_sums(mat: list[list[float | int]]) -> list[float]:
    ln_stl = len(mat[0])
    ls = []
    for l in mat:
        if len(l) != ln_stl:
            return 'ValueError'
        ls.append(sum(l))
    return ls


def col_sums(mat: list[list[float | int]]) -> list[float]:
    ln_stl = len(mat[0])
    ls = [0 for _ in range(ln_stl)]
    for l in mat:
        if len(l) != ln_stl:
            return 'ValueError'
        
        for i in range(ln_stl):
            ls[i] += l[i]
    return ls


print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))

print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))

print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
