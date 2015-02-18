# First we import the Fabric api
from fabric.api import *
import sys

sys.stdout = open("/usr/lib/zabbix/externalscripts/test2.out", "w")

# We can then specify host(s) and run the same commands across those systems
env.user = 'root'	#multipath command required root access to run
env.password = 'password_here'
env.hosts = ['host01','host02']	#Enter a list of hosts here - or Loop in for if the list is too big

def multipath():
        # Run multipath command on targets
        run("multipath -ll")

