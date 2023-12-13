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
        smudge = False
        l = sl
        r = sl + 1
        while (all(x in range(len(pattern[0])) for x in  [r, l])):
            difference = 0
            left = [x[l] for x in pattern]
            right = [x[r] for x in pattern]
            for i, _ in enumerate(left):
                if (left[i] != right[i]): difference += 1
            if (difference == 1 and not smudge):
                smudge = True
                difference -= 1
            if (difference != 0): break
            l -= 1
            r += 1
        else:
            return smudge
        return False
    sl = 0
    while (sl <= len(pattern[0]) - 1):
        if (symmetrical(sl)): break
        sl += 1
    else:
        return None
    return sl + 1

def horizontal(pattern):
    def symmetrical(sl):
        smudge = False
        t = sl
        b = sl + 1
        while (all(x in range(len(pattern)) for x in  [t, b])):
            difference = 0
            top = pattern[t]
            bottom = pattern[b]
            for i, _ in enumerate(top):
                if (top[i] != bottom[i]): difference += 1
            
            if (difference == 1 and not smudge):
                smudge = True
                difference -= 1
            if (difference != 0): break
            t -= 1
            b += 1
        else:
            return smudge
        return False
    sl = 0
    while (sl <= len(pattern) - 1):
        if (symmetrical(sl)): break
        sl += 1
    else:
        return None
    return (sl + 1)*100

for pattern in patterns:
    value = vertical(pattern) or horizontal(pattern)
    ans += value

print(ans)

