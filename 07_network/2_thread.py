import time
import threading

def get_order():
  for i in range(5):
    print(f"주문 받기{i+1}")
    time.sleep(1)


def send_order():
  for i in range(5):
    print(f"주문 전송{i+1}")
    time.sleep(1)

# get_order()
# send_order()

# 스레드 생성
t1 = threading.Thread(target=get_order)
t2 = threading.Thread(target=send_order)

# 스레드가 데몬 스레드인지 여부를 나타냅니다. 데몬 스레드는 백그라운드에서 실행되며 프로그램이 종료되는 것을 방해하지 않습니다. 이 속성은 start()를 호출하기 전에 설정해야 합니다.
t1.daemon = True
t2.daemon = True

# 스레드 시작
t1.start()
t2.start()

# 스레드가 종료될 때까지 대기
t1.join()
t2.join()

print("프로그램 종료")