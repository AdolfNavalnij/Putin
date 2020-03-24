from random import randint
def xor(x,y):
	if x == y:
		return x,y
	else:
		return y,x
def randstr(x):
	s = ""
	S = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","_"]
	for i in range(x):
		s = s + S[randint(0,len(S)-1)]
	return s

T2 = []
if input() == "1":
	file = open("codes.txt", "w")
	for i in range(2566611):
		file.write(randstr(40) + "\n")
	file.close
file = open("codes.txt", "r")
for char in file:
	T2.append(char)
file.close
if input() == "1":
	file = open("codes2.txt", "w")
	for i in range(2566611):
		file.write(str(randint(0,256661)) + "\n")
	file.close
T = []
file = open("codes2.txt", "r")
for char in file:
	T.append(int(char))
file.close

def hash(T,T2,W):
	h = len(W) 
	for c in W:
		index = h + ord(c)
		h = T[index]
		g = T2[index]
	return g
while True:
 	print(hash(T,T2,input()))
