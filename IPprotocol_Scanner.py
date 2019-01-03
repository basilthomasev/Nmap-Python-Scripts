##
##   IP protocol Scanner
##   Scanning methods All 
##   Developed by Basil Thamas
##

import nmap 
nm = nmap.PortScanner()

nm.scan(hosts='127.0.0.1', arguments='-sO -iL input.txt -oN /root/Documents/Codes/Network Sec/Finished codes/Results/result_IPprotocol')
for host in nm.all_hosts():
     print "   -----------------------------------------------------"
     print "   Hostname   :"    , host
     print(nm[host])
     Status = (nm[host].get('status'))
     print "   Status   :",Status
 
