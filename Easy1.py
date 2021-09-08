key = "SOLVECRYPTO"
Q = "UFJKXQZQUNB"
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
t = ""
for i in range(len(Q)):
    print((abc.index(Q[i]) - abc.index(key[i])) % 26)

    t += abc[abc.index(Q[i]) - abc.index(key[i]) % 26]
print(abc.index("M"))
print(t)

#tableをみると,縦横のabcのindexを足したものになっている。
#S + Key = T となっている
#よって S = T - key としてあげると求められる。
