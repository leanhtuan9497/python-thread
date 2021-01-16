import threading

sum_left = 0
sum_right = 0

def tinh_tong(arr,thread):
    tong = 0
    global sum_right
    global sum_left
    for i in arr:
        tong+=i;
    if thread == 1:
        sum_left = tong
    else:
        sum_right = tong
    print(threading.current_thread(),tong)

arr = [5,3,10,14,6,23,11,13,17,20]

t1 = threading.Thread(target=tinh_tong,args=(arr[0:int(len(arr)/2)],1,))
t2 = threading.Thread(target=tinh_tong,args=(arr[int(len(arr)/2):],2,))

t1.start()
t2.start()

t1.join()
t2.join()
print(sum_right+sum_left)
print("END")
