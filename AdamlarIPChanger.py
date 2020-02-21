#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# timer için
import sys
import time
import os

def Baslat():
		
	print "\nTorGhost baslatiliyor...\n"
		
	os.system("systemctl start tor")
	os.system("python torghost.py -s")
			
	sleepSecond = input("Saniye Girin?:")
			
	i=0
	while True:	
		i += 1
		print "IP tekrar degistiriliyor... Dongu: ", i
		os.system("python torghost.py -r")
		time.sleep(int(sleepSecond))

def Durdur():
	os.system("python torghost.py -x")
	os.system("systemctl stop tor")



print "AdamlarIPChanger'a Hosgeldiniz\n"

print "IP Adresiniz: "
os.system("curl http://icanhazip.com/")


print "\n"

islem = input("Islem Girin (Baslat=1, Durdur=2): ")

if islem == 1:
	Baslat()
elif islem == 2:
	Durdur()
else:
	print "Gecersiz islem"
