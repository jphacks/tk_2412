import serial

# 初始化串口
ser = serial.Serial('/dev/cu.usbserial-0001', 115200)
output_file = 'sensor_values.txt'

# 打开文件用于写入数据
with open(output_file, 'w') as file:
    try:
        while True:
            # 读取一行串口输出并解码为字符串
            line = ser.readline().decode('utf-8').strip()

            # 检查是否包含 "sensorValue=" 并提取数值
            if line.startswith("sensorValue="):
                value = line.split("=")[1]  # 提取"="后的部分
                if value == '0':
                    continue
                file.write(f"{value}\n")  # 将数值写入文件，每行一个
                file.flush()  # 确保每次写入文件时数据即时保存
                print(f"Sensor value: {value}")

    except KeyboardInterrupt:
        print("数据采集结束")
    finally:
        ser.close()
