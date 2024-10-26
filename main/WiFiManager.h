// WiFiManager.h
#ifndef WIFIMANAGER_H
#define WIFIMANAGER_H

#include <WiFi.h>
#include <DNSServer.h>
#include "config.h"

class WiFiManagerClass {
public:
    void begin();
};

extern WiFiManagerClass WiFiManager;

#endif // WIFIMANAGER_H
