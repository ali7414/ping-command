import sys
import subprocess 
import platform
#checking IP reachability 
def ip_reach(list):
 
    ip=list.rstrip("\n")
    #here we check wheather the operating system is windows or linux
    param='-n' if platform.system().lower()=='windows' else '-c'
    command=['ping',param,'2',ip]
    ping_reply=subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if (ping_reply.returncode==0) and  (("Destination host unreachable.") not in str(ping_reply)):
    #in Windows this function will still return True if you get a Destination Host Unreachable error. so we check the response here
        print("\n {} is reachable \n".format(ip))
        sys.exit()
    elif ping_reply.returncode ==0:
        print("\n {} not reachable check connectivity and try again".format(ip))
        sys.exit()
    else:
        print("\n {} not reachable check connectivity and try again".format(ip))
        sys.exit()
            
addr= input("please enter your IP Address:\n")
ip_reach(addr)