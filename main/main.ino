// main.ino
// #include "WiFiManager.h"
#include "SerialProxy.h"
#include "ADCReader.h"
#include "config.h"

void setup() {
    // 初始化串口代理
    SerialProxy.begin();

    // 初始化WiFi
    WiFiManager.begin();

    // 初始化ADC读取
    ADCReader.begin();

    // 根据serial_method设置
    if(String(SERIAL_METHOD) == "web") {
        SerialProxy.log("Serial method set to WEB");
    }
    else if(String(SERIAL_METHOD) == "serial") {
        SerialProxy.log("Serial method set to SERIAL");
    }
    else {
        SerialProxy.log("Unknown serial method, defaulting to SERIAL");
    }
}

void loop() {
    // 处理串口代理
    SerialProxy.handle();

    // 更新ADC读取
    ADCReader.update();
}
