
def WS():
    
    import speech_recognition as sr
    import os 
    import pyttsx3 as py
    
    py.speak("Enter your remote IP Address.")
    ip = input("Enter your IP Address: ")
    
    print("\t\t\t Menu Card \n")
    py.speak("Here my Webserver menu is displayed.")
    py.speak("with the help of thid code you can install apache webserver.")
    print("Install webserver")
    py.speak("and also you can start the webservices.")
    print("Start services")
    py.speak("you can do autometically everything.")
    print("for everthing autometically")
    
    
    
    
    def ins():
    
    	os.system("ssh root@{} yum install httpd".format(ip))
    
    def st():
    	
    	os.system("ssh root@{} systemctl start httpd".format(ip))
    
    
    def tt():
    	
    	os.system("ssh root@{} yum install httpd ".format(ip))
    	os.system("ssh root@{} systemctl start httpd".format(ip))
    	os.system("ssh root@{} systemctl status httpd".format(ip))
    
    	print("\n\n\t\t\t Web Server successfully configure\n\n")
    
    
    while True:
    		py.speak("Tell me. What i do for you ?")
    		print("what i do for you ? : ")
    		r = sr.Recognizer() 
    		z = sr.Recognizer()
    		with sr.Microphone() as s:
      		  	py.speak("Start saying...")
      		  	print("start saying ....")
      		  	audio = r.listen(s)
      		  	py.speak("i got it...")
      		  	print(" i got it ...")
        
    		ipp = z.recognize_google(audio)

    		if ("install" in ipp) and ("webserver" in ipp):
    			ins()
    		elif ("start" in ipp) and ("service" in ipp):
    			st()
    		elif ("create" in ipp) and ("everything" in ipp):
    			tt() 
    		else:
    			exit()
    
WS()