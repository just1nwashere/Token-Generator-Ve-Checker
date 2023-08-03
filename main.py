import random
import string
import pathlib
import requests, os, threading, sys, time, random, ctypes, webbrowser,re, hashlib, datetime, os.path
import colorama
from colorama import Fore, init, Back, Style
from datetime import date

count = 0
current_path = os.path.dirname(os.path.realpath(__file__))
	
print(Fore.WHITE +Fore.GREEN +"\n[1] "+Fore.LIGHTWHITE_EX+"Token Generator")
print(Fore.WHITE +Fore.GREEN +"[2] "+Fore.LIGHTWHITE_EX+"Token Checker")
print(Fore.WHITE +Fore.GREEN +"[3] "+Fore.LIGHTWHITE_EX+"Bilgilendirme")
print(Fore.WHITE +Fore.GREEN +"[4] "+Fore.LIGHTWHITE_EX+"Çıkış")
opcion = input("\nSeçenecek Gir: ")
if opcion=='1':

	cantidad = input("\nKaç adet token üretmek istiyorsun?: ")
	while int(count)<int(cantidad):
		f= open(current_path +"/"+str("Tokenler")+str("")+".txt","a")
		f.write("\n")
		count+=1
		if int(count)==int(cantidad):
			print("\n" + Fore.CYAN +Fore.LIGHTRED_EX +"> Hataları çözmede yarrak çalıştırırsın :D")