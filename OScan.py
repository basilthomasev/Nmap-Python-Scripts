##
##   OS Scanner
##   Scanning methods All
##   Developed by Basil Thamas
##
import nmap
nm = nmap.PortScanner()
scan_array =["-sn","-sT","-sA","-sW","-sM"]
for scan in scan_array:
 nm.scan(hosts='127.0.0.1', arguments='scan -O --osscan-guess -iL input.txt -oN /root/Documents/Codes/Network_Sec/Finished_codes/result_OSscan.txt  --append-output')
 print "The method of scan is:  ", scan
 for host in nm.all_hosts():
    print(host)
    print(nm[host])
    #value = (nm[host].get('osmatch'))
    #print(value)
