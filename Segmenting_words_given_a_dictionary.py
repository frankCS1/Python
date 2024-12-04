def word_break(string, dictionary):
    n = len(string)
    array = [False] * (n + 1)
    array[0] = True
    word_made = [[] for w in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i):
            if array[j] and string[j:i] in dictionary:
                array[i] = True
                word_made[i].append(string[j:i])

    if array[n]:
        print("Cannot be segmented into:")
        segmented(word_made, n)
    else:
        print("Cannot be segmented.")

    return array[n]

def segmented(word_made, i, current_segment=""):
    if i == 0:
        print(current_segment.strip())
        return
    for word in word_made[i]:
        segmented(word_made, i - len(word), word + " " + current_segment)

dictionary = {"coffee", "parrot", 'a', 'm', 'can', 'crate', 'walk', 'mmjop', 'fe'}
string1 = "canmwalkaacanmmjopmafea"
word_break(string1, dictionary)

