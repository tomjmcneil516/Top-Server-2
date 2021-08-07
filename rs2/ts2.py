import socket                
import sys

DNS_table = {}
DNS_file = open("PROJ2-DNSTS2.txt", 'r') 
for line in DNS_file:   
    domain_name = line.split()[0]  
    IP = line.split()[1]   
    flag = line.split()[2]         
    DNS_table[domain_name] = IP + " " + flag


ts2hostname = socket.gethostname()
ts2listenport = int(sys.argv[1])             

 
while True:       
                  
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
                s.bind((ts2hostname, ts2listenport))          

                s.listen(5)          

                conn, addr = s.accept() 

                data = conn.recv(4096)  
                if not data:            
                    break
                domain_name = data.decode('utf-8')
                if domain_name in DNS_table:            
                    data = (domain_name + " " + DNS_table[domain_name]).encode('utf-8')
                    conn.sendall(data)

                s.close()

             

