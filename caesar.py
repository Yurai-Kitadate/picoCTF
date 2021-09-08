Q = "dspttjohuifsvcjdpoabrkttds"
abc = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(26):
    t = ""
    for j in range(len(Q)):
        if Q[j] in abc:
            t += abc[abc.index(Q[j])+i]
        else:
            t += Q[j]
    print(t)

    #シフト暗号です
    #脊髄で解けるようにしよう！！
  
