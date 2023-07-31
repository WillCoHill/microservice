# Microservice

+ PORT hard coded to be 1234.

+ Run on same machine as main programme.

+ Data is sent as utf-8 encoded string, be sure to cast to int in order to use. Max byte size is 1024
      + create a socket object.
          <br />`s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)`
          <br />`s.connect((socket.gethostname(), 1234))` <br />
          
+ get data with a receive command
          <br />`s.recv(1024)`

+ Decode with a direct encode() call to the data with parameter "utf-8" then cast to int if desired
          <br />`data.encode("utf-8")`
  
+ Server is running in while loop and generates random int from 1 to 8 again after sending data

<sub>optimal for multiple calls</sub>
![UML Diagram of the socket process](https://github.com/WillCoHill/microservice/blob/main/YouTube%20Diagram.png)https://github.com/WillCoHill/microservice/blob/main/YouTube%20Diagram.png)
