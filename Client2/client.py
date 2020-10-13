import socket, sys

def main():

    if len(sys.argv)<2:
        host = raw_input("Enter host ip address: ")
    else:
        host = sys.argv[1]

    port = 5001
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    s.connect((host, port))
    docName = s.recv(1024)
    print "Enter "+"'"+docName+"' when prompted to download the document..."
    s.send('OKAY')
    filename = raw_input("Enter the filename: ")
    if filename !='q':
        s.send(filename)
        datafile = s.recv(1024)
        if datafile[:6] == 'EXISTS':
            filesize = long(datafile[6:])
	    message = raw_input("File Exists, "+str(filesize)+" Bytes, downoad?(Y/N): ")
	    if message == 'Y':
                s.send('OK')
    	        f = open('new_'+filename, 'wb')
       	        datafile = s.recv(1024)
                totalRecv= len(datafile)
                f.write(datafile)
		while totalRecv < filesize:
                    datafile=s.recv(1024)
       	            totalRecv+=len(datafile)
		    f.write(datafile)
                    print "{0:.2f}".format((totalRecv/float(filesize))*100)+"% Done"
	        print "Download Complete!"

	else:
		print "File does not exist!"

    s.close()

if __name__ == "__main__":
    main()
