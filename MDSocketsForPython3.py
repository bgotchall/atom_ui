import socket
import select
class MDSocket:
    def __init__(self,ip_addr,tcp_port,timeout_secs):
        self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.ip=ip_addr
        self.tcp=tcp_port
        self.to=timeout_secs
        self.baseCommand="m"
        self.rxbufsize = 1024
        self.read_all_at_once = True
        
    #connect
    def connect(self):
        self.s.setblocking(0)
        self.s.settimeout(self.to)
        self.s.connect((self.ip,self.tcp))
    #disconnect
    def disconnect(self):
        if self.s!=None:
            self.s.close()

    #send command string to connected socket
    def send(self, command):
        if self.s is None:
            raise OSError('Socket error; not connected')
        
        buf = bytes(command, 'ascii')
        try:
            self.s.sendall(buf)
        except OSError as e:
            raise OSError("Socket error; send failure (sending \'%s\')" % command.strip())
    #receive response from connected socket
    def receive(self):
        if self.s is None:
            raise OSError('Socket error; not connected')

        bytes = bytearray()
        while True:
            try:
                readable, writeable, error = select.select([self.s], [], [], self.to)
            except Exception as e:
                raise OSError("Socket error; read failure")

            if readable:
                data = self.s.recv(self.rxbufsize)
                if not data:
                    raise OSError('Socket error; no data on readable socket')
                else:
                    bytes += data
                    if self.read_all_at_once:
                        break
            else:
                break

        response = str(bytes, 'utf-8', errors="ignore").rstrip('\r\n')
        return response

    def transact(self, command):
        self.send(command)
        response = self.receive()
        return response
    #Read MI Registar from machine       
    def ReadMI(self,address):
        if self.s is None:
            raise OSError('Socket error;not connected')
        Command="MI" + address +"?"
        self.transact(self.baseCommand)
        print ('Querying ' + Command)
        return self.transact(Command)
    #Read MB Registar from machine    
    def ReadMB(self,address):
        if self.s is None:
            raise OSError('Socket error;not connected')
        Command="MB" + address +"?"
        self.transact(self.baseCommand)
        print ('Querying ' + Command)
        return self.transact(Command)
        
    #Write MI Registar with specified value
    def WriteMI(self,address,value):
        if self.s is None:
            raise OSError('Socket error;not connected')
        Command="MI" + address +"," + str(value)
        self.transact(self.baseCommand)
        print ('Modifying ' + Command)
        return self.transact(Command)
    #Write MB Registar with specified value    
    def WriteMB(self,address,value):
        if self.s is None:
            raise OSError('Socket error;not connected')
        Command="MB" + address +"," + str(value)
        self.transact(self.baseCommand)
        print ('Modifying ' + Command)
        return self.transact(Command)

#main
if __name__ =='__main__':
    #socket info
    ip_addr="10.109.10.20"
    tcp_port=5000
    timeout_secs = 3
    s=MDSocket(ip_addr,tcp_port,timeout_secs)
    print('Connecting...')
    s.connect()
    print(s.ReadMB("0020"))
    print(s.ReadMI("0699"))
    print(s.WriteMB("0020",0))
    print(s.ReadMB("0020"))
    
    
    print(s.WriteMI("0699","0260"))
    print(s.ReadMI("0699"))
    s.disconnect()
