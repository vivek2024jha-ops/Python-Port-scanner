import socket
import sys
import time
import threading

usage = "python3 Port_Scanner.py TARGET START_PORT END_PORT"

print("_" * 70)
print("Python Simple Port Scanner")
print("_" * 70)

Start_time = time.time()

if len(sys.argv) != 4:
    print(usage)
    sys.exit()

try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name resolution error")
    sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print("Scanning target", target)

closed_ports = 0
open_ports = 0
lock = threading.Lock()

def scan_port(port):
    global closed_ports, open_ports

    print("Scanning port:", port)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    conn = s.connect_ex((target, port))

    if conn == 0:
        try:
            service = socket.getservbyport(port)
        except:
            service = "Unknown"

        print("Port {} is OPEN ({})".format(port, service))
        with lock:
            open_ports += 1
    else:
        with lock:
            closed_ports += 1

    s.close()

threads = []

for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

End_time = time.time()

print("\nTotal Open Ports:", open_ports)
print("Total Closed Ports:", closed_ports)
print("Total Time Taken: {:.2f} seconds".format(End_time - Start_time))