##
##   Firewall Scanner
##   Scanning methods All
##   Developed by Basil Thamas
##

import nmap
nm = nmap.PortScanner()
scan_array =["-sn","-sT","-sA","-sW","-sM"]
for scan in scan_array:
 nm.scan(hosts='127.0.0.1', arguments='scan -f --mtu 16  -S 10.0.2.1 -e eth0 -iL input.txt -oN  /root/Documents/Codes/Network_Sec/Finished_codes/Results/result_Firewall.txt --append-output')
 print "The method of scan is:  ", scan
 for host in nm.all_hosts():
     print "   -----------------------------------------------------"
     print "   Hostname   :"    , host
     print(nm[host])
     #Status = (nm[host].get('status'))
     #print "   Status   :",Status
     #hostnames = (nm[host].get('hostnames'))
     #print "   hostnames   :",hostnames
     #vendor = (nm[host].get('vendor'))
     #print "   vendor   :",vendor
