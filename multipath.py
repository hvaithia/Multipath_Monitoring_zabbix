#!/usr/bin/python

import sys

def multipath_check():
        infile = "/usr/lib/zabbix/externalscripts/test2.out"
        outfile = "/usr/lib/zabbix/externalscripts/zabbixout.log"
        mpath_var=""
        filehandler = open(outfile,'w')
        statusvar=0
        with open(infile) as inf:
                for line in inf:
                        if "mpath" in line:
                                mpath_var=line
                        if "policy" in line:
                                if "active" in line or "enabled" in line:
                                        continue
                                else:
                                        statusvar = 1
                                        print mpath_var
                                        filehandler.write(mpath_var)
        if statusvar == 0:
                filehandler.write("NORMAL\n")
                print "NORMAL"
        elif statusvar == 1:
                with open(outfile, 'r') as myfile:
                        print myfile.read().replace('\n','|')
        else:
                print "Error Unknown"
        filehandler.close()

def main():
        multipath_check()

if __name__ == "__main__":
        main()

