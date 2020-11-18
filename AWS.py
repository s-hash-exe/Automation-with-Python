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