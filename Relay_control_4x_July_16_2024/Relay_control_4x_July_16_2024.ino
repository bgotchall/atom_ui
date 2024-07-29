#include <Wire.h>
#include "SparkFun_Qwiic_Relay.h"
#define RELAY_ADDR 0x6D

//This works with "quad_relay_control.py"

//Qwiic_Relay relay(RELAY_ADDR); 
Qwiic_Relay quadRelay(RELAY_ADDR); 

int x;
int i;
char this_byte;
String text_in;


void setup() {
  Wire.begin();
  Serial.begin(115200);
  Serial.setTimeout(1);
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.println("Arduino: Hello world.");
   

            
   // Let's see
  if(!quadRelay.begin()) {
    Serial.println("Arduino: Check connections to Qwiic Relay.");
  }
  else {
    Serial.println("Arduino: Ready to flip some switches.");
  }

}


void loop() {
   while (!Serial.available());
  x = Serial.readString().toInt();          //this is the working version, for 0, 1 and x
  Serial.flush();
 

  
    if (x==1) {
     // Serial.println("Arduino: got a 1, turning vacuum line on");         //These would be really nice, but it doesn't work.  they lag in infuriating ways.
      
      quadRelay.toggleRelay(1); 
      delay(200);
      Serial.print("Vacuum line is now: ");
      // Is the relay on or off?
      int state = quadRelay.getState(1);
      if(state == 1)
        Serial.println("On!");
      else if(state == 0)
        Serial.println("Off!");
      delay(1000);
    } 

  if (x==2) {
     // Serial.println("Arduino: got a 1, turning vacuum line on");         //These would be really nice, but it doesn't work.  they lag in infuriating ways.
     
      quadRelay.toggleRelay(2); 
      delay(200);
      Serial.print("Test site purge air is now: ");
      // Is the relay on or off?
      int state = quadRelay.getState(2);
      if(state == 1)
        Serial.println("On!");
      else if(state == 0)
        Serial.println("Off!");
      delay(1000);
    } 

 if (x==3) {
     // Serial.println("Arduino: got a 1, turning vacuum line on");         //These would be really nice, but it doesn't work.  they lag in infuriating ways.
     
      quadRelay.turnRelayOn(3); 
      delay(200);
      quadRelay.turnRelayOff(3); 
      Serial.print("Start Button was pressed for 200ms ");
      delay(1000);
    } 

if (x==5) {
     // Serial.println("Arduino: got a 1, turning vacuum line on");         //These would be really nice, but it doesn't work.  they lag in infuriating ways.
    int state = quadRelay.getState(1);
     if(state == 1)
        Serial.println("|Vac line is            | On  |");
      else if(state == 0)
        Serial.println("|Vac line is            | Off |");
    
    delay(100);
     state = quadRelay.getState(2);
     if(state == 1)
        Serial.println("|Test site purge air is | On  |");
      else if(state == 0)
        Serial.println("|Test site purge air is | Off |");
    } 




}