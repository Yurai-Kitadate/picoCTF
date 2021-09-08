Q = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_uJdSftmh}"
abc = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(26):
    t = ""
    for j in range(len(Q)):
        if Q[j] in abc:
            t += abc[abc.index(Q[j])+i]
        else:
            t += Q[j]
    print(t)

#mod 26からアルファベットを何個かずらすだけだとわかる
#適当にループを回すとpicoCTFという文字列が見つかるのでそれがflag
