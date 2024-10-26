// config.h
#ifndef CONFIG_H
#define CONFIG_H

// 定义serial方法: 0 = serial, 1 = web
#define SERIAL_METHOD 0  // 1 表示 web 模式，0 表示 serial 模式

// 固定IP的MAC地址
#define FIXED_MAC "34:5f:45:a8:9a:a4"

// 固定IP地址
#define FIXED_IP "192.168.1.2"

// ESP32的IP地址
#define ESP_IP "192.168.1.1"

// POST目标地址和端口
#define POST_HOST "192.168.1.2"
#define POST_PORT 3000
#define POST_ENDPOINT "/api/emotion"

// WiFi AP配置
#define AP_SSID "Emotional Damage"
#define AP_PASSWORD "1919810@JPHacks"

// OTA Web端口
#define WEB_PORT 80

#endif // CONFIG_H
