import threading
import  os


def ADD():
    print('add operation')
    print(os.getpid())
    print('add operation is assigned to thread:{}'.format(threading.current_thread().name))

def SUB():
    print('sub operation')
    print(os.getpid())
    print('sub operation is assigned to thread:{}'.format(threading.current_thread().name))

if __name__=="__main__":
    print("Main thread name:{}".format(threading.current_thread().name))

    t1=threading.Thread(target=ADD,name='t1')
    t2=threading.Thread(target=SUB,name='t2')

    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

    

