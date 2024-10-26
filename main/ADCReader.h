// ADCReader.h
#ifndef ADCREADER_H
#define ADCREADER_H

#include <Arduino.h>

class ADCReaderClass {
public:
    void begin();
    void update();
private:
    const int GSR_PIN = 34;
    const int LED_PIN = 15;
    int threshold;
    long sum;
    int count;
    unsigned long lastPostTime;
    long accumulatedValue;
};

extern ADCReaderClass ADCReader;

#endif // ADCREADER_H
