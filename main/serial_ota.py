# serial_ota.py
import serial
import time
import sys

def send_firmware_update(serial_port, firmware_path):
    with open(firmware_path, 'rb') as f:
        firmware = f.read()

    ser = serial.Serial(serial_port, 115200, timeout=1)
    time.sleep(2)  # 等待串口初始化

    # 假设ESP32已经有接收OTA的协议
    # 具体实现取决于ESP32端的OTA接收代码

    # 这里是一个示例流程
    ser.write(b'OTA_START\n')
    time.sleep(1)
    ser.write(firmware)
    ser.write(b'OTA_END\n')

    while True:
        line = ser.readline().decode('utf-8').rstrip()
        if line:
            print(line)
        if 'OTA Update Success' in line:
            print("Firmware update successful")
            break
        elif 'OTA Update Failed' in line:
            print("Firmware update failed")
            break

    ser.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python serial_ota.py <serial_port> <firmware_path>")
        sys.exit(1)

    serial_port = sys.argv[1]
    firmware_path = sys.argv[2]

    send_firmware_update(serial_port, firmware_path)
