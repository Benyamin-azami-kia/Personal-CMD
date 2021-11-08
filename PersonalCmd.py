import time
import os
import socket
import ctypes

''' A Simple Personal Cmd with a few Commands'''

def shtdown(tm=[]):

	#it shuts down your system (Be Careful)

	if tm==[]:
		#os.system("shutdown /s /t 0")
		print("shutdown")
	else:
		time.sleep(int(tm[0]))
		#os.system("shutdown /s /t 0")
		print("shutdown")

def opfile(d=[]):
	#you can open text files only
	if d==[]:
		print("You Should Enter Address after Command (For Example: opfile E:\\file.txt)\nTry Again.")
	else:
		dir=d[0]
		try:
			with open(dir) as file:
				content=file.read()
				print(content)
		except Exception:
			print("There Was an Error with Your Command!\nMaybe You Have Used an Invalid File Address\n"
			+"or Unsupported Files(This Virsion Supports Only Text Files!)")

def delf(d=[]):
	'''To Delete any Type Of file'''
	if d==[]:
		print("You Should Enter Address after Command (For Example: delf E:\\file.txt)\nTry Again.")
	else:
		dir=d[0]
		try:
			os.remove(dir)
			print("The File Has been Removed!")
		except Exception:
			print("There Was an Error with Your Command!\nMaybe You Have Used an Invalid File Address\n"
			+"or Unsupported Files(This Virsion Supports Only Text Files!)")


def hlp():
	print(
		'''
		############################################################################################################################################
										
										Welcom To My Personal CMD V 1.0

	*** List Of The Commands:


	1)shtdown s
	
		(This Command Will Shut Down Your Computer In 's' second
		The s Argument Is a Number and It is Optional.)

	2)opfile addr

		(You Can Open Text Files With This Command.
		The addr Argument Is The Address Of File)

	3)scnprt

		(A Simple Port Scanner)

	4)rstart s

		(This Command Will Restart Your Computer in 's' Second
		The s Argument Is a Number and It Is Optional.)
	
	5)sysinfo

		(It Shows Your System Informations and Has No Argument)
	
	6)userlist

		(List Of Users On Your Computer and Has No Argument (it just works on windows) )
	
	7)cbground addr

		(This Command Will Change Your Desktop Wallpaper, You Should Enter The Photo Address After Command (addr). (and it only works on Windows) )
	'''
	)

def scnprt():

	#a simple port scanner

	try:
		ip=input("Enter Your IP :")
		t_p=socket.gethostbyname(ip)
		print("starting scan ...")
		for port in range(1,5):
			sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			result=sock.connect((t_p,port))
			if result==0 :
				print ("Port "+port+" is open")
			sock.close()
	except Exception:
		print("Faild !!!")


def rstart(tm):

	#it restarts your system (Be Careful)

	if tm==[]:
		os.system("shutdown /r /t 0")
	else:
		time.sleep(int(tm[0]))
		os.system("shutdown /r /t 0")


def sysinfo():
	#it shows your system informations
	info=os.system("systeminfo")
	print(info)

def userlist():
	#List of users on your computer (it just works on windows)
	user=os.system("net user")
	print(user)

def sleep():
	os.system("rundll32.exe powerprof.dll, setsuspendstate 0,1,0")

def cbground():
	#this function will change your desktop wallpaper. and it only works on Windows
	try:
		adrr=input("Please Enter The File Address: ")
		ctypes.windll.user32.SystemParametersInfoW(20,0,adrr,0)
	except Exception:
		print("Faild! Maybe the file address is not valid")


#List of Commands with 1 or more Arguments(Keyswords and functions)
command1 = {"shtdwn" : shtdown, "opfile" : opfile,  "rstart":rstart, "delf":delf}

#List of Command with no Argument(Keyswords and functions)
command2={"hlp" : hlp, "scnprt":scnprt, "sysinfo":sysinfo, "userlist":userlist,
 		"sleep":sleep, "cbground":cbground}


while True:

	com, *t =input(">> ").split()
	comm=com.lower()

	if comm in command1.keys():
		command1[comm](t)

	elif comm in command2.keys() and not t:
		command2[comm]()

	else:
		print("Invalid Command!!!\nEnter hlp (Cmd Help)")
		continue
