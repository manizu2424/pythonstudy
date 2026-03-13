'''
1. 소켓생성
2. 바인딩
3. 접속대기
4. 접속수락
5. 데이터 송수신
6. 접속종료
'''
import socket

print("1. 소켓생성")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(server_socket)

print("2. 바인딩")
server_socket.bind(('localhost', 9999))

print("3. 접속대기")
server_socket.listen()

print("4. 접속수락")
client_socket, addr = server_socket.accept()
print(client_socket)
print(addr) 

print("5. 데이터 송수신")
receve_data = client_socket.recv(1024)
print("받은 데이터:", receve_data.decode())
client_socket.send("I am a server".encode())

print("6. 접속종료")
client_socket.close()
server_socket.close()