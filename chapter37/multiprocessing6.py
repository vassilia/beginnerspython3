from multiprocessing import Process, Pipe
from time import sleep


def worker(conn):
    print('Worker - started now sleeping for 1 second')
    sleep(1)
    print('Worker - sending data via Pipe')
    conn.send('hello')
    print('Worker - closing worker end of connection')
    conn.close()


def main():
    print('Main - Starting, creating the Pipe')
    parent_connection, child_connection = Pipe()
    print('Main - Setting up the process')
    p = Process(target=worker, args=[child_connection])
    print('Main - Starting the process')
    p.start()
    print('Main - Wait for a response from the child process')
    print(parent_connection.recv())
    print('Main - closing parent process end of connection')
    parent_connection.close()
    print('Main - Done')


if __name__ == '__main__':
    main()
