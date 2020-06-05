#swape keys and values of dictionary
port1={21:"FTP",22:"SSH",23:"telnet",80:"http"}
port2=dict(zip(port1.values(),port1.keys()))
print(port2)