#include <Wire.h>
#include "SparkFun_Qwiic_Relay.h"
#define RELAY_ADDR 0x18 // Alternate address 0x19

Qwiic_Relay relay(RELAY_ADDR); 

/******************************************************************************************
Jan 3:  This is the code that goes into an Arduino nano, that just listens on the com port
and switches the relays on and off.  

Jan 3 status:  This is just controlling 1 relay.  When I get the x4 relay I will expand it.

Truth table:   (the numbers are just strings sent over com4)
1: Relay 1 on
2: Relay 1 off
3: Relay 2 on
4: Relay 2 off
5: Relay 3 on
6: Relay 3 off
7: Relay 4 on
8: Relay 4 off
******************************************************************************************/

int x;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(1);
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);


   // Let's see
  if(!relay.begin())
    Serial.println("Check connections to Qwiic Relay.");
  else
    Serial.println("Ready to flip some switches.");

  float version = relay.singleRelayVersion();
  Serial.print("Firmware Version: ");
  Serial.println(version);
}

void  loop() {

  
  while (!Serial.available());
  x = Serial.readString().toInt();
  if (x==1) {
    Serial.println("got a 1");
    Serial.println(x);
    digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
    relay.turnRelayOn(); 
  } else {
    Serial.println("something other than 1");
    digitalWrite(LED_BUILTIN, LOW);   // turn the LED off by making the voltage LOW
    relay.turnRelayOff();

  }
  
}