
import os
import time
from multiprocessing import Process, current_process

def square(number):
    for number in numbers:
        time.sleep(0.5)
        result = number * number
        proc_id = os.getpid()
        print(f'The number {number} squares to {result}.')
        print(f'Process ID: {proc_id}')

#if __name__ == '__main__':

processes = []
numbers = range(100)

for i in range(50):
    process = Process(target=square, args=(numbers,))
    processes.append(process)

    # Processes are spawned by creating a Process object and
    # then calling its start() method.
    process.start()

for process in processes:
    process.join()

print('Multiprocessing complete')
