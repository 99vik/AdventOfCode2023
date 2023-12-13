patterns = []
data = {}
ans = 0
with open('./day13/data.txt') as file:
    i = 0
    for line in file:
        if (i >= len(patterns)): patterns.append([])
        if (line.rstrip() == ''):
            i += 1
            continue
        patterns[i].append(line.rstrip())

def vertical(pattern):
    def symmetrical(sl):
        l = sl -1
        r = sl
        while (all(x in range(len(pattern[0])) for x in  [r, l])):
            if ([x[l] for x in pattern] != [x[r] for x in pattern]): break
            l -= 1
            r += 1
        else:
            return True
        return False
    sl = 0
    prev = []
    while (sl <= len(pattern[0]) - 1):
        current = [x[sl] for x in pattern]
        if (current == prev and symmetrical(sl)): break
        prev = current
        sl += 1
    else:
        return None
    return sl

def horizontal(pattern):
    def symmetrical(sl):
        t = sl -1
        b = sl
        while (all(x in range(len(pattern)) for x in  [b, t])):
            if (pattern[b] != pattern[t]): break
            t -= 1
            b += 1
        else:
            return True
        return False
    sl = 0
    prev = []
    while (sl <= len(pattern) - 1):
        current = pattern[sl]
        if (current == prev and symmetrical(sl)): break
        prev = current
        sl += 1
    else:
        return None
    return sl*100

for pattern in patterns:
    value = vertical(pattern) or horizontal(pattern)
    ans += value

print(ans)

