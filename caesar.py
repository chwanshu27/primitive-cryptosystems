

if __name__=='__main__':
	print "This is the portal for Caesar cipher!"
	print "1. Press 1 for encryption"
	print "2. Press 2 for decryption"
	print "Enter your choice:"
	
	query=int(raw_input())

	print "Enter the text:"
	inp=raw_input()
	print "Enter the key:"
	key=int(raw_input())
	
	out=""
	if query==1:
		for i in inp:
			c=ord(i)+key
			if(c>90 and ord(i)<=90):
				c=c-90+64
			elif(c>122):
				c=c-122+96
			out+=chr(c)
		print "The encrypted text is:"
	elif query==2:
		for i in inp:
			c=ord(i)-key
			if(c<65):
				c=c-65+91
			elif(c<97 and ord(i)>=97):
				c=c-97+123
			out+=chr(c)
		print "The decrypted text is:"
	
	print out
