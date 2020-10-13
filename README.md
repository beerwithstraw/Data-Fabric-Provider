# Multi-Client File Transfer Program
## About 
This is a simple multi-client file transfer program using `sockets` written in `python`. 

The server, when started, is asked to input the filename that it needs to supply to the clients when they connect. When any client is connected to the server, a message to the client is sent regarding the filename for the user to enter to download the file. 
The users response to download the file or not is stored in a text file with the server to keep track. And a new file is downloaded on client's workspace if they opt to download it.
## Environment
Run in a linux-based operating system. Currently working on Ububtu Desktop 18.04 LTS.
Or download the latest version from https://ubuntu.com/#download Desktop version.

## Run
Once you are in the directory where `server.py` or `client.py` file exists, run by typing the following commands in your terminal.

#### Server
> $ python server.py

#### Client
> $ python client.py hostname

## Example
For server and client running on the same system

**Server**
> $ python server.py
<pre>
				SERVER WORKING 
Enter filename you wish to distribute: "test.txt"
Waiting for connection...

Client connected <ip: ('127.0.0.1.,53552)>
	Message sent out to client <ip: ('127.0.0.1',53552)>
Client connected <ip: ('127.0.0.1.,53554)>
	Message sent out to client <ip: ('127.0.0.1.,53554)>
	Client: <ip: ('127.0.0.1.,53552)> disconnected!
	Client: <ip: ('127.0.0.1.,53554)> disconnected!
Client connected <ip: ('127.0.0.1.,53556)>
	Message sent out to client <ip: ('127.0.0.1.,53556)>
	Client: <ip: ('127.0.0.1.,53556)> disconnected!
</pre>


**Client 1**
> $ python client.py localhost

<pre>
Enter 'test.txt' when prompted to download the document...
Enter the filename: "test.txt"
File Exists, 11 Bytes, downoad?(Y/N): "Y"
Download Complete!
$
</pre>
**Client 2**
> $ python client.py localhost

<pre>
Enter 'test.txt' when prompted to download the document...
Enter the filename: "test.txt"
File Exists, 11 Bytes, downoad?(Y/N): "N"
$
</pre>

**Client 3**
> $ python client.py
> Enter host ip address: "127.0.0.1"
<pre>
Enter 'test.txt' when prompted to download the document...
Enter the filename: "doc.txt"
File does not exist!
$
</pre>

####Clients.txt 
<pre>
Client: ('127.0.0.1', 53552) downloaded the file 'test.txt'
Client: ('127.0.0.1', 53554) did not download the file 'test.txt'
</pre>

