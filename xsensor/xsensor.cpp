/*
theindranet: xsensors project
http://www.theindranet.com

by ak1n, janu5, keystroke, arrguile
2014-2015

license: Creative Commons Attribution-ShareAlike 4.0 International License (http://creativecommons.org/licenses/by-sa/4.0/)
based on: Eric Tsai's code written in 2014: https://github.com/homeautomationyay/OpenHab-RFM69
*/

#include "xsensor.h"

#include <Arduino.h>
#include <NewPing.h> //ultrasound sensor library - code.google.com/p/arduino-new-ping/downloads/detail?name=NewPing_v1.5.zip
#include <DHT.h> //temperature/humidity sensor library
#include <RFM69.h>

bool showTransmissions=false; //for debugging

xsensor::xsensor(int pin, int &sensorCount) //constructor for sensor class
{
	_pin = pin; //assign passed pin var to sensor instance variable

	_state_cur = NULL; //for reed: 1 = closed, 0 = open
	_state_prev = NULL;
	_state_two_cur = NULL; //for sensors with multiple variables (e.g. temp/humidity sensors)

	//set default values
	_refresh=0; //refresh interval for sensor - i.e. how frequently sensor probed
	_transmit_change=500; //time interval for broadcast if change in sensor value
	_transmit_nochange=300000; //time interval for broadcast if no change in sensor value
	_refreshesToTransmit=1; //number of cycles w changed value before transmitting - not yet functional
	_refreshCount=0; //not yet functional
	_changeTolerance=0; //difference from last value required to be considered change for transmit (0=any change)

	_time_lastRefresh=0; //time since last sensor refresh for this sensor
	_time_lastTransmit=0; //time since last transmission for this sensor
	
	_time_lastRefresh = millis(); //on creation of sensor instance set last refresh to now, as should check sensor on creation
	_time_lastTransmit = millis(); //on creation of sensor instance set last transmit to now, as should check sensor and transmit on creation
	
	incrementSensorCount(sensorCount); //keep track of how many sensors created
}

void xsensor::incrementSensorCount(int &sensorCount) {
	sensorCount++;
}

void xsensor::settimes(int new_refresh, int new_transmit_change, long new_transmit_nochange) { //override default values
    _refresh = new_refresh;
    _transmit_change = new_transmit_change;
    _transmit_nochange = new_transmit_nochange;
}

//--------------------------
//child class constructors
//--------------------------
reedswitch::reedswitch(int pin, String name, int &sensorCount):xsensor(pin,sensorCount) { // reed switch sensor
	_sensorTypeName = "reed";
	_sensorStatesKey = " (0=low=open / 1=hi=closed)";
	_sensorName = name;
}

dht_xsensor::dht_xsensor(int pin, uint8_t TYPE, String name, int &sensorCount):_xdht(pin,TYPE),xsensor(pin,sensorCount) { // temp/humidity sensor
	_sensorTypeName = "DHT";
	//String degreeSymbol = char(176); //unfortunately string concatenation breaks the fucking library...prob w string library or with code here?
	_sensorStatesKey = "F degrees";
	_sensorStatesKey_two = "\% humidity";
	_sensorName = name;
	settimes(3000,3000,300000);
		//broadcast every 3s unless no change (then q 5min)
		//ideally would broadcast if within ~a few degrees change, with an additional variance variable added to sensor class
}

pir_xsensor::pir_xsensor(int pin, String name, int &sensorCount):xsensor(pin,sensorCount) { // pir sensor
	_sensorTypeName = "pir";
	_sensorStatesKey = " (1=movement, 0=no movement)";
	_sensorName = name;
	settimes(1000,500,1800000);
}

sound_xsensor::sound_xsensor(int pin, String name, int &sensorCount):xsensor(pin,sensorCount) { // sound sensor
	_sensorTypeName = "sound";
	_sensorStatesKey = " (0=noise, 1=no noise)";
	_sensorName = name;
	settimes(100,100,1800000);
}

