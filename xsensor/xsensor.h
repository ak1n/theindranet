#ifndef xsensor_h
#define xsensor_h

/*
theindranet: xsensors project
http://www.theindranet.com

by ak1n, janu5, keystroke, arrguile
2014-2015

license: Creative Commons Attribution-ShareAlike 4.0 International License (http://creativecommons.org/licenses/by-sa/4.0/)
based on: Eric Tsai's code written in 2014: https://github.com/homeautomationyay/OpenHab-RFM69
*/

#include <Arduino.h>
#include <NewPing.h> //ultrasound sensor library - code.google.com/p/arduino-new-ping/downloads/detail?name=NewPing_v1.5.zip
#include <DHT.h> //temperature/humidity sensor library
#include <RFM69.h>

class xsensor {
  public:
	xsensor(int pin, int &sensorCount); //constructor
	void incrementSensorCount(int &sensorCount);
	virtual void setup(); //run once in arduino setup f'n
	void loop(boolean &firstLoop, boolean &oneSensorRefreshed, RFM69 radio, uint8_t NODE_ID, uint8_t GATEWAY_ID, char* ENCRYPT_KEY, int transmission_delay); //arduino loop
	virtual void updateSensorState(boolean &oneSensorRefreshed);
	virtual bool detectStateChange();
	void setPrevState();
	bool timeToRefreshSensor(boolean &firstLoop, String sensorTypeName);
	void reportSensorStates();
	void transmit(int state, RFM69 radio, uint8_t NODE_ID, uint8_t GATEWAY_ID, char* ENCRYPT_KEY, int transmission_delay);
	void transmit(int state, RFM69 radio, uint8_t NODE_ID, uint8_t GATEWAY_ID, char* ENCRYPT_KEY, int transmission_delay, int stateTwo);
	void settimes(int new_refresh, int new_transmit_change, long new_transmit_nochange);
	
	String _sensorName; //e.g. "my_pir_sensor"
	String _sensorTypeName; //sensortype - e.g. temphumid, rangefinder, pir, sound

	int _pin; //pins - note that some devices have multiple pins and there will be a primary pin that identifies the device 
	
	String _sensorStatesKey;
	int _state_cur;
	int _state_prev;
	
	int _state_two_cur; //re multiple states: obviously this is a shitty way to do this...ideally would have arrays and cycle through them
	String _sensorStatesKey_two;
	
	//refresh/transmit times - these are user-modifiable w initialization
	//note: could change refresh/transmit times based on plug/battery power
	int _refresh=0; //frequency that sensor should acquired data
	int _transmit_change=500; //frequency that sensor should transmit data if state change detected
	long _transmit_nochange=300000; //frequency that sensor should transmit data if no state change detected
	
	unsigned int _refreshesToTransmit=1;
	unsigned int _refreshCount=0;
	unsigned int _changeTolerance=0;
	
	/*
	C really seems to suck with regard to handling dynamic arrays - or we've gotten spoiled w dynamic memory mgt in newer languages...
	array of stateVars (e.g. reed state <0>/<1>, temps <37.0>, etc.)
	array of stateVarNames (e.g. <"temperature">, <"reed state">)
	*/

	//not needed to be user-modifiable
	unsigned long _time_lastRefresh; //when sensor last acquired data
	unsigned long _time_lastTransmit; //when sensor data last transmitted
};

/*
//node class (~sensor collection; for easier init/looping) - not yet used
class node_xsensor {
	int _num_sensors;
	//array of sensors
};
*/

//individual sensor-type classes
//reedswitch sensor
class reedswitch : public xsensor {
	public:
    	reedswitch(int pin, String name, int &sensorCount);
	    void setup();
		//note: 1 = closed, 0 = open
};

//pir/motion sensor
//note: to test point pir at ceiling and turn both knobs all the way counter-clockwise (decrease time interval and sensitivity)
class pir_xsensor : public xsensor {
	public:
    	pir_xsensor(int pin, String name, int &sensorCount);
	    void setup();
};

//sound sensor
class sound_xsensor : public xsensor {
	public:
    	sound_xsensor(int pin, String name, int &sensorCount);
		sound_xsensor(int pin, String name, int &sensorCount, int refreshInterval, int refreshesToTransmit);
		void setup();
};

//ultrasonic rangefinder
class ultrason_xsensor : public xsensor {
	public:
    	//ultrason_xsensor(int pin_echo, int pin_trg, String name);
		ultrason_xsensor(int pin_echo, int pin_trg, String name, unsigned int ultrason_dist_tolerance, int &sensorCount);
		const int max_distance = 400; // max dist in cm to ping for (max sensor dist rated at 400-500cm), could setup to be more variable/customizable
		unsigned int _ultrason_dist_tolerance=2;
		  //distance in cm that will be considered margin of error/variability for transmitting data
		  //i.e. if two consective measurements are 73cm and 74cm, tolerance  of 2cm will consider these to be the same
		
		NewPing _xultrason;
		void setup();
		//note main pin will be echo pin (input pin)
		int _pin_trg; //outgoing pin pin =pin_trg
		void updateSensorState(boolean &oneSensorRefreshed);
		bool detectStateChange();
};

//DHT - digital humidity temperature sensor
class dht_xsensor : public xsensor { //
	public:
		dht_xsensor(int pin, uint8_t TYPE, String name, int &sensorCount);
		DHT _xdht;
	    void setup();
		void updateSensorState(boolean &oneSensorRefreshed);

/*
for ref from DHT library:
#define DHT11 11
#define DHT22 22 ?(AM2302) blue one
#define DHT21 21 ?(AM2301) white one
#define AM2301 21
*/

};

#endif



