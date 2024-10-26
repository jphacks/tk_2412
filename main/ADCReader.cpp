// ADCReader.cpp
#include "ADCReader.h"
#include "SerialProxy.h"
#include "WiFiManager.h"
#include "config.h"
#include <WiFiClient.h>

ADCReaderClass ADCReader;

void ADCReaderClass::begin() {
    pinMode(LED_PIN, OUTPUT);
    digitalWrite(LED_PIN, LOW);
    delay(1000);

    for (int i = 0; i <= 100; i++) {
      int sensorValue = analogRead(GSR_PIN);
      SerialProxy.log(String(sensorValue));
      delay(20);
    }
    

    sum = 0;
    int max = 0, min = 4095;
    for(int i = 0; i < 1000; i++) {
        int sensorValue = analogRead(GSR_PIN);
        if (sensorValue <= 150) {
          delay(50);
          continue;
        }
        if (sensorValue > max) {
          max = sensorValue;
        }
        if (sensorValue <= min) {
          min = sensorValue;
        }
        sum += sensorValue;
        delay(5);
    }
    threshold = sum / 1000;
    SerialProxy.log("threshold = " + String(threshold));
    SerialProxy.log("max = " + String(max));
    SerialProxy.log("min = " + String(min));

    lastPostTime = millis();
    accumulatedValue = 0;
    count = 0;
}

void ADCReaderClass::update() {
    delay(100);
    int sensorValue = analogRead(GSR_PIN);
    SerialProxy.log("sensorValue=" + String(sensorValue));
    accumulatedValue += sensorValue;
    count++;

    // // 检测情绪变化（基于原始代码）
    // int temp = threshold - sensorValue;
    // if(abs(temp) > 60) {
    //     sensorValue = analogRead(GSR_PIN);
    //     temp = threshold - sensorValue;
    //     if(abs(temp) > 60){
    //         digitalWrite(LED_PIN, HIGH);
    //         SerialProxy.log("Emotion Changes Detected!");
    //         delay(3000);
    //         digitalWrite(LED_PIN, LOW);
    //         delay(1000);
    //     }
    // }

    // 每5秒发送一次数据
    // if (millis() - lastPostTime >= 5000) {
    //     if(count > 0){
    //         long average = accumulatedValue / count;
    //         // 发送POST请求
    //         WiFiClient client;
    //         if (client.connect(POST_HOST, POST_PORT)) {
    //             String postData = "value=" + String(average);
    //             client.println("POST " + String(POST_ENDPOINT) + " HTTP/1.1");
    //             client.println("Host: " + String(POST_HOST));
    //             client.println("Content-Type: application/x-www-form-urlencoded");
    //             client.println("Content-Length: " + String(postData.length()));
    //             client.println();
    //             client.print(postData);
    //             client.stop();
    //             SerialProxy.log("Posted data: " + String(average));
    //         } else {
    //             SerialProxy.log("Failed to connect to server");
    //         }
    //         // 重置累积值
    //         accumulatedValue = 0;
    //         count = 0;
    //         lastPostTime = millis();
    //     }
    // }
}
