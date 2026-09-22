inp = input('in: ')
st = ''
i1 = 0
i2 = 0
for i in range(len(inp)):
    s = inp[i]
    if s == s.upper(): 
        i1 = i
        st = st + s
        break

for i in range(len(inp)):
    s = inp[i]
    if s.isdigit():
        i2 = i+1
        st = st + inp[i+1]
        break


step = abs(i2-i1)
for i in range(i2+step, len(inp), step):
    s = inp[i]
    st = st + s
    
print(f'out: {st}')
