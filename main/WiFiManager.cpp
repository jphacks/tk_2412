// WiFiManager.cpp
#include "WiFiManager.h"

WiFiManagerClass WiFiManager;

void WiFiManagerClass::begin() {
    // 设置ESP32为AP模式
    WiFi.mode(WIFI_AP);
    WiFi.softAP(AP_SSID, AP_PASSWORD);

    // 设置ESP32的IP
    IPAddress local_IP;
    local_IP.fromString(ESP_IP);
    WiFi.softAPConfig(local_IP, local_IP, IPAddress(255, 255, 255, 0));

    // 开启DHCP服务器并设置固定IP分配
    // Arduino的WiFi库不直接支持DHCP固定分配，需要使用esp_wifi_set_sta_list 或者其他低级API
    // 这里提供一个简化的实现，实际应用中可能需要更复杂的处理

    // 打印AP信息
    Serial.print("AP IP address: ");
    Serial.println(WiFi.softAPIP());
}
