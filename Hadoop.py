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
        Option 2: To Configurde datanode
        Option 3: To Configure Client
        Option 4: To Start namenode
        Option 5: To Stop namenode
        Option 6: To Start datanode
        Option 7: To Stop datanode
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
        elif ("exit" in cmd)and("quit" in cmd):
            print("""Are you sure?
            Say Yes to exit and No to continue.""")
            pt.speak("""Are you sure?
            Say yes to exit and No to continue.""")
            with sr.Microphone() as source2:
                pt.speak("Please start speaking your choice")
                print("Here you go...")
                audio2 = r.listen(source1)
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