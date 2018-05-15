
if __name__=='__main__':
	print "This is the portal for Vigenere cipher."
	print "1. Press 1 for encryption"
	print "2. Press 2 for decryption"
	print "Enter your choice:"
	
	query=int(raw_input())

	print "Enter the text:"
	inp=raw_input()
	print "Enter the key:"
	key=raw_input()
	m=len(key)
	k=0
	
	out=""
	if query==1:
		for i in inp:
			if(ord(i)<=90):
				index=ord(i)+(ord(key[k%m])%65)
				if(index>90):
					index=index-90+64
			else:
				index=ord(i)+(ord(key[k%m])%97)
				if(index>122):
					index=index-122+96
			
			out+=chr(index)
			k+=1

		print "The encrypted text is:"
	elif query==2:
		for i in inp:
			index=ord(i)-(ord(key[k%m])%65)

			if(ord(i)<=90):
				index=ord(i)-(ord(key[k%m])%65)
				if(index<65):
					index=index-65+91
			else:
				index=ord(i)-(ord(key[k%m])%97)
				if(index<97):
					index=index-97+123

			out+=chr(index)
			k+=1

		print "The decrypted text is:"
	
	print out
