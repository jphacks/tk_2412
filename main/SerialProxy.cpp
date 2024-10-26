// SerialProxy.cpp
#include "SerialProxy.h"
#include "config.h"

#if SERIAL_METHOD == 1  // 如果SERIAL_METHOD为1，则启用web模式
  #include <WebServer.h>
  #include <Update.h>
#endif

SerialProxyClass SerialProxy;

#if SERIAL_METHOD == 1
WebServer server(WEB_PORT);
String logBuffer = "";

void handleRoot() {
    String page = "<!DOCTYPE html><html><head><title>ESP32 Logs</title></head><body><h1>Logs</h1><pre>";
    page += logBuffer;
    page += "</pre><h2>OTA Update</h2><form method='POST' action='/update' enctype='multipart/form-data'>";
    page += "<input type='file' name='update'><input type='submit' value='Update'></form></body></html>";
    server.send(200, "text/html", page);
}

void handleUpdate() {
    HTTPUpload& upload = server.upload();
    if (upload.status == UPLOAD_FILE_START) {
        Serial.println("Start OTA Update");
        if (!Update.begin(UPDATE_SIZE_UNKNOWN)) { // Start with max available size
            Update.printError(Serial);
        }
    } else if (upload.status == UPLOAD_FILE_WRITE) {
        if (Update.write(upload.buf, upload.currentSize) != upload.currentSize) {
            Update.printError(Serial);
        }
    } else if (upload.status == UPLOAD_FILE_END) {
        if (Update.end(true)) { // true to set the size to the current progress
            Serial.println("OTA Update Success");
            server.sendHeader("Location", "/");
            server.send(303, "text/plain", ""); // Redirect to root
        } else {
            Update.printError(Serial);
            server.send(500, "text/plain", "OTA Update Failed");
        }
    }
}

void handleNotFound(){
    server.send(404, "text/plain", "Not Found");
}
#endif

void SerialProxyClass::begin() {
    Serial.begin(115200);
#if SERIAL_METHOD == 1
    // 设置Web服务器路由
    server.on("/", handleRoot);
    server.on("/update", HTTP_POST, []() {}, handleUpdate);
    server.onNotFound(handleNotFound);
    server.begin();
    Serial.println("Web server started");
#endif
}

void SerialProxyClass::log(const String &message) {
#if SERIAL_METHOD == 1
    logBuffer += message + "\n";
    // 限制日志大小
    if (logBuffer.length() > 10000) {
        logBuffer = logBuffer.substring(logBuffer.length() - 10000);
    }
#else
    Serial.println(message);
#endif
}

void SerialProxyClass::handle() {
#if SERIAL_METHOD == 1
    server.handleClient();
#endif
}

void SerialProxyClass::setupOTA() {
#if SERIAL_METHOD == 1
    // OTA已经在handleUpdate中处理
#endif
}
