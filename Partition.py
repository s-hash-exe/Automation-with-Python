




# for partation 
def parti():
    import speech_recognition as sr
    import os
    import pyttsx3 as py
    
    py.speak("Enter your remote IP Address ?")
    ip = input("Enter Your IP Address (eg. 1.2.3.4) : ")
    
    py.speak("Do you want to make partition ? (yes or no)")
    print("Do you want to make partition: ")
    
    
    r = sr.Recognizer()
    with sr.Microphone() as s:
        py.speak("Start saying.....")
        print("start saying ....")
        audio = r.listen(s)
        py.speak("i got it...")
        print("i got it ...")

    
    p = r.recognize_google(audio)
    
    def info():
    	os.system("ssh root@{} fdisk -l".format(ip))
    
    def Mp():
    	
    	os.system("ssh root@{} df -h".format(ip))
    
    def cPar():
    	
    	info()
    	dk = input("Enter Disk name : ")
    	os.system("ssh root@{} fdisk {}".format(ip,dk))
    		
    
    def Driv():
    	
    	os.system("ssh root@{} udevadm settle".format(ip))
    
    def Fmt():
    	
    	info()
    	DDk = input("Enter partation name to format : ")
    	os.system("ssh root@{} mkfs.ext4 {} ".format(ip,DDk))
    
    def MnF():
    	
    	info()
    	dd = input("Enter new partation name you have created : ")
    	bb = input("enter Which folder/dir you want to mount ): ")
    	os.system("ssh root@{} mount {} {}".format(ip,dd,bb))
    	
    	
    
    if p == "yes":
    	print("\n\n\t\t = = = = = = = = = = = = = =")
    	py.speak("i can help you with the help of this menu.")
    	py.speak("i can display disk information.")
    	print(" To see disk information.")
    	py.speak("and also you can see how many mounted folder you have.")
    	print(" To see mounted partations.")
    	py.speak("i can create partition.")
    	print(" To create Partations.")
    	py.speak("with the help of my code you can give driver to new partition.")
    	print(" To Give Driver to Partations.")
    	py.speak("and also i can format partition. ")
    	print(" To format the Partations.")
    	py.speak("i can mount folder or directory to the partition.")
    	print(" To Mount folder/directory")
    	py.speak("and also i can create everthing for you in one saying.")
    	print(" To Create Everthing ")
    	py.speak("for exit or quit ")
    	print(" For Exit/Quit")
    	
    	while True:
    		py.speak("Tell me. What i do for you ?")
    		print("what i do for you ? : ")
    		z = sr.Recognizer()
    		with sr.Microphone() as s:
      		  	py.speak("Start saying...")
      		  	print("start saying ....")
      		  	audio = r.listen(s)
      		  	py.speak("i got it...")
      		  	print(" i got it ...")
        
    		inp = z.recognize_google(audio)
    		if ("display" in inp) and ("disk information" in inp):
    			info()
    		elif ("display" in inp) and ("mounted partition" in inp):
    			Mp()
    		elif ("create" in inp) and ("partition" in inp):
    			cPar()
    		elif ("give" in inp) and ("driver" in inp):
    			Driv()
    		elif ("format" in inp) and ("partition" in inp):
    			Fmt()
    		elif ("mount" in inp) and ("folder" in inp):
    			MnF()
    		elif ("create" in inp) and ("everything" in inp):
    			info()
    			print("\t\t\t======================\n\n")
    			Mp()
    			print("\t\t\t======================\n\n")
    			cPar()
    			print("\n\n\t\t\t==========Partation Created============\n\n")
    			Driv()
    			print("\n\n\t\t\t==========Driver Installed============\n\n")
    			Fmt()
    			print("\n\n\t\t\t==========Partation Formated============\n\n")
    			MnF()
    			print("\n\n\t\t\t==========Partation Successfully Created============\n\n")
    		elif ("exit" in inp) or ("quit" in inp):
    			exit()
    		else:
    			print("Your saying something wrong") 
    			break
    
    
    
    else:
    	print("Thankyou For using...\n good bye...")
    	exit()

parti()