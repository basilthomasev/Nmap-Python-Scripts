##
##   Port & Service Scanner
##   Scanning methods All
##   Developed by Basil Thamas
##

import nmap
nm = nmap.PortScanner()
nm.scan(hosts='192.168.1.5', arguments='-sV -A -v --privileged --version-all --version-trace -T4 -p1-10000 -iL input.txt -oN /root/Documents/Codes/Network_Sec/Finished_codes/Results/result_Port_Version.txt')

for host in nm.all_hosts():
    print "   ---------------------------------------------------------------------------------------"
    print "   "
    print "   ---------------------------------------------------------------------------------------"
    print "   "
    print "   "
    print nm[host]
    print "   "
    print "   "
    print "   Hostname   :"    , host
    print "   Open ports and status of  :"  ,  host

    try:
     hostz = nm[host].get('tcp','Unknown')
     for i in hostz.items():
      for j in i:
    	print "  ",j
    except:
     print "   No ports found for this host: ", host
