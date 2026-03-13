'''
1. 소켓생성
2. 
3. 접속시도
4. 
5. 데이터 송수신
6. 접속종료
'''
import socket

print("1. 소켓생성")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(client_socket)

print("2. ")

print("3. 접속시도")
client_socket.connect(('localhost', 9999))

print("4. ")

print("5. 데이터 송수신")
client_socket.send("I am a client".encode())
receve_data = client_socket.recv(1024)
print("받은 데이터:", receve_data.decode())

print("6. 접속종료")
client_socket.close()
# server_socket.close()  # 클라이언트에서는 서버 소켓을 닫지 않음 (서버가 닫아야 함)