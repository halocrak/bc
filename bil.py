import requests
import os
import sys
import time
import random
import time, os,sys
from time import sleep
ani = sys.platform
os.system('clear')
os.system('rm -rf email.txt')
E = '\033[1;97m'
A = '\033[1;91m'
Q = '\033[1;93m'
G = '\033[1;32m'
W = '\033[1;95m'
def ketik(s):
	for ASU in s + '\n':
		sys.stdout.write(ASU)
		sys.stdout.flush()
		sleep(10. / 10000)
def error():
	while True:
		print('')		
		print('خطا في لمعلومات')
		print('error !! ')
		
def logo():	
	ketik("""
                                 

telegram @i4m_mrx
--------------------------------------------------
""")
	ketik(' 	[ gmail / yahoo / hotmail ]')

	domen = input(G+'[✪]danayak halbzhera: @'+E)
	usr = 'zaqxswcdevfrbgtnhymjukilop'
	how = input(W+'\n[✪] chand dana bet  : '+E)
	how = int(how)
	
	hrf = input('\n[✪] chand pet bet : '+E)
	hrf = int(hrf)
	
	for email in range(how):
		email = ''
		for item in range(hrf):
			email = ''
		for item in range(hrf):
			email += random.choice(usr)
			x="12345678900987654321"
			x1=random.choice(x)
			x2=random.choice(x)
			x3=random.choice(x)
			x4=x1+x2+x3
		print (E+email+'@'+domen+'.com'+A+':'+Q+email+x4)
		with open('cc.txt', 'a') as x:
			x.write(email+'@'+domen+'.com:'+email+x4+'\n')
			
logo()

