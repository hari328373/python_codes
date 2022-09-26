#count of word

def word_order(n,i):
    count= {}
    l=[]
    for i in range(n):
        word = input()
        l.append(word)
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    return (len(count))
    return ' '.join([str(count[word]) for word in count])


