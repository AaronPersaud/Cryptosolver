def encrypt(message, key):
	m = message.upper()
	k = key.upper()
	s = ""
	for i in range(0, min(len(m),len(k))):
		if k[i] == " " or k[i] == "'":
			u = m[i]
		elif m[i] == " " or m[i] == "'":
			u = k[i]
		else:
			u = chr(ord(m[i]) + ord(k[i]) - ord('A')+1)
		if u == '@' or u == "'":
			s += " "
		elif ord(u) > ord("Z"):
			s += chr(ord(u) - 27)
		else:
			s += u
	return s

def decrypt(message, key):
	m = message.upper()
	k = key.upper()
	s = ""
	for i in range(0,min(len(m),len(k))):
		if k[i] == " " or k[i] == "'":
			u = m[i] 
		elif m[i] == " ":
			u = chr(ord(m[i]) + ord("A") - ord(k[i]) + 31)
		elif k[i] == "'" or k[i].isalpha() == False:
			u = chr(ord(m[i]) + ord("A") - ord(k[i]) + 25)
		else:
			u = chr(ord(m[i]) - ord(k[i]) + ord('A') -1)
		if u == "@" or u == "[" or u == "'":
			s += " "
		elif ord(u) < ord("A"):
		 	s += chr(ord(u) + 27)
		elif u.isalpha() == False:
			s += " "
		else:
			s += u
	return s