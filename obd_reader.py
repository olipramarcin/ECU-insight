import obd
import serial.tools.list_ports
from multiprocessing import Process, Queue

def try_connect(port, queue):
    try:
        connection = obd.OBD(port, fast=False, timeout=1)
        if connection.is_connected():
            queue.put(port)
        else:
            queue.put(None)
    except:
        queue.put(None)

def auto_connect():
    ports = serial.tools.list_ports.comports()
    print("🔍 Wykrywam porty OBD...")

    for port in ports:
        port_name = port.device

        print(f"Próba: {port_name}")

        queue = Queue()
        p = Process(target=try_connect, args=(port_name, queue))
        p.start()

        p.join(2)

        if p.is_alive():
            print(f"⚠️ Timeout na {port_name} → zabijam")
            p.terminate()
            p.join()
            continue

        result = queue.get()

        if result:
            print(f"✅ Połączono: {result}")
            return obd.OBD(result, fast=False)

    print("❌ Nie znaleziono OBD")
    return None
