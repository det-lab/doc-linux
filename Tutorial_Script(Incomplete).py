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
    'more ~/.ssh/id_rsa.pub',
    'less ~/.ssh/id_rsa.pub',
    'more /home/user/.ssh/id_rsa.pub',
    'less /home/user/.ssh/id_rsa.pub'}
ckey = {'aB123 user@local'}
rpv = {'less .ssh/id_rsa',
    'more .ssh/id_rsa',
    'less ~/.ssh/id_rsa',
    'more ~/.ssh/id_rsa',
    'less /home/user/.ssh/id_rsa',
    'more /home/user/.ssh/id_rsa'}
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
cfig = {'Host comp \
    HostName specific-computer.cluster.domain.edu \
    User guest \
    Port 22 \
    IdentityFile /home/user/.ssh/id_rsa'}
chmod = {'chmod 600 ~/.ssh/config',
    'chmod 600 /home/user/.ssh/config',
    'chmod 600 .ssh/config'}

#Taking commands.
a = 0
while a == 0: #Force indefinite loop.
    prompt = raw_input(' $ ') #Initial prompt
    if prompt in ssh22:
        if ssh == 1:
            print("TUTORIAL ERROR: You're already connected!")
        elif ssh == 0:
            if key == 1:
                print("Congratulations! You've completed Exercise 2.")
                ssh = 1
            elif key == 0:
                print("You do not have permission to connect to port 22 on this computer.")
            else: print("TUTORIAL ERROR: INTERNAL: Invalid value for 'key.'")
        else: print("TUTORIAL ERROR: INTERNAL: Invalid value for 'ssh.'")

    elif prompt in ssh26:
        if ssh == 1:
            print("TUTORIAL ERROR: You're already connected!")
        elif ssh == 0:
            prompt = raw_input("password: ")
            ssh = 1
            if key == 0:
                while known == 0:
                    prompt = raw_input("Host unrecognized. Continue? [yes/no]: ")
                    if y:
                        known = 1
                        print("Congratulations! You've completed Exercise 1.")
                    elif n:
                        ssh = 0
                        print("Disconnected from remote host.")
                        break
                    else: print("Please type 'yes' or 'no.'")
            elif key != 1: print("TUTORIAL ERROR: INTERNAL: Invalid value for 'key.'")
        else: print("TUTORIAL ERROR: INTERNAL: Invalid value for 'ssh.'")

    elif prompt in sshcf:
        if ssh == 1:
            print("TUTORIAL ERROR: You're already connected!")
        elif ssh == 0:
            if config == 0:
                print("Host not found.")
            elif config == 1:
                if perms == 0:
                    print("Bad permissions.")
                elif perms == 1:
                    ssh = 1
                    print("Congratulations! You've completed Exercise 3. You may now close the tutorial.")
                else: print("TUTORIAL ERROR: INTERNAL: Invalid value for 'perms.'")
            else: print("TUTORIAL ERROR: INTERNAL: Invalid value for 'config.'")
        else: print("TUTORIAL ERROR: INTERNAL: Invalid value for 'ssh.'")

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
            elif gen != 0:
                print("TUTORIAL ERROR: INTERNAL: Invalid value for 'gen.'")
            if config == 1:
                print("config")
            elif config != 0:
                print("TUTORIAL ERROR: INTERNAL: Invalid value for 'config.'")
        elif ssh == 1:
            if key == 1:
                print("authorized_keys")
            elif key != 0:
                print("TUTORIAL ERROR: INTERNAL: Invalid value for 'key.'")
        else: print("TUTORIAL ERROR: INTERNAL: Invalid value for 'ssh.'")

    elif prompt in keygen:
        gen = 1
        print("Key created.")

    elif prompt in epub:
        if ssh == 0:
            print("TUTORIAL ERROR: Can't edit. To view contents, use 'less' or 'more.'")
        elif ssh == 1:
            print("TUTORIAL ERROR: Can't create file")
        else: print("TUTORIAL ERROR: INTERNAL: Invalid value for 'ssh.'")

    elif prompt in rpub:
        print("TUTORIAL NOTE: Will render similarly to 'more,' but may vary.")
        if ssh == 1:
            print("The specified file does not exist.")
        elif ssh == 0:
            if gen == 0:
                print("The specified file does not exist.")
            elif gen == 1:
                print("aB123 user@local")
                print("TUTORIAL NOTE: Real keys will be much longer than this one.")
            else: print("TUTORIAL ERROR: INTERNAL: Invalid value for 'gen.'")
        else: print("TUTORIAL ERROR: INTERNAL: Invalid alue for 'ssh.'")

    elif prompt in rpv:
        if ssh == 1:
            print("The specified file does not exist.")
        elif ssh == 0:
            if gen == 0:
                print("The specified file does not exist.")
            elif gen == 1:
                print("TUTORIAL WARNING: This is your private key! Keep it safe! [You can neither view nor edit this file.]")
            else: print("TUTORIAL ERROR: INTERNAL: Invalid value for 'gen.'")
        else: print("TUTORIAL ERROR: INTERNAL: Invalid value for 'ssh.'")

    elif prompt in epv:
        if ssh == 1:
            print("TUTORIAL ERROR: Cannot create this file.")
        elif ssh == 0:
            if gen == 0:
                print("TUTORIAL ERROR: Cannot create this file.")
            elif gen == 1:
                print("TUTORIAL WARNING: This is your private key! Keep it safe! [You can neither view nor edit this file.]")
            else: print("TUTORIAL ERROR: INTERNAL: Invalid value for 'gen.'")
        else: print("TUTORIAL ERROR: INTERNAL: Invalid value for 'ssh.'")

    elif prompt in auth:
        if ssh == 1:
            print("TUTORIAL NOTE: A generic text prompt will be used instead of the specified editor.")
            prompt = raw_input("file_contents $ ")
            if prompt in ckey:
                key = 1
                print("Saved.")
            else: print("TUTORIAL ERROR: Could not create or edit file. Please check your spelling and try again.")
        elif ssh == 0:
            print("TUTORIAL ERROR: Cannot create file. (Did you mean to connect first?)")
        else: print("TUTORIAL ERROR: INTERNAL: Invalid value for 'ssh.'")

    elif prompt in fig:
        if ssh == 1:
            print("TUTORIAL ERROR: Cannot create file. Did you mean to disconnect first?")
        elif ssh == 0:
            print("TUTORIAL NOTE: A generic text prompt will be used instead of the specified editor.")
            prompt = raw_input("file_contents $ ")
            #if prompt == cfig:
            config = 1
            print("NOTE: Currently not fully implemented. Assumed correct value without checking.")
        else: print("TUTORIAL ERROR: INTERNAL: Invalid value for 'ssh.'")

    elif prompt in chmod:
        if ssh == 0:
            if config == 0:
                print("File not found.")
            elif config == 1:
                perms = 1
                print("Success.")
            else: print("TUTORIAL ERROR: INTERNAL: Invalid value for 'config.'")
        elif ssh == 1:
            print("File not found.")
        else: print("TUTORIAL ERROR: INTERNAL: Invalid value for 'ssh.'")

    elif prompt.startswith('cd') == True: print("TUTORIAL ERROR: Unsupported command; only the home directories are supported for this tutorial. Try using relative file paths instead.")

    else: print("TUTORIAL ERROR: Unrecognized command. Please closely follow the steps in the exercises and check your spelling.")