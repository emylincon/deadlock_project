import threading

shared_lock = 0
count = 10
shared_resource_lock = threading.Lock()


def increment_with_lock():
    global shared_resource_lock
    global shared_lock

    for i in range(count):
        shared_resource_lock.acquire()
        shared_lock += 1
        shared_resource_lock.release()


def decrement_with_lock():
    global shared_resource_lock
    global shared_lock

    for i in range(count):
        shared_resource_lock.acquire()
        shared_lock -= 2
        shared_resource_lock.release()


if __name__ == "__main__":
    t1 = threading.Thread(target=increment_with_lock)
    t2 = threading.Thread(target=decrement_with_lock)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('value: ', shared_lock)