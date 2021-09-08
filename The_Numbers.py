num = [16,9,3,15,3,20,6,20,8,5,14,21,13,2,5,18,19,13,1,19,15,14]
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
t = ""
for i in range(len(num)):
	t += abc[num[i]-1]
print(t)

#numがアルファベットを表していると考えると,picoCTFのpの部分とoの部分の数字が16,15となっているので
#アルファベットで何番目かをnumが表していると考えられる。
