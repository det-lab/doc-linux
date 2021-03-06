#Written generically; will be translated into a particular language (likely python) once I've an outline.

#Set variables to 0 ("False")
ssh = 0
known = 0
gen = 0
perms = 0
key = 0
config = 0

#Possible Commands
ssh22 = {'ssh guest@specific-computer.cluster.domain.edu', 
    'ssh -p 22 guest@specific-computer.cluster.domain.edu'}
ssh26 = {'ssh -p 26 guest@specific-computer.cluster.domain.edu'}
sshcf = {'ssh comp'}
y = {'yes'}
n = {'no'}
q = {'exit',
    'logout'}
ls = {'ls'}
lsa = {'ls -a'}
lssh = {'ls .ssh'}
#cd is below to allow variation.
keygen = {'ssh-keygen -t rsa'}
epub = {'vi .ssh/id_rsa.pub',
    'vim .ssh/id_rsa.pub',
    'nano .ssh/id_rsa.pub',
    'vi ~/.ssh/id_rsa.pub',
    'vim ~/.ssh/id_rsa.pub',
    'nano ~/.ssh/id_rsa.pub',
    'vi /home/user/.ssh/id_rsa.pub',
    'vim /home/user/.ssh/id_rsa.pub',
    'nano /home/user/.ssh/id_rsa.pub'}
rpub = {'more .ssh/id_rsa.pub',
    'less .ssh/id_rsa.pub',
    'cat .ssh/id_rsa.pub',
    'more ~/.ssh/id_rsa.pub',
    'less ~/.ssh/id_rsa.pub',
    'cat .ssh/id_rsa.pub',
    'more /home/user/.ssh/id_rsa.pub',
    'less /home/user/.ssh/id_rsa.pub',
    'cat /home/user/.ssh/id_rsa.pub'}
ckey = {'ssh-rsa aB123 user@local'}
rpv = {'less .ssh/id_rsa',
    'more .ssh/id_rsa',
    'cat .ssh/id_rsa',
    'less ~/.ssh/id_rsa',
    'more ~/.ssh/id_rsa',
    'cat ~/.ssh/id_rsa',
    'less /home/user/.ssh/id_rsa',
    'more /home/user/.ssh/id_rsa',
    'cat /home/user/.ssh/id_rsa'}
epv = {'nano .ssh/id_rsa',
    'vi .ssh/id_rsa',
    'vim .ssh/id_rsa'}
auth = {'nano .ssh/authorized_keys',
    'vi .ssh/authorized_keys',
    'vim .ssh/authorized_keys',
    'nano ~/.ssh/authorized_keys',
    'vi ~/.ssh/authorized_keys',
    'vim ~/.ssh/authorized_keys',
    'nano /home/guest/.ssh/authorized_keys',
    'vi /home/guest/.ssh/authorized_keys',
    'vim /home/guest/.ssh/authorized_keys'}
fig = {'nano .ssh/config',
    'vi .ssh/config',
    'vim .ssh/config',
    'nano ~/.ssh/config',
    'vi ~/.ssh/config',
    'vim ~/.ssh/config',
    'nano /home/user/.ssh/config',
    'vi /home/user/.ssh/config',
    'vim /home/user/.ssh/config'}
cfig = {'Host comp HostName specific-computer.cluster.domain.edu User guest Port 22 IdentityFile /home/user/.ssh/id_rsa'}
chmod = {'chmod 600 ~/.ssh/config',
    'chmod 600 /home/user/.ssh/config',
    'chmod 600 .ssh/config'}

