# An example of thread unsafe operations like changing a global state
import threading
import random
from time import sleep

threads = []
count = 0


def tiny_sleep():
    sleep(random.uniform(0.01, 0.1))


def incr():
    global count
    old_count = count
    tiny_sleep()
    count = old_count + 1


if __name__ == '__main__':

    for i in range(100):
        t = threading.Thread(target=incr)
        threads.append(t)

    for t in threads:
        tiny_sleep()
        t.start()

    for t in threads:
        t.join()

    print(count)                    # Should be 100
