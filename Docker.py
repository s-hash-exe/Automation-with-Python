#docker lounch

def Dock():


                            import os
                            import speech_recognition as sr
                            import pyttsx3 as py

                            print("\n\n\t\t\t======= Welcome to My World =======\n\n")
                            py.speak("I want to install docker")
                            print("docker is installed")
                            py.speak("i want to install the container")
                            print("container installed")
                            py.speak("i want to Run the container")
                            print("container is running")
                            py.speak("can you please open all the container Images")
                            py.speak("To start again the container")
                            print("container started")
                            py.speak("Can you show me how many Container are Launched")
                            py.speak("exit")
                            print("exit")

                            py.speak("Enter your remote IP Address.")
                            ip = input("Enter the IP Address (eg. 1.2.3.4 ) : ")


                            def LND():
                                os.system("ssh root@{} yum install docker".format(ip))
                                print("\n\n\t\t\t======Docker Installed=======\n")

                            def Ctos():
                                cn = input("tell me which contener/OS you want to lounch : ")
                                os.system("ssh root@{} docker pull {}".format(ip,cn))
                                print("\n\n\t\t\t======Contener Installed=======\n\n")

                            def run():
                                cnn = ("Enter contener-image-name and version (eg. centos:latest ): ")
                                nm = input("Enter the name as you want to give the contener : ")
                                os.system("ssh root@{} docker run -it --name {} {}".format(ip,nm,cnn))

                            def img():
                                os.system("ssh root@{} docker images".format(ip))

                            def attch():
                                Nd = input("Enter contener name you want to start again : ")
                                os.system("ssh root@{} docker start {} ".format(ip,Nd))
                                os.system("ssh root@{} docker attach {}".format(ip,Nd))


                            while True:


                                r = sr.Recognizer()
                                with sr.Microphone() as s:
                                    py.speak("Start saying.....")
                                    print("start saying ....")
                                    audio = r.listen(s)
                                    py.speak("i got it...")
                                    print("i got it ...")


                                inp = r.recognize_google(audio)
                                if("install" in inp) and ("docker" in inp):
                                    LND()
                                elif ("install" in inp) and ("container" in inp):
                                    Ctos()
                                elif ("run" in inp) and ("container" in inp):
                                    run()
                                elif ("open" in inp) and ("images" in inp):
                                    img()
                                elif ("start" in inp) and ("container" in inp):
                                    attch()

                                elif ("show" in inp) and ("images" in inp) and ("container" in inp):
                                    os.system("ssh {} docker ps -a".format(ip))
                                    print("\n\t\t\t========================================\n")
                                    LND()
                                    print("\n\t\t\t========================================\n")
                                    print("\n\t\t\t========================================\n")
                                    Ctos()
                                    print("\n\t\t\t========================================\n")
                                    print("\n\t\t\t========================================\n")
                                    run()
                                    print("\n\t\t\t========================================\n")
                                    print("\n\t\t\t========================================\n")
                                    img()
                                    print("\n\t\t\t========================================\n")
                                    print("\t\t\t========================================\n")
                                    attch()
                                    print("\t\t\t========================================\n")

                                elif("exit" in inp):
                                    exit()
                                else:
                                    py.speak("Not supported ")
                                    print("not supported")
                                    break


Dock()
