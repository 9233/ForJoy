def cut(froms, starts, ends):
    str = froms.split(starts)
    strs = str[1].split(ends)
    return strs[0]

a = "555abcdefghijklmnopqrst123456789"
print cut(a,'cd','5')
