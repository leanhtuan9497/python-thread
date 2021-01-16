import threading
import time

def tinh_tong(a,b):
    print("start thread", threading.current_thread())
    time.sleep(1)
    print(a + b)

t1 = threading.Thread(target=tinh_tong,args=(1,2,), name="T1")
t2 = threading.Thread(target=tinh_tong,args=(10,2,))

t1.start()
t2.start()
t1.join()
t2.join()
print("end")
