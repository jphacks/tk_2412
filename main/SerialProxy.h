// SerialProxy.h
#ifndef SERIALPROXY_H
#define SERIALPROXY_H

#include <Arduino.h>
#include "config.h"

class SerialProxyClass {
public:
    void begin();
    void log(const String &message);
    void handle();
    void setupOTA(); // 仅在WEB模式下使用
};

extern SerialProxyClass SerialProxy;

#endif // SERIALPROXY_H