sound_xsensor::sound_xsensor(int pin, String name, int &sensorCount, int refreshInterval, int refreshesToTransmit):xsensor(pin,sensorCount) { //sound sensor w extra params - note that refresh count functionality not yet working/finished
	sound_xsensor(pin,name,sensorCount,refreshInterval,refreshesToTransmit);
	settimes(refreshInterval,refreshInterval,refreshInterval);
	_refreshesToTransmit=refreshesToTransmit;
}

ultrason_xsensor::ultrason_xsensor(int pin_echo, int pin_trg, String name, unsigned int ultrason_dist_tolerance, int &sensorCount):_xultrason(pin_trg, pin_echo, max_distance),xsensor(pin_echo,sensorCount) { // pir sensor
	_sensorTypeName = "ultrasonic dist sens";
	_sensorStatesKey = " (cm)";
	_sensorName = name;
	//_xultrason; //; // NewPing setup of pins and maximum distance.
	//note main pin will be echo pin (input pin)
	int _pin_trg=pin_trg; //outgoing pin 
	_ultrason_dist_tolerance=ultrason_dist_tolerance;
	settimes(5000,5000,5000); //would assume setting refresh too low would not allow time for sensor to ping and wait for response for distance calc
}

//need create alternative constructor sans dist tolerance
//ultrason_xsensor(int pin_echo, int pin_trg, String name);

//------  ------  ------//

//node setup to be run once
void xsensor::setup()
{
	//this function needs to be able to be overridden by subclass functions
	Serial.println("sensor setup function called");

	pinMode(_pin, INPUT); //initialize pin - NOTE: for some sensors this is handled in associated included class libraries
	
	//consider here calling setup(0) and moving any additional code to other setup fn
	
	//******should loop be called here initially, so that initial values are sent to gateway for sensors?*******//
}

/*
//setup functions for sensors where pin initialization is handled
void xsensor::setup(boolean suppressPinInit) {

}
*/

//consider consolidating the following by passing sensor type name to setup fn
void reedswitch::setup() {
  Serial.println("reedswitch setup called"); //should be able to pull sensor name from class and consolidate all of these prints
  xsensor::setup();
}

void pir_xsensor::setup() {
  Serial.println("pir setup called");
  xsensor::setup();
}

void sound_xsensor::setup() {
  Serial.println("sound setup called");
  xsensor::setup();
}

void ultrason_xsensor::setup() {
  Serial.println("ultrason setup called");
  pinMode(_pin, INPUT); //ultrasonic distance sensor input put initialization
  pinMode(_pin_trg, OUTPUT); //initialize trg output pin
  //******nl setup fn in ultrasound class library function rather than xs?????*******//
  //xsensor::setup();
}

void dht_xsensor::setup() {
  Serial.println("dht sensor setup called");
  _xdht.begin(); //initialize from dht library class function
  //xsensor::setup();
}

//------  ------  ------//

void xsensor::updateSensorState(boolean &oneSensorRefreshed) {
	//this function needs to be able to be overridden by subclass functions
	//Serial.println("xsensor updateSensorState called");
  	_state_cur = digitalRead(_pin); //assuming int has binary val 0 or 1, may have to use conditionals hi/low and assign binary state if that's wrong
	//need address multi pins here
	//Serial.print("xsensor pin status=");
	//Serial.println(_state_cur);
	oneSensorRefreshed=true;
	_time_lastRefresh = millis();
}

void dht_xsensor::updateSensorState(boolean &oneSensorRefreshed) {
	//Serial.println("dht updateSensorState called");
	
	float h = _xdht.readHumidity();
	float tc = _xdht.readTemperature(); // Read temperature as Celsius - currently not used but could set flag in config file to switch F/C (or both)
	float tf = _xdht.readTemperature(true); // Read temperature as Fahrenheit

	// Check if any reads failed and exit early (to try again).
	if (isnan(h) || isnan(tc) || isnan(tf)) {
		Serial.println("Failed to read from DHT sensor!");
		return; //modify to throw more organized exception back here?
	}
	
	//round floats to nearest integer...this is not ideal. would be better to get floats to server via another route
	_state_cur = int(tf+0.5); 
	_state_two_cur = int(h+0.5);
	
	oneSensorRefreshed=true;
	_time_lastRefresh = millis();

/*
	Serial.print("temp=");
	Serial.print(tf);
	Serial.print("F, ");
	Serial.print(tc);
	Serial.print("C, ");
	Serial.print("humid=");
	Serial.print(h);
	Serial.println(""); 
*/
}

