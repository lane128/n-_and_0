#coded by Wang Lei
#lane128@gmail.com

def Find5(n):
	z=n/5
	if n/5.0>=1.0:
		z=z+Find5(z)
		pass
	return z

if __name__ == '__main__':

	n=raw_input('input a postive int number:')
	if str.isdigit(n):
		n=int(n)
		if n>=0:
			zero=Find5(n)
			print "The {0}! result contains {1} '0' .".format(n,zero)
	else:
		print "Input Error!"
