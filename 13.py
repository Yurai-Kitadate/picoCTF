Q = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"
abc = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(26):
    t = ""
    for j in range(len(Q)):
        if Q[j] in abc:
            t += abc[abc.index(Q[j])+i]
        else:
            t += Q[j]
    print(t)

    #どうせシーザー暗号なのでいつもので回す
    #picoCTFがでてくるのでそれがflag