void ultrason_xsensor::updateSensorState(boolean &oneSensorRefreshed) {
	//Serial.println("ultrason updateSensorState called");
	/*Serial.println("");
	Serial.print("ultrasonic dist sens: ");
	Serial.print(_state_cur);
	Serial.println(" cm");*/
	unsigned int us_ping_time = _xultrason.ping(); // Send ping, get ping time in microseconds (uS);
	_state_cur = us_ping_time / US_ROUNDTRIP_CM; // convert ping time to distance (0 = outside set distance range, no ping echo)
}

//------  ------  ------//

bool xsensor::detectStateChange() { //returns true if state has changed
	//may eventually incorporate change tolerance class variables here (i.e. how MUCH change should flip change switch for non-bool vars?)
	if(_state_cur != _state_prev) return true;
	else return false;
}

bool ultrason_xsensor::detectStateChange() {
	//ascertain if change within tolerance parameters
    int distChange = abs(_state_cur - _state_prev);
	/*Serial.print("distChange=");
	Serial.print(distChange);
	Serial.print(", tol=");
	Serial.print(_ultrason_dist_tolerance);*/
    if(distChange > _ultrason_dist_tolerance) return true;
	else return false;
}

//------  ------  ------//

void xsensor::reportSensorStates() {
	//Serial.println("sensor state fn called");
	Serial.print(_sensorName);
	Serial.print(" (");
	Serial.print(_sensorTypeName);
	Serial.print(" type) = ");
	Serial.print(_state_cur);
	Serial.print(_sensorStatesKey); //for conditional ID state can also do: if(reed_state == HIGH) or LOW (latter for open)
	if(_state_two_cur != NULL) {
		Serial.print(", ");
		Serial.print(_state_two_cur);
		Serial.print(_sensorStatesKey_two);
	}
}

void xsensor::setPrevState() {
	_state_prev = _state_cur;
}

//------  ------  ------//
void xsensor::loop(boolean &firstLoop, boolean &oneSensorRefreshed, RFM69 radio, uint8_t NODE_ID, uint8_t GATEWAY_ID, char* ENCRYPT_KEY, int transmission_delay)
{
	//Serial.println("sensor loop function called");
	
	if(timeToRefreshSensor(firstLoop,_sensorTypeName)) {		
	
		updateSensorState(oneSensorRefreshed);
	
		reportSensorStates();
	
		boolean transmitting = false;
		
		if(firstLoop) {
	  		Serial.print(", first loop");
			setPrevState();
	  		transmitting=true;
		}
		else {
	  		long timechange = millis() - _time_lastTransmit;
			if(!detectStateChange()) {
	    		Serial.print(", unchanged");
	    		if( timechange > _transmit_nochange ) {
	      			Serial.print(", transmit threshold met");
	      			transmitting=true;
	    		}
	  		}
	  		else {
	    		Serial.print(", CHANGED");
	    		if( timechange > _transmit_change ) {
	      			Serial.print(", transmit threshold met");
	      			transmitting=true;
	    		}
	    		setPrevState(); //was: _reed_previous=_reed_state; //need to rename to abstract to sensor class
	  		}
		}
		//separate transmission into separate f'n
	  	if(transmitting) {
			transmit(_state_cur, radio, NODE_ID, GATEWAY_ID, ENCRYPT_KEY, transmission_delay, _state_two_cur);
		}
		Serial.println("");
		
	} //end if refresh criteria met
/*
  Serial.print("times: ");
  Serial.print(refresh);
  Serial.print(", ");
  Serial.print(transmit_change);
  Serial.print(", ");
  Serial.print(transmit_nochange);
  Serial.println("");*/
} //end xsensor loop