#Taking commands.
print()
print("Welcome to the ssh tutorial script!")
print("Please see 'connecting.adoc' for instructions.")
print()
print("============================")
print()
print("The following aliases are used:")
print()
print("'ls' functions as 'ls 1'")
print("'less' and 'more' will function as 'cat'.")
print("All text editors will be generic.")
print()
print("============================")
print()
stop = 0
while stop == 0: #Indefinitely long loop
    if ssh == 0:
        prompt = input('user@local:~$ ') #Initial prompt
    elif ssh == 1:
        prompt = input('guest@specific-computer.cluster.domain.edu~$ ') #ssh'd prompt

    #Commands

    if prompt in ssh22:
        if ssh == 1:
            print("There is a time and a place for everything! But not now.")
            print("[TUTORIAL ERROR: You're already connected!]")
        elif ssh == 0:
            if key == 1:
                print("Last login: Unknown from local")
                print()
                print("Congratulations! You've completed Exercise 2.")
                ssh = 1
            elif key == 0:
                print("ssh: connect to host specific-computer.cluster.domain.edu port 22: Connection refused")

    elif prompt in ssh26:
        if ssh == 1:
            print("There is a time and a place for everything! But not now.")
            print("[TUTORIAL ERROR: You're already connected!]")
        elif ssh == 0:
            prompt = input("guest@specific-computer.cluster.domain.edu's password: ")
            ssh = 1
            if key == 0:
                while known == 0:
                    print("The authenticity of host 'specific-computer.cluster.domain.edu (123.45.678.900)' can't be established.")
                    print("RSA key fingerprint is ABC123:AWJIFEO198334qu89Uu19.")
                    prompt = input("Are you sure you want to continue connecting (yes/no)? ")
                    if prompt in y:
                        known = 1
                        print("Warning: Permanently added 'specific-computer.cluster.domain.edu (123.45.678.900)' (RSA) to the list of known hosts.")
                        print()
                        print("Congratulations! You've completed Exercise 1.")
                    elif prompt in n:
                        ssh = 0
                        print("Disconnected from remote host.")
                    else: print("Please type 'yes' or 'no.'")
            elif key == 1:
                print("Last login: Unknown from local")


    elif prompt in sshcf:
        if ssh == 1:
            print("There is a time and a place for everything! But not now.")
            print("[TUTORIAL ERROR: You're already connected!]")
        elif ssh == 0:
            if config == 0:
                print("ssh: Could not resolve hostname comp: Temporary failure in name resolution")
            elif config == 1:
                if perms == 0:
                    print("Bad owner or permissions on /home/user/.ssh/config")
                elif perms == 1:
                    if key == 1:
                        ssh = 1
                        print("Last login: Unknown from local")
                        print()
                        print("Congratulations! You've completed Exercise 3. The tutorial will now close.")
                        stop = 1
                    elif key == 0:
                        print("ssh: connect to host specific-computer.cluster.domain.edu port 22: Connection refused")

    elif prompt in q:
        if ssh == 1: ssh = 0
        else: raise SystemExit

    elif prompt in ls: print("")
    elif prompt in lsa: print(".ssh")
    elif prompt in lssh:
        if ssh == 0:
            print ("known_hosts")
            if gen == 1:
                print("id_rsa")
                print("id_rsa.pub")
            if config == 1:
                print("config")
        elif ssh == 1:
            if key == 1:
                print("authorized_keys")

    elif prompt in keygen:
        gen = 1
        print("Generating public/private rsa key pair.")

    elif prompt in epub:
        if ssh == 0:
            print("TUTORIAL ERROR: Can't edit. To view contents, use 'less,' 'more,' or 'cat.'")
        elif ssh == 1:
            print("TUTORIAL ERROR: Can't create file")

    elif prompt in rpub:
        if ssh == 1:
            print("No such file or directory.")
        elif ssh == 0:
            if gen == 0:
                print("No such file or directory.")
            elif gen == 1:
                print("ssh-rsa aB123 user@local")
                print("TUTORIAL NOTE: Real keys will be much longer than this one.")

    elif prompt in rpv:
        if ssh == 1:
            print("No such file or directory.")
        elif ssh == 0:
            if gen == 0:
                print("No such file or directory.")
            elif gen == 1:
                print("TUTORIAL ERROR: This is your private key! Keep it safe! [You can neither view nor edit this file.]")

    elif prompt in epv:
        if ssh == 1:
            print("TUTORIAL ERROR: Cannot create this file.")
        elif ssh == 0:
            if gen == 0:
                print("TUTORIAL ERROR: Cannot create this file.")
            elif gen == 1:
                print("This is your private key! Keep it safe!")
                print("[TUTORIAL ERROR: You can neither view nor edit this file.]")

    elif prompt in auth:
        if ssh == 1:
            prompt = input("file_contents $ ")
            if prompt in ckey:
                key = 1
                print("Saved.")
            else: print("TUTORIAL ERROR: Could not create or edit file. Please check your spelling and try again.")
        elif ssh == 0:
            print("TUTORIAL ERROR: Cannot create file. (Did you mean to connect first?)")

    elif prompt in fig:
        if ssh == 1:
            print("TUTORIAL ERROR: Cannot create file. (Did you mean to disconnect first?)")
        elif ssh == 0:
            prompt = input("line 1 $ ")
            prompt = prompt + " " + input("line 2 $     ")
            prompt = prompt + " " + input("line 3 $     ")
            prompt = prompt + " " + input("line 4 $     ")
            prompt = prompt + " " + input("line 5 $     ")
            if prompt in cfig:
                config = 1
                print("Saved.")
            else: print("TUTORIAL ERROR: Could not create or edit file. Please check your spelling and try again.")

    elif prompt in chmod:
        if ssh == 0:
            if config == 0:
                print("No such file or directory.")
            elif config == 1:
                perms = 1
        elif ssh == 1:
            print("No such file or directory.")

    else: print("I am sorry, my responses are limited. You must ask the right questions.")
    elif prompt.startswith('cd') == True: print("TUTORIAL ERROR: Unsupported command; only the home directories are supported for this tutorial. Try using relative file paths instead.")

    else: print("I am sorry, my responses are limited. You must ask the right questions.")
    else: print("[TUTORIAL ERROR: Unrecognized command, argument, or target. Please closely follow the steps in the exercises and check your spelling.]")