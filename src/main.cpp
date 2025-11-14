#include <Arduino.h>
#include "model.h"

void setup()
{
  Serial.begin(115200);
}

using namespace Eloquent::ML::Port;

RandomForest classifier;

void loop()
{
  // TODO: Replace with real sensor data
  float x_sample[] = {0.1, 0.2, 0.3}; // Example sample, update as needed
  int prediction = classifier.predict(x_sample);
  Serial.println(prediction);
  delay(500);
}