bool xsensor::timeToRefreshSensor(boolean &firstLoop, String sensorTypeName) {
	boolean will_refresh = false;
	if( ((millis() - _time_lastRefresh) > _refresh) || firstLoop) {
		
	/*
		Serial.print("sensor \"");
		Serial.print(_sensorName);
		Serial.print("\" (");
		Serial.print(sensorTypeName);
		Serial.print(" type): ");*/
		
		if(_refreshesToTransmit == 1) {
			will_refresh = true;
		}
		else {
			/*
			//this needs finishing...code does not belong here but in another fn as this fn only evals time (not state-change)
			if(_refreshCount > _refreshesToTransmit) {
				will_refresh = true;
			}
			*/
			will_refresh = true;
		}
	}
	return will_refresh;
}

/*
void reedswitch::loop(boolean &firstLoop, boolean &oneSensorRefreshed, RFM69 radio, uint8_t NODE_ID, uint8_t GATEWAY_ID, char* ENCRYPT_KEY, int transmission_delay) {
	xsensor::loop();
	//xsensor::loop(boolean &firstLoop, boolean &oneSensorRefreshed, RFM69 radio, uint8_t NODE_ID, uint8_t GATEWAY_ID, char* ENCRYPT_KEY, int transmission_delay);
} //end reed loop
*/

//--------------------------------------
void xsensor::transmit(int state, RFM69 radio, uint8_t NODE_ID, uint8_t GATEWAY_ID, char* ENCRYPT_KEY, int transmission_delay) {
	transmit(_state_cur, radio, NODE_ID, GATEWAY_ID, ENCRYPT_KEY, transmission_delay, NULL);
}

void xsensor::transmit(int state, RFM69 radio, uint8_t NODE_ID, uint8_t GATEWAY_ID, char* ENCRYPT_KEY, int transmission_delay, int stateTwo) {
	//uint8_t NODE_ID, uint8_t GATEWAY_ID, uint8_t ENCRYPT_KEY, int transmission_delay
	
	//we are aware that declaring and using this struct here is a shitty way of doing things
	//do not yet know how to do this better re efficiency/memory/etc
	//struct is in dire need of rehashing
	//worth it to convert to JSON format? would mean a lot more data across radio, but prob worth it
		//could use json and then define a server/node index for json to be reduced to small ints?
	//at minimum should rename all these variables to make more sense
	
	//struct for wireless data transmission
	typedef struct {		
		unsigned int       nodeID; //node_id; 2 digits
		unsigned int       sensorID; //1 digit, main sensor pin
		unsigned long   var1_usl; 		//uptime in ms, unsigned means variable won't go below zero ("no sign")
		float     var2_float; //main sensor data variable - primary sensor state
		float     var3_float; //secondary sensor data variable - secondary sensor state
	} Payload;
	Payload theData; //create instance of payload struct for passing to radio library functions
	theData.nodeID = NODE_ID;  //this node id should be the same for all devices in this node
	
	Serial.println("");
	Serial.print("transmitting: ");
	_time_lastTransmit = millis();  //update reed_time_send with when sensor value last transmitted
	theData.sensorID = _pin;
	theData.var1_usl = millis();
	theData.var2_float = state;
	theData.var3_float = stateTwo;		//will be null if have no data to pass
	if(showTransmissions) {
		Serial.print("transmit theData string: node_id=");
		Serial.print(NODE_ID);
		Serial.print(", device_id (_pin)=");
		Serial.print(_pin);
		Serial.print(", millis=");
		Serial.print(millis());
		Serial.print(", state=");
		Serial.print(state);
		Serial.print(", stateTwo=");
		Serial.print(stateTwo);
		Serial.print(", gateway id=");
		Serial.println(GATEWAY_ID);
	}
	radio.sendWithRetry(GATEWAY_ID, (const void*)(&theData), sizeof(theData));	//const void* = a pointer that points to theData variable (buffer)	
	//from library:    bool RFM69::sendWithRetry(byte toAddress, const void* buffer, byte bufferSize, byte retries, byte retryWaitTime) 
	Serial.print("transmit done");
	delay(transmission_delay);
}


