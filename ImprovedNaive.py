def ImprovedNaive(String, Pattern):
    i = 0
    while i <= len(String) - len(Pattern):
        for j in range(len(Pattern)):
            if String [i+j] != Pattern [j]:
                break
            j += 1
        if j == len(Pattern):
            print ("Found!")
            i = i + len(Pattern)
        elif j == 0:
            i = i + 1
        else:
            i = i+ j
