# Note: Algorithm is taken from internet how can I write it on my own. But i fully understand the implementation of algorithm
# Its working is explained on pdf which I uploaded

def BoyerMooreHorspool(pattern, text):
    m = len(pattern)
    n = len(text)
    if m > n:
        return -1
    skip = []
    for k in range(256):
        skip.append(m)
    for k in range(m - 1):
        skip[ord(pattern[k])] = m - k - 1
    skip = tuple(skip)
    k = m - 1
    while k < n:
        j = m - 1; i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1; i -= 1
        if j == -1:
            return i + 1
        k += skip[ord(text[k])]
    return -1
