# Menu card Using Python language !!



import os
import getpass as gt
import subprocess as sp
import pyttsx3 as pt
import speech_recognition as sr



#Header
print("\n")

#os.system("tput setaf 2")
print("==============================================================================")

#os.system("tput setaf 3")
print("\t\t\tWelcome to My world of Automation !!!")

#os.system("tput setaf 2")
print("==============================================================================")

pt.speak("""Welcome to My World of Automation.
I am Jarvis. I am here at your service.""")




print("")


# set password
pt.speak("Enter the password.")
PW = gt.getpass("Enter Password : ")
if PW != "rahul" :
    sp.getoutput("tput setaf 9")
    print("\n\nYour Entered Password is incorrect...")
    pt.speak("Entered Password is incorrect.")
    #os.system("tput setaf 4")
    #print("\nPlease contact Rahul Rathod ( Mobi- 9179561247 & Email - rr1818772@gmail.com )for login inside the menu.\n\n")
    print("==============================================================================\n")
    exit()




elif PW == "rahul":
    #Menu Card
    print()
    pt.speak("Here's your Main Menu Card.")
    #os.system("tput setaf 1")
    print("Basic Linux Commands")
    print("Hadoop Setup ")
    print("Linux Partitions")
    print("Docker Basic")
    print("Webserver Configuration")
    print("AWS Basics")
    print("-------------------------------------------------------------------------------")
    pt.speak("""Basic Linux Commands.
    Hadoop Setup.
    Linux Partitions.
    Docker Setup.
    Web Server Configuration.
    AWS Basics.""")
    

            # Looping  &  Choice's

    while True:
        print("\n= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
        pt.speak("Please select from the above option.")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Here you go.")
            pt.speak("Here you go.")
            audio = r.listen(source)
            print("Got it!")
            pt.speak("Got it.")
        cm = r.recognize_google(audio)
        cm = cm.lower()
        print(" = == = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = \n")
        if ("linux" in cm) and ("comm" in cm):
                    print("==============================================================================")
                    print("\n\t\t Welcome to Redhat 8 Linux ( Basic Commands ) !!\n")
                    pt.speak("Enter the remote IP")
                    ip = input("Enter remote IP : ")
                    print("""
            Option 1 : Run date command
            Option 2 : Run calendar command
            Option 3 : Check IP Address
            Option 4 : Display list of files and directories
            Option 5 : Create directories
            Option 6 : Remove directories
            Option 7 : Exit
            \n""")
                    pt.speak("""Check your system's date.
                    See the calendar.
                    Check your IP Address.
                    See the list of files and directories.
                    Create directories.
                    Remove directories.
                    Exit from the chosen option.""")
                    print("==============================================================================")
                    while True :
                        #os.system("tput setaf 5")
                        print("\n\t\t=======================================")
                        pt.speak("Please select from the above options.")
                        with sr.Microphone() as source:
                            print("Here you go.")
                            pt.speak("Here you go.")
                            audio = r.listen(source)
                            print("Got it!")
                            pt.speak("Got it.")
                        ch = r.recognize_google(audio)
                        ch = ch.lower()
                        print("\t\t=======================================\n")
                        if ("date" in ch):
                            #os.system("tput setaf 4")
                            sp.getoutput("ssh root@{} date".format(ip))
                        elif ("calendar" in ch):
                            #os.system("tput setaf 6")
                            os.system("ssh root@{} cal".format(ip))
                        elif ("address" in ch):
                            #os.system("tput setaf 7")
                            os.system("ssh root@{} ifconfig".format(ip))
                        elif ("file" in ch)and("directoty" in ch):
                            #os.system("tput setaf 8")
                            os.system("ssh root@{} ls".format(ip))
                        elif (("create" in ch)or("make" in ch))and("director" in ch) :
                            #os.system("tput setaf 2")
                            dn = input("Enter directory name : ")
                            os.system("ssh root@{} mkdir {}".format(ip, dn))
                            print("Successfully created directory " +dn)
                        elif ("remove" in ch)and("directo" in ch): 
                            #os.system("tput setaf 9")
                            os.system("ssh root@{} rm -rf {}".format(ip, rdn))
                            print("Successfully removed directory " +rdn)
                        elif ("exit" in ch) or ("quit" in ch):
                            #os.system("tput setaf 10")
                            pt.speak("Terminating.")
                            print("Terminating...")
                            print("\n------------------------------------------------------------------------------\n")
                            break
                        else:
                            #os.system("tput setaf 1")
                            pt.speak("Please select a valid option")
                            print("Please Enter valid choice !!!")

        elif ("hadoop" in cm):
                    print("==============================================================================")
                    print("\n\t\t Welcome to Hadoop Setup !!\n")
                    #hadoop configuration [ namenode , datanode , client ] 

                    #hadoop configuration [ namenode , datanode , client ] 

                    def hadoop_all():
                        import os
                        import subprocess as sp
                        import speech_recognition as sr
                        import pyttsx3 as pt

                        def instll():
                            pt.speak("Enter directory name where java and hadoop file resides")
                            dir = input("Enter directory name where java and hadoop file resides : ")
                            print(dir)
                            sp.getoutput("ssh root@{} rpm -i {}/jdk-8u171-linux-x64.rpm".format(St_ip,dir))
                            sp.getoutput("ssh root@{} rpm -i {}\/hadoop-1.2.1-1.86_64.rpm --force".format(St_ip,dir))

                        def stn():
                                a = sp.getstatusoutput("ssh root@{} hadoop namenode -format".format(St_ip))
                                if a[0]!=1:
                                    pt.speak("Some error occured.")
                                    print("Some error occured.")
                                else:
                                    sp.getoutput("ssh root@{} hadoop-daemon.sh start namenode".format(St_ip))
                                    sp.getoutput("ssh root@{} jps".format(St_ip))
                                    sp.getoutput("ssh root@{} hadoop dfsadmin -report".format(St_ip))

                        def stpn():
                                a = sp.getstatusoutput("ssh root@{} hadoop-daemon.sh stop namenode".format(St_ip))
                                if a[0]!=0:
                                    print("Some error occured.")
                                    pt.speak("Some error occured.")
                                else:
                                    sp.getoutput("ssh root@{} jps".format(St_ip))

                        def std():
                                a = sp.getstatusoutput("ssh root@{} hadoop-daemon.sh start datanode".format(St_ip))
                                if a[0]!=0:
                                    print("Some error occured.")
                                    pt.speak("Some error occured.")
                                else:
                                    sp.getoutput("ssh root@{} jps".format(St_ip))
                                    sp.getoutput("ssh root@{} hadoop dfsadmin -report".format(St_ip))

                        def stpd():
                                a = sp.getstatusoutput("ssh root@{} hadoop-daemon.sh stop datanode".format(St_ip))
                                if a!=0:
                                    print("Some error occured.")
                                    pt.speak("Some error occured.")
                                else:
                                    sp.getoutput("ssh root@{} jps".format(St_ip))


                        pt.speak("Enter the remote IP")
                        St_ip = input("Enter remote IP : ")
                        while True :
                            pt.speak("Here is your Hadoop Menu Card")
                            print(''' \t\t\t Select Option:
                            Option 1: To configure Namenode
                            Option 2: To Configurde Datanode
                            Option 3: To Configure Client
                            Option 4: To Start Namenode
                            Option 5: To Stop Namenode
                            Option 6: To Start Datanode
                            Option 7: To Stop Datanode
                            Option 8: To Exit
                        ''')
                            pt.speak("""Configure NameNode.
                            Configurde DataNode.
                            Configure Client Node.
                            Start namenode.
                            Stop namenode.
                            Start datanode.
                            Stop datanode.
                            Exit.""")
                            pt.speak("Please command me from the above menu.")
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                print("Start speaking your choice.")
                                pt.speak("Start speaking your choice.")
                                audio = r.listen(source)
                                print("Got it...")
                                pt.speak("Got it.")
                            cmd = r.recognize_google(audio)
                            cmd = cmd.lower()

                            if ("configure" in cmd)and("name" in cmd):
                                def namenode():
                                    instll()
                                    pt.speak("Provide the details about namenode")
                                    print("\t\t\tProvide the details about namenode:")
                                    pt.speak("Provide IP at which you want to configure namenode")
                                    namenode_IP = input("\t\t\tProvide IP at which you want to configure namenode:")
                                    pt.speak("Provide the Folder name for Namenode")
                                    namenode_folder = input("\t\t\tProvide the Folder name for Namenode:")
                                    sp.getoutput("ssh root@{} rm -rf {}".format(St_ip,namenode_folder))#firstly removing if created 
                                    sp.getoutput("ssh root@{} mkdir {}".format(St_ip,namenode_folder))#creating folder
                                    pt.speak("Provide Port Number at which you want to run namenode service")
                                    namenode_port = input("\t\t\tProvide Port Number at which you want to run namenode service:")
                                    file_hdfs_nn = open("/etc/hadoop/hdfs-site.xml","w")#opening the hdfs file to configure 
                                    #hdfs data
                                    hdfs_data_nn =  '''<?xml version="1.0"?>                                            
                                <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

                                <!-- Put site-specific property overrides in this file. -->
                                <configuration>
                                <property>
                                <name>dfs.name.dir</name>
                                <value>{}</value>
                                </property>
                                </configuration>\n'''.format(namenode_folder)
                                    file_hdfs_nn.write(hdfs_data_nn) #writing in data

                                    file_core_nn = open("/etc/hadoop/core-site.xml", "w")
                                    #core file data
                                    core_data_nn = '''<?xml version="1.0"?>
                                <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
                                <!-- Put site-specific property overrides in this file. -->
                                <configuration>
                                <property>
                                <name>fs.default.name</name>
                                <value>hdfs://{}:{}</value>
                                </property>
                                </configuration>\n'''.format(namenode_IP,namenode_port)
                                    file_core_nn.write(core_data_nn)   

                                namenode()




                            elif ("configure" in cmd)and("data" in cmd):
                                def datanode():
                                    instll()
                                    pt.speak("Provide the Folder name for datanode.")
                                    datanode_folder = input("\t\t\tFolder name for datanode:")
                                    sp.getoutput("ssh root@{} rm -rf {}".format(St_ip,datanode_folder))
                                    sp.getoutput("ssh root@{} mkdir {}".format(St_ip,datanode_folder))
                                    pt.speak("Provide namenode IP.")
                                    namenode_IP = input("\t\t\tProvide namenode IP: ")
                                    pt.speak("Provide port number of namenode.")
                                    namenode_port = input("\t\t\tProvide port number of namenode: ")
                                    file_hdfs_dn = open("/etc/hadoop/hdfs-site.xml","w")#opening hdfs-site.xml file
                                     #data of hdfs of datanode
                                    hdfs_data_dn =  '''<?xml version="1.0"?>
                                <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

                                <!-- Put site-specific property overrides in this file. -->
                                <configuration>
                                <property>
                                <name>dfs.data.dir</name>
                                <value>{}</value>
                                </property>
                                </configuration>\n'''.format(datanode_folder)
                                    file_hdfs_dn.write(hdfs_data_dn) #writing the data

                                    file_core_dn = open("/etc/hadoop/core-site.xml", "w")#opening core-site.xml file
                                    core_data_dn = '''<?xml version="1.0"?>
                                <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
                                <!-- Put site-specific property overrides in this file. -->
                                <configuration>
                                <property>
                                <name>fs.default.name</name>
                                <value>hdfs://{}:{}</value>
                                </property>
                                </configuration>\n'''.format(namenode_IP,namenode_port)
                                    file_core_dn.write(core_data_dn)   
                                datanode()


                            elif ("configure" in cmd)and("client" in cmd): 
                                def client():
                                    instll()
                                    pt.speak("Provide namenode IP.")
                                    namenode_IP = input("\t\t\tProvide namenode IP: ")
                                    pt.speak("Provide port number of namenode.")
                                    namenode_port = input("\t\t\tProvide port number of namenode: ")
                                    print(''' \t\t\t Select Option:
                                        Option1: Do you Want Change both replication factor and block size
                                        Option2: Do you Want to Change only replication_factor
                                        Option3: Do you Want to Change only block size
                                        Option4: Don't Want to do anything.
                                    ''')
                                    pt.speak("""Do you Want Change both replication factor and block size.
                                        Do you Want to Change only replication_factor.
                                        Do you Want to Change only block size.
                                        Don't Want to do anything.""")
                                    pt.speak("Please command me from the above options.")

                                    with sr.Microphone() as source1:
                                        pt.speak("Please start speaking your choice")
                                        print("Here you go...")
                                        audio1 = r.listen(source1)
                                        print("Got it...")
                                        pt.speak("Got it.")

                                    opt = r.recognize_google(audio1)

                                    if ("change" in opt)and("replica" in opt)and("factor" in opt)and("block" in opt)and("size" in opt):
                                        pt.speak("Enter the replication factor.")
                                        replication_size=int(input("Enter replication_factor:"))
                                        pt.speak("Enter the block size in bytes.")
                                        block_size=int(input("Enter block size in bytes:"))
                                        file_hdfs_cn = open("/etc/hadoop/hdfs-site.xml","w")
                                        hdfs_data_cn =  '''<?xml version="1.0"?>
                                <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

                                <!-- Put site-specific property overrides in this file. -->
                                <configuration>
                                <property>
                                <name>dfs.replication</name>
                                <value>{}</value>
                                </property>
                                <property>
                                <name>dfs.block.size</name>
                                <value>{}</value>
                                </property>
                                </configuration>\n'''.format(replication_size,block_size)
                                        file_hdfs_cn.write(hdfs_data_cn)

                                    elif ("change" in opt)and("replication" in opt):
                                        pt.speak("Enter the replication factor.")
                                        replication_factor=int(input("Enter replication_factor:"))
                                        file_hdfs_cn = open("/etc/hadoop/hdfs-site.xml","w")
                                        hdfs_data_cn =  '''<?xml version="1.0"?>
                                <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

                                <!-- Put site-specific property overrides in this file. -->
                                <configuration>
                                <property>
                                <name>dfs.replication</name>
                                <value>{}</value>
                                </property>
                                </configuration>\n\n'''.format(replication_factor)
                                        file_hdfs_cn.write(hdfs_data_cn)

                                    elif ("change" in opt)and("block" in opt)and("size" in opt):
                                        pt.speak("Enter the block size in bytes.")
                                        block_size=int(input("Enter block size in bytes:"))
                                        file_hdfs_cn = open("/etc/hadoop/hdfs-site.xml","w")
                                        hdfs_data_cn =  '''<?xml version="1.0"?>
                                <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

                                <!-- Put site-specific property overrides in this file. -->
                                <configuration>
                                <property>
                                <name>dfs.block.size</name>
                                <value>{}</value>
                                </property>
                                </configuration>\n'''.format(block_size)
                                        file_hdfs_cn.write(hdfs_data_cn)

                                    else:
                                        file_hdfs_cn = open("/etc/hadoop/hdfs-site.xml","w")
                                        hdfs_data_cn =  '''<?xml version="1.0"?>
                                <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

                                <!-- Put site-specific property overrides in this file. -->
                                <configuration>
                                </configuration>\n'''
                                        file_hdfs_cn.write(hdfs_data_cn)


                                    file_core_cn = open("/etc/hadoop/core-site.xml", "w")
                                    core_data_cn = '''<?xml version="1.0"?>
                                <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
                                <!-- Put site-specific property overrides in this file. -->
                                <configuration>
                                <property>
                                <name>fs.default.name</name>
                                <value>hdfs://{}:{}</value>
                                </property>
                                </configuration>\n'''.format(namenode_IP,namenode_port)
                                    file_core_cn.write(core_data_cn)   
                                client()

                            elif ("start" in cmd)and("name" in cmd)and("node" in cmd):
                                stn()

                            elif ("stop" in cmd)and("name" in cmd)and("node" in cmd):
                                stpn()

                            elif ("start" in cmd)and("data" in cmd)and("node" in cmd):
                                std()

                            elif ("stop" in cmd)and("data" in cmd)and("node" in cmd):
                                stpd()
                            elif ("exit" in cmd)or("quit" in cmd):
                                print("""Are you sure?
                                Say Yes to exit and No to continue.""")
                                pt.speak("""Are you sure?
                                Say yes to exit and No to continue.""")
                                with sr.Microphone() as source2:
                                    pt.speak("Please start speaking your choice")
                                    print("Here you go...")
                                    audio2 = r.listen(source2)
                                    print("Got it...")
                                    pt.speak("Got it.")

                                yn = r.recognize_google(audio2)
                                yn = yn.lower()
                                if ("yes" in yn):
                                    break
                            else:
                                pt.speak("Please enter a valid choice.")
                                print("Please enter a valid choice.")
                            sp.getoutput("tput setaf 6")
                            pt.speak("Press enter to continue.")
                            inp = input("Press Enter to continue")
                            sp.getoutput("tput setaf 7")
                            sp.getoutput("clear")

                    hadoop_all()


        elif ("partition" in cm) or ("Partition" in cm):
                    print("==============================================================================")
                    print("\n\t\t Welcome to Linux Partitions !!\n")
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
                                    break
                                else:
                                    print("Your saying something wrong") 
                                    break



                        else:
                            print("Thankyou For using...\n good bye...")
                            exit()

                    parti()


        elif ("Docker" in cm) or ("docker" in cm):
                    print("==============================================================================")
                    print("\n\t\t Welcome to Docker Setup !!\n")



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
                                                        break
                                                    else:
                                                        py.speak("Not supported ")
                                                        print("not supported")
                                                        break


                    Dock()




        elif ("webserver" in cm) or ("server" in cm):
                    print("==============================================================================")
                    print("\n\t\t Welcome to Apache Web Server Setup !!\n")  



                    def WS():

                        import speech_recognition as sr
                        import os 
                        import pyttsx3 as py

                        py.speak("Enter your remote IP Address.")
                        ip = input("Enter your IP Address: ")
                        pt.speak("Here's the Web Server Menu Card.")
                        
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
                                    break

                    WS()


        elif("AWS" in cm) or ("aws" in  cm) or ("a w s" in cm) or ("a ws" in cm) or ("aw s" in cm):
            print("==============================================================================")
            print("\n\t\t Welcome to AWS Setup !!\n")
            def aws():
                import os
                import subprocess as sp
                import speech_recognition as sr
                import pyttsx3 as pt

                pt.speak("Enter your remote IP Address ?")
                ip = input("Enter Your IP Address (eg. 1.2.3.4) : ")

                def menu():
                    print("Install AWS CLI")
                    print("Check AWS version")
                    print("Create a new Key Pair")
                    print("Display all existing Keys")
                    print("Create a new Security Group")
                    print("Add new inbound rules to a Security Group")
                    print("Launch a new EC2 Instance")
                    print("Display existing EC2 Instances")
                    print("Start an existing EC2 Instance")
                    print("Stop a running EC2 Instance")
                    print("Terminate an EC2 Instance")
                    print("Create an EBS Volume")
                    print("Attach an EBS VOlume to an EC2 Instance")
                    print("Detach an EBS Volume from an EC2 Instance")
                    print("Create a new S3 Bucket")
                    print("Copy files to S3 Bucket")
                    print("Create a CloudFront Distribution")
                    print("Remotely login to an EC2 Instance")
                    print("Create a Snapshot")
                    print("Restore a snapshot")
                    print("EXIT")
                    pt.speak("Here's your AWS Menu Card. How can I help you ?")
                    pt.speak("""Installing AWS CLI.
                    Check AWS version.
                    Create a new Key Pair.
                    Cisplay all existing Keys.
                    Create a new Security Group.
                    Add new inbound rules to a Security Group.
                    Launch a new EC2 Instance.
                    Display existing EC2 Instances.
                    Start an existing EC2 Instance.
                    Stop a running EC2 Instance.
                    Terminate an EC2 Instance.
                    Create an EBS Volume.
                    Attach an EBS VOlume to an EC2 Instance.
                    Detach an EBS Volume from an EC2 Instance.
                    Create a new S3 Bucket.
                    Copy files to S3 Bucket.
                    Create a CloudFront Distribution.        
                    Remotely login to an EC2 Instance.
                    Create a Snapshot.
                    Restore a snapshot.
                    EXIT.""")

                def version():
                    #a = os.system("aws --version 2>> ttt.txt")
                    a = sp.getstatusoutput("ssh root@{} aws --version".format(ip))
                    if a[0]!=0 :
                        print("Please install AWS CLI first.")
                        pt.speak("Please install AWS CLI first.")
                    else:
                        print(a[1])

                def install():
                    #a = os.system("aws --version | grep 2.0")
                    a = sp.getstatusoutput("ssh root@{} aws --version".format(ip))
                    if a[0] != 0 :
                        sp.getoutput('ssh root@{} curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"'.format(ip))
                    #a = os.system("rpm -q unzip | grep xyz")
                    b = sp.getstatusoutput("ssh root@{} rpm -q unzip".format(ip))
                    if b[0] !=0 : 
                        sp.getoutput("ssh root@{} yum install unzip -y".format(ip))
                    sp.getoutput(" ssh root@{} unzip awscliv2.zip".format(ip))
                    sp.getoutput("ssh root@{} sudo ./aws/install".format(ip))

                def createKey():
                    pt.speak("Please enter the required details.")
                    keyn = input("Enter the key name: ")
                    #a = os.system("aws ec2 create-key-pair --key-name {0} > {0}.pem".format(keyn))
                    a = sp.getstatusoutput("ssh root@{} aws ec2 create-key-pair --key-name {0} > {0}.pem".format(ip, keyn))
                    if a[0]==0:
                        sp.getoutput("tput setaf 6")
                        print("Key successfully created")
                        pt.speak("Key successfully created")

                def displayKey():
                    sp.getoutput("ssh root@{} aws ec2 describe-key-pairs".format(ip))

                def createSecurityGroup():
                    pt.speak("Please enter the required details.")
                    name = input("Enter the name of new security group: ")
                    des = input("Enter the security group description: ")
                    sp.getoutput("ssh root@{} aws ec2-create-security-group --group-name {} --description {}".format(ip, name, des))

                def addBounds():
                    pt.speak("Please enter the required details.")
                    name = input("Enter the security group name: ")
                    protocol = input("Enter the protocol: ")
                    port = input("Enter the port number: ")
                    cidr = input("Enter the cidr block: ")
                    a = sp.getstatusoutput("ssh root@{} aws ec2 authorize-security-group-ingress --group-name {} --protocol {} --port {} --cidr {} 2>> ttt.txt".format(ip, name,protocol,port,cidr))
                    if a[0]!=0 :
                        print("Enter valid details")
                    else:
                        sp.getoutput("tput setaf 6")
                        print("Inbound Rules successfully added")
                        sp.getoutput("tput setaf 7")

                def newInstance():
                    pt.speak("Please enter the required details.")
                    ami = input("Enter the AMI id: ")
                    type = input("Enter the instance type: ")
                    count = input("Enter the number of instances to be launched: ")
                    subid = input("Enter the subnet id: ")
                    secname = input("Enter the security group ID: ")
                    key = input("Enter the key name: ")
                    a = sp.getstatusoutput("ssh root@{} aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id {} --security-group-ids {} --key-name {} 2>> ttt.txt".format(ip, ami, type, count, subid, secname, key))
                    if a[0]!= 0 :
                        print("Enter the valid details")


                def displayInstance():
                    sp.getoutput("aws ec2 describe-instances")

                def startInstance():
                    pt.speak("Please enter the required details.")
                    id = input("Enter the Instance ID to be launced: ")
                    a = sp.getstatusoutput("ssh root@{} aws ec2 start-instances --instance-ids {} 2>> ttt.txt".format(ip, id))
                    if a[0]!=0:
                        print("Enter the valid details")

                def stopInstance():
                    pt.speak("Please enter the required details.")
                    id = input("Enter the id of instance to be stopped: ")
                    a = sp.getstatusoutput("ssh root@{} aws ec2 stop-instances --instance-ids {} 2>> ttt.txt".format(ip, id))
                    if a[0]!=0 :
                        print("Enter a valid running instance id")

                def terminateInstance():
                    pt.speak("WARNING: Terminating an instance would result in loss of all data.")
                    print("WARNING: Terminating an instance would result in loss of all data")
                    pt.speak("Press 1 to continue with the process.")
                    inp = input("Press 1 to continue with the process: ")
                    if inp==1:
                        id = input("Enter id of instance to be terminated: ")
                        a = sp.getstatusoutput("ssh root@{} aws ec2 terminate-instances --instance-ids {} 2>> ttt.txt".format(ip, id))
                        if a[0]!=0 :
                            print("Enter a valid ID")


                def createVolume():
                    pt.speak("Please enter the required details.")
                    type = input("Enter the volume type: ")
                    size = input("Enter the volume size: ")
                    az = input("Enter the availibilty zone: ")
                    a = sp.getstatusoutput("ssh root@{} aws ec2 create-volume --volume-type {} --size {} --availability-zone {} 2>> ttt.txt".format(ip, type, size, az))
                    if a[0]!=0 :
                        print("Enter valid details")


                def attachVolume():
                    pt.speak("Please enter the required details.")
                    id = input("Enter volume id: ")
                    insid = input("Enter Instance ID: ")
                    dev = input("Enter device name: ")
                    a = sp.getstatusoutput("ssh root@{} aws ec2 attach-volume --instance-id  {} --volume-id {} --device {} 2>> ttt.txt".format(ip, insid, id, dev))
                    if a[0]!=0 :
                        print("Enter valid details")

                def detachVolume():
                    pt.speak("Please enter the required details.")
                    id = input("Enter volume id: ")
                    a = sp.getstatusoutput("ssh root@{} aws ec2 detach-volume --volume-id {} 2>> ttt.txt".format(ip, id))
                    if a[0]!=0 :
                        print("Enter valid Volume ID")


                def createBucket():
                    pt.speak("Please enter the required details.")
                    name = input("Enter the Bucket Name: ")
                    access = input("Enter the access permission: ")
                    lc = input("Enter the Location Constraint: ")
                    a = sp.getstatusoutput("ssh root@{} aws s3api create-bucket --bucket {} --ac {} --create-bucket-configuration LocationConstraint={} 2>> ttt.txt".format(ip, name, access, lc))
                    if a[0]!=0 :
                        print("Enter valid details")

                def cpBucket():
                    pt.speak("Please enter the required details.")
                    path = input("Enter the complete path of file to be copied in bucket: ")
                    name = input("Enter the bucket name: ")
                    per = input("Enter the permission: ")
                    a = sp.getstatusoutput("ssh root@{} aws s3 cp {} s3://{} --acl {} 2>> ttt.txt".format(ip, path, name, per))
                    if a[0]!=0 :
                        print("Enter valid details")

                def createCloudfront():
                    pt.speak("Please enter the required details.")
                    id = input("Enter the origin domain name: ")
                    a = sp.getstatusoutput("ssh root@{} aws cloudfront create-distribution --origin-domain-name {} 2>> ttt.txt".format(ip, id))
                    if a[0]!=0 :
                        print("Enter a valid origin name")

                def loginInstance():
                    pt.speak("Please enter the required details.")
                    ip = input("Enter the public ip of the Instance: ")
                    name = input("Enter the full path of key: ")
                    a = sp.getstatusoutput("ssh -i {} ec2-user@{} 2>> ttt.txt".format(name, ip))
                    if a[0]!=0 :
                        print("Enter valid details")

                def createSnapshot():
                    pt.speak("Please enter the required details.")
                    id = input("Enter the volume id: ")
                    des = input("Enter the description")
                    a = sp.getstatusoutput("ssh root@{} aws ec2 create-snapshot --volume-id {} --description {} 2>> ttt.txt".format(ip, id, des))
                    if a[0]!=0 :
                        print("Enter the valid details")

                def restoreSnapshot():
                    pt.speak("Please enter the required details.")
                    id = input("Enter the snapshot ID: ")
                    a = sp.getstatusoutput("ssh root@{} aws restore-from-snapshot --snapshot-id {} 2>> ttt.txt".format(ip, id))
                    if a[0]!=0 :
                        print("Enter valid snapshot ID")
                while True:
                    sp.getoutput("tput setaf 6")
                    menu()
                    sp.getoutput("tput setaf 7")
                    print("\n")
                    r=sr.Recognizer()
                    with sr.Microphone() as source:
                        print("From the menu, Please command me!")
                        audio = r.listen(source)
                        print("Got it...")
                    cmd = r.recognize_google(audio)
                    cmd=cmd.lower()
                    if ("install" in cmd)and("aws" in cmd):
                        install()
                    elif ("aws" in cmd)and("version" in cmd):
                        version()
                    elif ("create" in cmd)and("key" in cmd):
                        createKey()
                    elif ("display" in cmd)and("key" in cmd):
                        displayKey()
                    elif ("create" in cmd)and(("security" in cmd)or(" sg " in cmd)):
                        createSecurityGroup()
                    elif (("inbound" in cmd)or("ingress" in cmd)or("rules" in cmd)):
                        addBounds()
                    elif (("create" in cmd)or("launch" in cmd))and("new" in cmd)and("instance" in cmd):
                        newInstance()
                    elif ("display" in cmd)and("instance" in cmd):
                        displayInstance()
                    elif ("start" in cmd)and("instance" in cmd):
                        startInstance()
                    elif ("stop" in cmd)and("instance" in cmd):
                        stopInstance()
                    elif ("terminate" in cmd)and("instance" in cmd):
                        terminateInstance()
                    elif ("create" in cmd)and("volume" in cmd):
                        createVolume()
                    elif ("attach" in cmd)and("volume" in cmd):
                        attachVolume()
                    elif ("detach" in cmd)and("volume" in cmd):
                        detachVolume()
                    elif ("create" in cmd)and("bucket" in cmd):
                        createBucket()
                    elif ("copy" in cmd)and("bucket" in cmd):
                        cpBucket()
                    elif ("create" in cmd)and("cloud" in cmd)and("front" in cmd):
                        createCloudfront()
                    elif ("login" in cmd)and("instance" in cmd):
                        loginInstance()
                    elif (("create" in cmd)or("make" in cmd))and("snapshot" in cmd):
                        createSnapshot()
                    elif ("restore" in cmd)and("snapshot" in cmd):
                        restoreSnapshot()
                    elif ("exit" in cmd)or("quit" in cmd):
                        sp.getoutput("tput setaf 1")
                        pt.speak("Do you want to exit?")
                        print("Do you want to EXIT ?")
                        sp.getoutput("tput setaf 7")
                        pt.speak("Press Y to exit and N to continue")
                        ch = input("Press Y to exit and N to continue: ")
                        if ch=='y' or ch=='Y':
                            pt.speak("Terminating the program.")
                            print("Terminating...")
                            break
                    else:
                        print("Enter a valid choice")
                    sp.getoutput("tput setaf 6")
                    pt.speak("Press enter to continue.")
                    inp = input("Press Enter to continue")
                    sp.getoutput("tput setaf 7")
                    sp.getoutput("clear")
            aws()



        elif ("exit" in cm):
                    print("Thank You !!! Have a nice day")
                    exit()
