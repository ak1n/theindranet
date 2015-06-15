'''
theindranet: xsensors project
http://www.theindranet.com

by ak1n, janu5, keystroke, arrguile
2014-2015

license: Creative Commons Attribution-ShareAlike 4.0 International License (http://creativecommons.org/licenses/by-sa/4.0/)
based on: Eric Tsai's code written in 2014: https://github.com/homeautomationyay/OpenHab-RFM69
'''

'''
ak1n public PGP key

Public Key Server -- Get "0xdaec87bcc47b78a6 "

-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: SKS 1.1.5
Comment: Hostname: pgp.mit.edu

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
EOE2yvU=
=h45/
-----END PGP PUBLIC KEY BLOCK-----
'''

import json, os,string

debugMode=0

output_dir = "output/" #include trailing "/"
"""
note that the following libraries are required:
	-xsensor library (should be included with this file)
	-RFM69 - radio library
	-NewPing - if using ultrasound sensor, library at: code.google.com/p/arduino-new-ping/downloads/detail?name=NewPing_v1.5.zip
	-DHT - if using temperature/humidity sensor
	(note: even if not using these sensors, the includes are called for in generated code here)

output files:
	wireless gateway arduino file (.ino)
	ethernet gateway arduino file (.ino)
	".ino" file for each node (will be named based on node name put in config file)
	openhab configuration files: items, sitemap, rules
"""

print """
**=====================================================**
**=====================================================**
              xsensor startup script				
**=====================================================**
**=====================================================**
"""


#first verify can access input files

sclass_suffix = "_xsensor" #don't mess with this (correlates w xsensor library)
openhab_project_name="xsensors" #can override with config file
oh_server_url="tcp://localhost:1883" #will override with config file

#following defines variable keys for radio broadcasts
#this is CERTAINLY a bad way of doing things, will attempt re-visiting later
#should prob either use long var names and take the hit re memory/power usage (because will broadcast more redundant data) or setup clearer id/key-value system
def_sens_subId_prim = "2" #default sub id for sensor nodes. e.g. ID initially: 2-digit node ID, then sensor pin, then another number (this one)
def_sens_subId_sec = "3" #secondary sub id for sensor nodes

gateway_radio_id="1"
gateway_ethernet_address="42" #don't know exactly how this works, but address seems required for I2C communication...see where used below

num_nodes=0

if debugMode: #this may be of utility if having memory/sensor-dying issues
	debugCodeLoop="""
if(debugMode) {
	if((millis() - time_since_debug_check) > 10000) {
		long livetimesec=(millis()/1000);
		Serial.print("time node has been active: ");
		//if(livetimesec < 60) {
			Serial.print((livetimesec));
			Serial.print(" s");
		//}
	
		if(livetimesec > 60) {
			Serial.print(" = ");
			if(livetimesec > 86400) {
				Serial.println((livetimesec/86400));
				Serial.println(" days");
			}
			else if(livetimesec > 3600) {
				Serial.println((livetimesec/3600));
				Serial.print(" hrs ");
				Serial.print((livetimesec%3600)/60);
				Serial.println(" min");
			}
			else {
				Serial.print((livetimesec/60));
				Serial.print(" min ");
				Serial.print((livetimesec%60));
				Serial.println(" s");
			}
		}
		else Serial.println("");
	
		Serial.print("available ram: ");
		Serial.println(free_ram()); //https://learn.adafruit.com/memories-of-an-arduino/measuring-free-memory
		time_since_debug_check=millis();
  	}
  }
	"""
	debugCodeHeader="""
boolean debugMode=1;
long time_since_debug_check=0;

int free_ram () //space btwn heap and stack, https://learn.adafruit.com/memories-of-an-arduino/measuring-free-memory
{
  extern int __heap_start, *__brkval; 
  int v; 
  return (int) &v - (__brkval == 0 ? (int) &__heap_start : (int) __brkval); 
}
	"""
else: debugCodeHeader=debugCodeLoop=""

#openhab file prep
oh_sitemap_file="sitemap mqttsec label=\"xsensors\" {\n"
oh_sitemap_post = "}"
oh_sitemap_groups="Frame label=\"network nodes\" {"
oh_sitemap_sensors=""
oh_sitemap_alarms="Frame label=\"sensor statuses\" {\n"
oh_items_file=""
oh_items_groups="Group All\n"
oh_items_sensors=""
oh_rules_file="""import org.openhab.core.library.types.*
import org.openhab.core.persistence.*
import org.openhab.model.script.actions.*
"""

def ensure_folder(loc): #checks if folder exists, creates if it doesn't exist
	directory_exists=1
	try:
		d = os.path.dirname(loc)
		if not os.path.exists(d): #also works: if not os.path.isdir(d):
			#print "directory '"+d+"' does not exist"
			directory_exists=0
	except:
		print "problem attempting to access file system to create directories for arduino files"
		directory_exists=0
		return 0
	else:
		if not directory_exists:
			print "directory '"+d+"' not found, attempting to create..."
			try:
				os.mkdir(d)
			except:
				print "unable to create directory"
				return 0
			else:
				print "successfully created directory"
				return 1
		else:
			print "directory "+d+" exists"
			return 1

def email_notify(): #have not gotten working yet
	#ensure have sufficient data from config file
	have_mail_vars[0]=[1]
	hostname=getjvar("email_sender_server",have_mail_vars)
	port=getjvar("email_sender_outgoing_port",have_mail_vars)
	username=getjvar("email_sender_username",have_mail_vars)
	password=getjvar("email_sender_password",have_mail_vars)
	receipient=getjvar("email_receipient",have_mail_vars)
	
	if have_mail_vars[0]:
		oh_config_mail="""
mail:hostname=smtp.gmail.com
mail:port=587
mail:username=????? without the @gmail
mail:password=?????
mail:from=??? yourname@gmail.com
mail:tls=true		
		"""
	else: print "do not have enough config data to setup email notifications"

def setup_node(json_node, node_name): #will be called for each node definition found in config file, generates arduino/openhab files for each node
	global oh_sitemap_file, oh_sitemap_groups, oh_sitemap_sensors, oh_sitemap_alarms, oh_items_groups, oh_items_sensors, oh_rules_file
	global network_id,gateway_id,encrypt_key,radio_frequency,global_loop_delay,transmission_delay,is_RFM69HW_code
	
	print "processing json_node \"" + node_name + "\" with content of: " + str(json_node) + "\n"
	
	node_enabled=1 #can be overriden by config file for easier debugging
	
	#stop processing if "enabled" flag is 0
	if "enabled" in json_node:
		if json_node["enabled"] is 0:
			node_enabled=0
			print "node is disabled, so not processing it further\n"
	
	if node_enabled is 1:
		#validate node - make sure have sensor data
		sufficient_node_data=1
		if "sensors" not in json_node:
			print "sensors not found in json config file"
			sufficient_node_data=0
		elif "node_id" not in json_node:
			print "node_id not found for node (this is required)"
			sufficient_node_data=0
		
		if(sufficient_node_data):
			print "have sufficient data for node_id "+json_node["node_id"]
			sens_constructs=[]
			firstItem = 1
			sensorArrayCode = "xsensor *sensorArr[]={"
			json_sensors = json_node["sensors"]
			node_id=json_node["node_id"]
			oh_sitemap_these_sens=""
		
			#group related code (i.e. for grouping things in openhab since openhab's refresh sucks if it's a large page w page position lost)
			oh_sitemap_groups+="\nGroup item="+node_name+" label=\""+node_name+"\""
			#oh_sitemap_these_sens+="Group item="+node_name+" label=\"view only "+node_name+"\"\n"
			oh_items_groups+="Group "+node_name+" <network> (ALL)\n"
			this_grp_suf=" ("+node_name+",ALL)" #this sensor's group suffix
		
			update_time_var_type="DateTime"
		
			nodeUpdateVar="xs_"+node_name+"_lastUpdate"
			
			icon_interp="<keyring>"
			
			oh_items_sensors+=update_time_var_type+" "+nodeUpdateVar+" \"last node update: [%1$tm/%1$td, %1$tI:%1$tM %1$tp]\" <clock>"+this_grp_suf+"\n"
			oh_sitemap_these_sens+="Text item="+nodeUpdateVar+"\n"
		
			oh_rules_node_suffix="postUpdate("+nodeUpdateVar+", new "+update_time_var_type+"Type())"	
		
			for item in json_sensors: #cycle through sensors
				print item + ": " + str(json_sensors[item])
				varname = item
				name = str(json_sensors[item]['name'])
				type = str(json_sensors[item]['type'])
				pin = str(json_sensors[item]['pin'])
				
				print "varname is "+varname
				print "type is "+type
				print "pin is "+pin
				construct=-1
		
				if(firstItem):
					firstItem = 0
					sensorArrayCode+= ("&"+varname)
				else:
					sensorArrayCode+= (",&"+varname)
			
				sens_prefix="xs_"+node_name+"_"+varname
				sens_mqtt=sens_prefix+"_mqtt"
				sens_id_prefix=node_id+pin
				
				sens_alm_sta=sens_prefix+"_alma_sta"
				sens_state=sens_prefix+"_state"
				
				oh_rules_actions="" #resets every sensor, with appending oh_rules
				
				#check for alert configurations								
				if "actions" in json_sensors[item]:
					print "\nhave actions"
					if "open" in json_sensors[item]['actions']:
						print "have open action"
						if "xmpp" in json_sensors[item]['actions']['open']:
							#should verify here if have global xmpp config variables
							if have_xmpp_vars:
								if "recipient" in json_sensors[item]['actions']['open']['xmpp']:
									xmpp_recipient=json_sensors[item]['actions']['open']['xmpp']['recipient']
									if "message" in json_sensors[item]['actions']['open']['xmpp']:
										xmpp_message=json_sensors[item]['actions']['open']['xmpp']['message']
										xmpp_message=string.replace(xmpp_message,"****sensorname****",varname)
									else: xmpp_message="openhab event - sensor name: %s (type: %s) - action: switch opened" % (varname,type)
									oh_rules_actions="""
rule "%s email"
	when
		Item %s changed from OFF to ON
	then
		postUpdate(%s, "OPENED - should msg xmpp")
		sendXMPP("%s", "%s")
end
									""" % (sens_mqtt,sens_alm_sta,sens_state,xmpp_recipient,xmpp_message)
									print "have xmpp open action w designated recipient, as well as global xmpp config data found in config file"
								else: print "no recipient found for xmpp open action"
							else: print "found xmpp open action, but xmpp global configuration not found in config file"
						else: print "have open action but no handling method/medium"
					else: print "do not have open action"
				else: print "do not have actions\n"
				
				"""
					if str(json_sensors[item]['actions']['open']):
						if str(json_sensors[item]['actions']['open']['xmpp']):
							if str(json_sensors[item]['actions']['open']['xmpp']['message']):
								print "have sufficient information to set xmpp open action for sensor"
							else: print "error xmpp open actino set for sensor, but without message specified\n"
						else: print "error: open action set for sensor, but w/o an appropriate medium to handle action\n"
					else: print "error: actions field set but without open action for sensor\
				"""
				#if actions: print "actions\n"
				#else: print "no actions\n"
				
				#vars for last update time of sensor
				sens_time=sens_prefix+"_time"
				sens_time_item=update_time_var_type+" "+sens_time+" \"last "+type+" check: [%1$tm/%1$td, %1$tI:%1$tM %1$tp]\" <clock>"+this_grp_suf+"\n"
				sens_time_rule_line="postUpdate("+sens_time+", new "+update_time_var_type+"Type())"
				sens_time_sitemap="Text item="+sens_time+"\n"
		
				if type == "dht":
					model = str(json_sensors[item]['model'])
					sens_dht_temp=sens_prefix+"_temp_mqtt"
					sens_dht_humi=sens_prefix+"_humidty_mqtt"
					construct = type + sclass_suffix + " " + varname + "(" + pin +"," + model + ",\"" + name + "\",sensorCount);"
					oh_items_sensors+="Number "+sens_prefix+"_temp_mqtt \"temp [%.1f] F\" <temperature>"+this_grp_suf+" {mqtt=\"<[localbroker:"+sens_id_prefix+def_sens_subId_prim+":state:default]\"}\n"
					oh_items_sensors+="Number "+sens_prefix+"_humidity_mqtt \"humidity [%.1f] %\" <temperature>"+this_grp_suf+" {mqtt=\"<[localbroker:"+sens_id_prefix+def_sens_subId_sec+":state:default]\"}\n"
					oh_items_sensors+=sens_time_item
					oh_sitemap_these_sens+="Text item="+sens_prefix+"_temp_mqtt\n"
					oh_sitemap_these_sens+="Text item="+sens_prefix+"_humidity_mqtt\n"
					oh_sitemap_these_sens+=sens_time_sitemap
					
					#following is rule only for temp (not humid) sensor, don't see need for two rules as receive broadcast for either
					oh_rules_file+="""
	rule "%s temp trigger"
		when
			Item %s received update
		then
			%s
			%s
	end
					""" % (sens_prefix,sens_dht_temp,sens_time_rule_line,oh_rules_node_suffix)
				elif type == "sound":
					construct = "default"
					sens_state=sens_prefix+"_state"
					oh_items_sensors+=sens_time_item
					oh_items_sensors+="Number "+sens_mqtt+" \""+type+" state (mqtt): [%s]\""+this_grp_suf+" {mqtt=\"<[localbroker:"+sens_id_prefix+def_sens_subId_prim+":state:default]\"}\n"
					oh_items_sensors+="String "+sens_prefix+"_state \"sound state interp: [%s]\""+icon_interp+this_grp_suf+"\n"
					oh_sitemap_these_sens+="Text item="+sens_mqtt+"\n"
					oh_sitemap_these_sens+="Text item="+sens_prefix+"_state\n"
					oh_sitemap_these_sens+=sens_time_sitemap
					oh_rules_file+="""
	rule "%s trigger"
		when
			Item %s received update
		then
			if(%s.state == 1) //no noise from sound sensor
			{
				postUpdate(%s, "no noise (state 1)")
			}
			else //noise is detected from sound sensor
			{
				postUpdate(%s, "noise (state 0)")
			}
			%s
			%s
	end
					""" % (sens_prefix,sens_mqtt,sens_mqtt,sens_state,sens_state,sens_time_rule_line,oh_rules_node_suffix)
				
				elif type == "ultrason":
					pin_trg = str(json_sensors[item]['pin_trg'])
					dist_tolerance = str(json_sensors[item]['dist_tolerance'])
					construct = type + sclass_suffix + " " + varname + "(" + pin + "," + pin_trg + ",\"" + name + "\"," + dist_tolerance + ",sensorCount);"
					oh_items_sensors+=sens_time_item
					#oh_items_sensors+="String "+sens_time+" \"last "+type+" check: [%1$tm/%1$td, %1$tI:%1$tM %1$tp]\""+this_grp_suf+"\n"
					oh_items_sensors+="Number " + sens_mqtt + " \""+type+" state (mqtt): [%s]\" <smartheater>"+this_grp_suf+" {mqtt=\"<[localbroker:" + sens_id_prefix + def_sens_subId_prim + ":state:default]\"}\n"
					oh_sitemap_these_sens+="Text item="+sens_mqtt+"\n"
					oh_sitemap_these_sens+=sens_time_sitemap
					oh_rules_file+="""
	rule "%s trigger"
		when
			Item %s received update
		then
			%s
			%s
	end
					""" % (sens_prefix,sens_mqtt,sens_time_rule_line,oh_rules_node_suffix)
				
				elif type == "reedswitch":
					construct = type + " " + varname + "(" + pin + ",\"" + name + "\",sensorCount);"
					oh_items_sensors+="Switch "+sens_alm_sta+" \"Reed "+node_name+"_"+varname+" open\""+this_grp_suf+"\n"
					oh_items_sensors+=sens_time_item
					#oh_items_sensors+="String "+sens_prefix+"_time \"last "+type+" check: [%1$tm/%1$td, %1$tI:%1$tM %1$tp]\""+this_grp_suf+"\n"
					oh_items_sensors+="Number "+sens_mqtt+" \"reed state (mqtt): [%s]\" <contact>"+this_grp_suf+" {mqtt=\"<[localbroker:"+sens_id_prefix+def_sens_subId_prim+":state:default]\"}\n"
					oh_items_sensors+="String "+sens_prefix+"_state \"reed state interp: [%s]\""+icon_interp+this_grp_suf+"\n"
					oh_sitemap_these_sens+="Text item="+sens_mqtt+"\n"
					oh_sitemap_these_sens+="Text item="+sens_prefix+"_state\n"
					
					oh_sitemap_these_sens+=sens_time_sitemap
					#oh_sitemap_these_sens+="Text item="+sens_prefix+"_time\n"
					oh_sitemap_alarms+="Switch item="+sens_alm_sta+" mappings=[OFF=\"Off\"]\n"
	
					oh_rules_file+="""
	rule "%s trigger"
		when
			Item %s received update
		then
			if(%s.state == 1) //reed is closed
			{
				postUpdate(%s, "closed (state 1)")
				sendCommand(%s, OFF)
			}
			else //reed is open
			{
				postUpdate(%s, "open (state 0)")
				sendCommand(%s, ON)
			}
			%s
			%s
	end
	%s
					""" % (sens_prefix,sens_mqtt,sens_mqtt,sens_state,sens_alm_sta,sens_state,sens_alm_sta,sens_time_rule_line,oh_rules_node_suffix,oh_rules_actions)
					
					"""
					rule "%s email"
						when
							Item %s changed from OFF to ON
						then
							postUpdate(%s, "OPENED - should email")
							sendXMPP("xris@dukgo.com", "openhab event - switch opened")
					end
					"""
					#,sens_mqtt,sens_alm_sta,sens_state)
					#sendMail("xx@xx.com", "openhab event" , "switch opened")
				
				elif type == "pir":
					construct = "default"
					sens_lastUpdate=sens_prefix+"_lastUpdate"
					sens_lastMotion=sens_prefix+"_lastMotion"
					sens_state=sens_prefix+"_state"
					oh_items_sensors+="Number " + sens_prefix + "_mqtt \""+type+" state (mqtt): [%s]\" <smartheater>"+this_grp_suf+" {mqtt=\"<[localbroker:" + sens_id_prefix + def_sens_subId_prim + ":state:default]\"}\n"
					oh_items_sensors+=update_time_var_type+" "+sens_prefix+"_lastMotion \"last "+type+" motion: [%1$tm/%1$td, %1$tI:%1$tM %1$tp]\" <clock>"+this_grp_suf+"\n"
					oh_items_sensors+=sens_time_item
					#oh_items_sensors+="String "+sens_prefix+"_lastUpdate \"last "+type+" update: [%1$tm/%1$td, %1$tI:%1$tM %1$tp]\""+this_grp_suf+"\n"
					oh_items_sensors+="String "+sens_state+" \"pir state interp: [%s]\""+icon_interp+this_grp_suf+"\n"
					oh_sitemap_these_sens+="Text item="+sens_mqtt+"\n"
					oh_sitemap_these_sens+="Text item="+sens_state+"\n"
					oh_sitemap_these_sens+="Text item="+sens_lastMotion+"\n"
					oh_sitemap_these_sens+=sens_time_sitemap
					oh_rules_file+="""
	rule "%s trigger"
		when
			Item %s received update
		then
			postUpdate(%s, new %sType())
			if(%s.state == 1) { //motion detected
				postUpdate(%s, "1 (motion)")
				postUpdate(%s, new %sType())
			}
			else { //no motion
				postUpdate(%s,"0 (no motion)")
			}
			%s
			%s
	end
					""" % (sens_prefix,sens_mqtt,sens_time,update_time_var_type,sens_mqtt,sens_state,sens_lastMotion,update_time_var_type,sens_state,sens_time_rule_line,oh_rules_node_suffix)
				
				if construct != -1:
					if construct == "default":
						construct = type + sclass_suffix + " " + varname + "(" + pin + ",\"" + name + "\",sensorCount);"
					print "construct is " + construct
					sens_constructs.append(construct)
					oh_items_sensors+="\n"
				else:
					print "construct is -1"
				print "\n"
			#end for each sensor
	
			num_constructs = len(sens_constructs)
			if num_constructs > 0:
				#arduino part
				sensorArrayCode+="};"
				constructs_str = '\n'.join(sens_constructs)
				customCode = constructs_str + "\n" + sensorArrayCode
			
				#-------------------------------------------------------------------------
				#start arduino file construction------------------------------------------
				arduino_node_file=""
				arduino_node_file+=codeHeaderArduino
				arduino_node_file+="""
	//includes
	#include <xsensor.h> //xsensor library import

	#include <NewPing.h> //ultrasound sensor library - code.google.com/p/arduino-new-ping/downloads/detail?name=NewPing_v1.5.zip
	#include <RFM69.h>
	#include <SPI.h>
	#include <DHT.h> //temperature/humidity sensor library

/*
	neccesary user modifications:
	-network and node variables: NODE_ID, NETWORK_ID, GATEWAY_ID, ENCRYPT_KEY
	-radio type vars: FREQUENCY, IS_RFM69HW
	-global timing variables: globalLoopDelay, transmission_delay
	-create sensor instances
	-create sensor setup and loop calls

*/

	//--------------------------define constants--------------------------//

	//unique for each node on same network - MUST CHANGE FOR EACH ARDUINO SENSOR
				"""
				arduino_node_file+="""
	#define NODE_ID  %s //unique to each arduino device on network

	//unique for each network
	#define NETWORK_ID  %s //same for all nodes that communicate w one another - is passed to radio methods
	#define GATEWAY_ID  %s //need to import from config file
	#define ENCRYPT_KEY  "%s" //same 16 chars for all nodes on network - needs higher security, need to import from config file

	      //------------ radio stuff that needs cleanup  ------------//
	//Match frequency to the hardware version of the radio on your Moteino (uncomment one):
	//should leave all these commented out here, then import from config desired one
	//#define FREQUENCY   RF69_433MHZ
	//#define FREQUENCY   RF69_868MHZ
	//#define FREQUENCY     RF69_915MHZ
	#define FREQUENCY     %s
	%s

	#define ACK_TIME      30 // max # of ms to wait for an ack
	#define SERIAL_BAUD   9600  //must be 9600 for GPS, use whatever if no GPS //don't think this is ever used - consider deletion

	//time interval globals 
	const int globalLoopDelay=%s; //delay after each main loop, setting higher makes watching serial output easier + might increase battery life (if using batteries)
	const int transmission_delay=%s; //delay in program after each radio transmission (unsure if actually necessary to be greater than 0); alt author set at 1000

	%s

	//-------------------------- end constants  --------------------------//
	//---------------------define non-constant globals--------------------//
	boolean firstLoop=1;
	long timechange; //time since sensor was last checked (will be re-assigned upon each sensor-check during loop function)
	boolean oneSensorRefreshed=0; //to see if at least one sensor refreshed during loop - important for initial sensor broadcasting and variable-setting

	char buff[20]; //buffer size of radio transmissions (for sendwithretry RFM library f'n)
	byte sendSize=0;
	boolean requestACK = false;
	RFM69 radio; //create instance of RFM library

	int sensorCount=0; //number of sensors in this node (will be incremented with creation of sensor objects)

	      //------------ create sensor instances  ------------//
	      //-------------- requires user input ---------------//
				""" % (node_id,network_id,gateway_id,encrypt_key,radio_frequency,is_RFM69HW_code,global_loop_delay,transmission_delay,debugCodeHeader)
				arduino_node_file+=customCode
				arduino_node_file+="""

	      //---------- end create sensor instances  ----------//

	//-----------------------end non-constant globals---------------------//

	void setup()
	{
	  Serial.begin(9600);          //  setup serial
	  Serial.println("starting up...");
	  Serial.println("--------------------");
	  Serial.println("--------------------");
	  //Serial.println("main setup function called");

	  //RFM69-------------------------------------------
	  Serial.println("initializing radio...");
	  radio.initialize(FREQUENCY,NODE_ID,NETWORK_ID);
	  #ifdef IS_RFM69HW
	    radio.setHighPower(); //uncomment only for RFM69HW!
	  #endif
	  Serial.println("setting up encryption...");
	  radio.encrypt(ENCRYPT_KEY);
	  char buff[50];
	  sprintf(buff, "\\nTransmitting at %d Mhz...", FREQUENCY==RF69_433MHZ ? 433 : FREQUENCY==RF69_868MHZ ? 868 : 915);
	  Serial.println(buff);

	  //end RFM--------------------------------------------

	  Serial.print("sensor count is: ");
	  Serial.println(sensorCount);

	  //cycle through sensor array to call each sensor's setup method
	  for(int i=0; i < sensorCount; i++)	sensorArr[i]->setup();


	}
				"""
				arduino_node_file+="""
	void loop()
	{
	  oneSensorRefreshed=false;
	  if(firstLoop) Serial.println("this is the first loop");

		//cycle through sensor array and call each sensor's loop method
	    for(int i=0; i < sensorCount; i++) sensorArr[i]->loop(firstLoop, oneSensorRefreshed, radio, NODE_ID, GATEWAY_ID, ENCRYPT_KEY, transmission_delay);

	  if(firstLoop) firstLoop=0;

	  %s
  
	  if(oneSensorRefreshed) Serial.println("-----------");
	  delay(globalLoopDelay);
	}
				""" % (debugCodeLoop)
			
				"""
				arduino_node_outFile.append("codeHeader.txt")
				arduino_node_outFile.append("arduino_part1.ino")
				arduino_node_outFile.append(customCode)
				arduino_node_outFile.append("arduino_part2.ino")
				finalNodeCode = arduinoPre + "\n" + customCode + arduinoPost
				print "final custom code for " + node_name + " with " + str(num_constructs) + " sensors/constructors:" + "\n" + customCode
				print "\n"
				"""
			
				print "writing constructs to file...\n"
			
				node_folder_loc = output_dir+node_name+"/" #see if node_name folder exists and create it if not
				ensure_folder(node_folder_loc)
				node_file_loc= node_folder_loc + node_name + ".ino"
				#print "node file location will be: "+node_file_loc
				#print "os.path.isdir(d) is " + str(os.path.isdir(d))
				f = open((node_file_loc),'w')
				f.write(arduino_node_file) # python will convert \n to os.linesep
				f.close()
				#end arduino file construction--------------------------------------------
				#-------------------------------------------------------------------------
			
				#openhab part
				oh_sitemap_sensors+="\nFrame label=\""+node_name+"\" {\n"
				oh_sitemap_sensors+=oh_sitemap_these_sens
				oh_sitemap_sensors+="}\n"
			#end if num constructs > 0
		#end if sufficient node data
		else: print "not able to setup node due to lack of node data\n"
	#end if node is enabled
#end setup nodes function

def write_gateway_eth_arduino_file(): #creates arduino ethernet gateway file
	global codeHeaderArduino,gateway_ethernet_address,gateway_eth_mac,mqtt_server_ip,is_RFM69HW_code
	op=codeHeaderArduino
	op+="""
/*
Modifications Needed:
1)  Update mac address "mac[]" //xris does not know what mac this is...openhab server mac?
2)  Update MQTT broker IP address "server[]"

seems like code maybe based on:
http://www.mysensors.org/build/mqtt_gateway

*/

#include <SPI.h>
#include <Ethernet.h>
#include <Wire.h>
#include <PubSubClient.h>

//I2C receive device address
const byte MY_ADDRESS = %s;    //"I2C comms w/ other Arduino" //honestly don't know how this works...guessing eth gateyway address is equiv to node_id?

//Ethernet
byte mac[]    = {  %s }; //think can be random but need be unique on network
byte server[] = { %s }; //mosquitto broker server IP
//see https://blog.compose.io/a-temperature-sensing-and-networked-arduino/

EthernetClient ethClient;
PubSubClient client(server, 1883, callback, ethClient);

%s

	""" % (gateway_ethernet_address,gateway_eth_mac,mqtt_server_ip,debugCodeHeader)
	
	op+="""
unsigned long keepalivetime=0;
unsigned long MQTT_reconnect=0;


//use LED for indicating MQTT connection status.
int led = 13;
bool conn_ok;

//this fn required by above pubsub function call
void callback(char* topic, byte* payload, unsigned int length) {
  // handle message arrived
}


void setup() 
{
  //ethernet
  Wire.begin (MY_ADDRESS);
  Serial.begin (9600);

  Serial.println("starting");

  pinMode(led, OUTPUT);

  //wait for IP address
  Serial.println("getting IP address...");
  while (Ethernet.begin(mac) != 1)

  {
    Serial.println("Error getting IP address via DHCP, trying again...");
    delay(3000);
  }

  //Ethernet.begin(mac, ip);
  Serial.println("ethernet OK");
  keepalivetime=millis();
  Wire.onReceive (receiveEvent);

  while (client.connect("arduinoClient") != 1)
  {
    Serial.println("Error connecting to MQTT");
    delay(3000);
  }
  MQTT_reconnect = millis();
  Serial.println("setup complete");
  client.publish("localbroker","arduino ethernet gateway successfully connected to MQTT server");
}  // end of setup



volatile struct 
   {
  int                   nodeID;
  int			sensorID;		
  unsigned long         var1_usl;
  float                 var2_float;
  float			var3_float;		//
  int                   var4_int;
   } SensorNode;

int sendMQTT = 0;
volatile boolean haveData = false;

void loop() 
{
  //should keep track of time and ping MQTT server periodically via a topic that radio gateway and nodes are working properly


  //client.publish("mymosquitto","eth gateway MQTT con loop"); //for debugging

  if (haveData)
  {
    Serial.println("=========have data=========");
	Serial.print ("nodeID=");
	Serial.println (SensorNode.nodeID);
    Serial.print ("sensorID=");
    Serial.println (SensorNode.sensorID);  
    Serial.print ("var1 (time)=");
    Serial.println (SensorNode.var1_usl);
    Serial.print ("var2=");
    Serial.println (SensorNode.var2_float);
	Serial.println("---------");
    sendMQTT = 1;

    haveData = false;
  }  // end if haveData


  if (sendMQTT == 1)
  {

      Serial.println("starting MQTT send");

      conn_ok = client.connected();
      if (conn_ok==1)
      {
        digitalWrite(led, HIGH);
        Serial.println("MQTT connected OK from MQTT Send");
      }
      else
      {
        digitalWrite(led, LOW);
        Serial.println("MQTT NOT connected OK from MQTT Send");
      }

      //no connection, reconnect
      if (conn_ok == 0)
      {
        client.disconnect();
        delay(5000);
        while (client.connect("arduinoClient") != 1)
        {
          digitalWrite(led, LOW);
          Serial.println("Error connecting to MQTT");
          delay(4000);
          digitalWrite(led, HIGH);
        }
        digitalWrite(led, HIGH);
        Serial.println("reconnected to MQTT");
		
        MQTT_reconnect = millis();

      }


      int varnum;
      char buff_topic[6]; //e.g. 1282 - 12=node, 8=device, 2=variable
      char buff_message[12]; //e.g. state 0/1      

      //if reach here, know that have data to send, and know that connected to MQTT server ok
      client.publish("localbroker", "data loop publish achieved from eth gateway");

      //consider re-writing the following more, next couple dozen lines much up for deletion
      //send var2_float
      varnum = 2;
      buff_topic[6];
      buff_message[7];

      sprintf(buff_topic, "%02d%01d%01d", SensorNode.nodeID, SensorNode.sensorID, varnum);
      //int sprintf(char *str, const char *format, ...) sends formatted output to a string pointed to by str.//up for deletion
      //note sprintf usage: %02d = 2 digits (2), w leading zero padding if one digit (0), integer conversion (d)
      dtostrf (SensorNode.var2_float, 2, 1, buff_message);
      Serial.print("var2 buff topic: ");
      Serial.print(buff_topic);
      Serial.print(", message: ");
      Serial.println(buff_message);
      client.publish(buff_topic, buff_message);

      delay(200);

      //send var3_float
      varnum = 3;
      sprintf(buff_topic, "%02d%01d%01d", SensorNode.nodeID, SensorNode.sensorID, varnum);
      //Serial.println(buff_topic);
      dtostrf (SensorNode.var3_float, 2, 1, buff_message);
      Serial.print("var3 buff topic: ");
      Serial.print(buff_topic);
      Serial.print(", message: ");
      Serial.println(buff_message);
      client.publish(buff_topic, buff_message);

      delay(200);

      //send var4_int, RSSI
      varnum = 4;
      sprintf(buff_topic, "%02d%01d%01d", SensorNode.nodeID, SensorNode.sensorID, varnum);
      //Serial.println(buff_topic);
      sprintf(buff_message, "%04d%", SensorNode.var4_int);
      Serial.print("var4 buff topic: ");
      Serial.print(buff_topic);
      Serial.print(", message: ");
      Serial.println(buff_message);
      client.publish(buff_topic, buff_message);

      sendMQTT = 0;
      Serial.println("finished MQTT send");
      Serial.println("=========end have data=========");
    }//end if sendMQTT

  client.loop();
	"""
	op+="""
  if ((millis() - MQTT_reconnect) > 60000)
  {
    conn_ok = client.connected();
    if (conn_ok==1)
    {
      digitalWrite(led, HIGH);
      Serial.println("MQTT connected OK");
	  client.publish("localbroker","arduino ethernet gateway ping");
    }
    else
    {
      digitalWrite(led, LOW);
      Serial.println("MQTT NOT connected OK");
    }

    //no connection, reconnect
    if (conn_ok == 0)
    {
      client.disconnect();
      delay(5000);
      while (client.connect("arduinoClient") != 1)
      {
        digitalWrite(led, LOW);
        Serial.println("Error connecting to MQTT");
        delay(4000);
        digitalWrite(led, HIGH);
      }
      digitalWrite(led, HIGH);
    }

    Serial.println("reconnected to MQTT");
    MQTT_reconnect = millis();
  }

  %s
	delay(200); //this may not be necessary, up for deletion
}  // end of loop




// called by interrupt service routine when incoming data arrives
void receiveEvent (int howMany)
{
  if (howMany < sizeof SensorNode)
    return;

  // read into structure
  byte * p = (byte *) &SensorNode;
  for (byte i = 0; i < sizeof SensorNode; i++)
    *p++ = Wire.read ();

  haveData = true;     
}

	""" % (debugCodeLoop)
	#write the wireless gateway arduino file
	print "creating arduino wireless gateway ino file...\n"
	gw_folder=output_dir + "gateway_ethernet" + "/"
	ensure_folder(gw_folder)
	f = open((gw_folder + "gateway_ethernet" + ".ino"),'w')
	f.write(op) # python will convert \n to os.linesep
	f.close()
#end write_gateway_eth_arduino_file



def write_gateway_wi_arduino_file(): #creates arduino wireless/radio gateway file
	global codeHeaderArduino, gateway_radio_id,is_RFM69HW_code
	op=codeHeaderArduino
	
	op+="""
//RFM69  ----------------------------------
#include <RFM69.h>
#include <SPI.h>

#define NODE_ID  %s //unique to each arduino device on network

//unique for each network
#define NETWORK_ID  %s //same for all nodes that communicate w one another - is passed to radio methods
#define GATEWAY_ID  %s //need to import from config file
#define ENCRYPT_KEY  "%s" //same 16 chars for all nodes on network - needs higher security, need to import from config file
#define FREQUENCY     %s
%s

#define ACK_TIME      30 // max # of ms to wait for an ack
RFM69 radio;
bool promiscuousMode = false; //set to 'true' to sniff all packets on the same network
//I2C  -----------------------------------
#include <Wire.h>
const byte TARGET_ADDRESS = 42; //"I2C comms w/ other Arduino" //honestly don't know how this works...guessing eth gateyway address is equiv to node_id?
%s
	""" % (gateway_radio_id,network_id,gateway_id,encrypt_key,radio_frequency,is_RFM69HW_code,debugCodeHeader)
	op+="""
typedef struct {		
  int                   nodeID; 
  int			sensorID;
  unsigned long         var1_usl; 
  float                 var2_float; 
  float			var3_float;	
} Payload;
Payload theData;

typedef struct {		
  int                   nodeID; 
  int			sensorID;	
  unsigned long         var1_usl;
  float                 var2_float; 
  float			var3_float;
  int                   var4_int;
} itoc_Send;
itoc_Send theDataI2C;


void setup() 
{
  Wire.begin ();

  Serial.begin(9600); 

  //RFM69 ---------------------------
  radio.initialize(FREQUENCY,NODE_ID,NETWORK_ID);
  #ifdef IS_RFM69HW
    radio.setHighPower(); //uncomment only for RFM69HW!
  #endif
  radio.encrypt(ENCRYPT_KEY);
  radio.promiscuous(promiscuousMode);
  char buff[50];
  sprintf(buff, "\\nListening at %d Mhz...", FREQUENCY==RF69_433MHZ ? 433 : FREQUENCY==RF69_868MHZ ? 868 : 915);
  Serial.println(buff);

}  // end of setup

byte ackCount=0;
	"""
	op+="""
void loop() 
{

  if (radio.receiveDone())
  {
    //Serial.print('[');Serial.print(radio.SENDERID, DEC);Serial.print("] ");
    if (promiscuousMode)
    {
      Serial.print("to [");Serial.print(radio.TARGETID, DEC);Serial.print("] ");
    }


    if (radio.DATALEN != sizeof(Payload))
      Serial.println("Invalid payload received, not matching Payload struct!");
    else
    {
      theData = *(Payload*)radio.DATA; //assume radio.DATA actually contains our struct and not something else

	  Serial.print("nodeID=");
      Serial.print(theData.nodeID);
      Serial.print(", sensorID=");
      Serial.print(theData.sensorID);
      Serial.print(", var1=");
      Serial.print(theData.var1_usl);
      Serial.print(", var2=");
      Serial.print(theData.var2_float);
      Serial.print(", ");


      Serial.print(", RSSI= "); //received signal strength indicator (RSSI) is a measurement of the power present in a received radio signal
      Serial.println(radio.RSSI);

      //save it for i2c:
      theDataI2C.nodeID = theData.nodeID;
      theDataI2C.sensorID = theData.sensorID;
      theDataI2C.var1_usl = theData.var1_usl;
      theDataI2C.var2_float = theData.var2_float;
      theDataI2C.var3_float = theData.var3_float;
      theDataI2C.var4_int = radio.RSSI;      
    }


    if (radio.ACK_REQUESTED)
    {
      byte theNodeID = radio.SENDERID;
      radio.sendACK();
      //Serial.print(" - ACK sent.");
    }//end if radio.ACK_REQESTED

    //send wireless data to I2C
    Wire.beginTransmission (TARGET_ADDRESS);
    Wire.write ((byte *) &theDataI2C, sizeof theDataI2C);
    Wire.endTransmission ();
  } //end if radio.receive
  %s
}//end loop

	""" % (debugCodeLoop)
	#write the wireless gateway arduino file
	print "creating arduino wireless gateway ino file...\n"
	gw_folder=output_dir + "gateway_wireless" + "/"
	ensure_folder(gw_folder)
	f = open((gw_folder + "gateway_wireless" + ".ino"),'w')
	f.write(op) # python will convert \n to os.linesep
	f.close()
#end write_gateway_wi_arduino_file

def getjvar(json_var,req_vars,*json_passedData): #check if specific required variables (name json_var) defined in config file, makes req_vars 0 if not
	global json_data
	if not json_passedData:
		json_curData=json_data
	else:
		json_curData=json_passedData[0]
		#print "JSON data is:\n"+str(json_curData)+"\n"
	try:
		curVar=json_curData[json_var]
	except:
		print "could not find config variable " + str(json_var)
		req_vars[0]=0
		return 0
	else:
		print "found config variable " + str(json_var) + " with value "+str(json_curData[json_var])
		return json_curData[json_var]

#########################################
#		start main code body			#
#########################################

#process JSON configuration file
have_json_file=1 #will be set to 0 if cannot open configuration file
sufficient_net_data=[1] #will change if find don't have sufficient network data from config file
try:
	with open("config.json") as json_file:
		json_data = json.load(json_file)
	print "=============raw JSON configuration data============="
	print(json_data)
	print "====================================================="
except:
	print "could not open configuration file (config.json)\n"
	have_json_file=0
	sufficient_net_data[0]=0
else: print "successfully loaded JSON configuration file...\n"

if have_json_file:
	json_nodes = json_data["nodes"] #get the node data from configuration file

	#read config data that applies to all nodes

	if json_data["project_name"]: #see if override of project_name from config file
		openhab_project_name=json_data["project_name"]

	print "=============loading configuration data============="
	#following section should be rewritten using dict data type
	network_id=getjvar("network_id",sufficient_net_data)
	gateway_id=getjvar("gateway_id",sufficient_net_data)
	encrypt_key=getjvar("encrypt_key",sufficient_net_data)
	radio_frequency=getjvar("radio_frequency",sufficient_net_data)
	global_loop_delay=getjvar("global_loop_delay",sufficient_net_data)
	transmission_delay=getjvar("transmission_delay",sufficient_net_data)
	gateway_eth_mac=getjvar("gateway_eth_mac",sufficient_net_data)
	mqtt_server_ip=getjvar("mqtt_server_ip",sufficient_net_data)
	is_RFM69HW=getjvar("is_RFM69HW",sufficient_net_data)
	oh_server_url=getjvar("mqtt_server_url",sufficient_net_data)

	try:
		with open ("codeHeader.txt", "r") as myfile:
			codeHeader=myfile.read()
	except:
		print "could not find codeHeader file"
		sufficient_net_data[0]=0
	else:
		codeHeaderArduino="/*"+codeHeader+"*/"
		print "successfully loaded codeHeader file"
#end if have_json_file

if sufficient_net_data[0]:
	print "have sufficient network data to create network files..."
	
	#check for custom action variables
	#begin parsing for global xmpp data
	have_xmpp_data=[1]
	oh_xmpp=getjvar("xmpp",have_xmpp_data)
	if have_xmpp_data[0]:
		print "have xmpp data"
		have_xmpp_vars=[1]
		#need to parse out xmpp vars and load into local vars to pull from in rules section above
		xmpp_servername=getjvar("servername",have_xmpp_vars,oh_xmpp)
		xmpp_username=getjvar("username",have_xmpp_vars,oh_xmpp)
		xmpp_password=getjvar("password",have_xmpp_vars,oh_xmpp)
		xmpp_tlspin=getjvar("tlspin",have_xmpp_vars,oh_xmpp)
		if have_xmpp_vars[0]:
			print """
have xmpp vars:
-server = %s
-user = %s
-pass = %s
-tlspin = %s
			""" % (xmpp_servername,xmpp_username,xmpp_password,xmpp_tlspin)
		else:
			print "do not have xmpp vars"

		"""
		print "found xmpp configuration information...looking for all required variables..."
		if "servername" in oh_xmpp:
			if "servername" in oh_xmpp:
		else:
			print "error: found xmpp config info, but did not find 'severname' var within xmpp config!\n"
		print "have sufficient variables for xmpp configuration\n"
		"""
	else:
		print "no xmpp configuration data found in config file\n"
	#end global xmpp parsing

	if(is_RFM69HW): is_RFM69HW_code="#define IS_RFM69HW    //uncomment only for RFM69HW! Leave out if you have RFM69W!"
	else: is_RFM69HW_code="//#define IS_RFM69HW    //uncomment only for RFM69HW! Leave out if you have RFM69W!"
	
	print "====================================================="
	
	#ensure have output folder created
	ensure_folder(output_dir)
	
	#create arduino gateway files with calls to above functions
	write_gateway_eth_arduino_file()
	write_gateway_wi_arduino_file()

	#cycle through the nodes
	for cur_node in json_nodes:
		setup_node(json_nodes[cur_node],cur_node)
		num_nodes+=1
		print "=========================================================================="
	
	print "============finished arduino files, creating openhab files....============"
	print "=========================================================================="
	
	#create openhab files
	oh_configFile="""
mqtt:localbroker.url=%s
mqtt:localbroker.clientId=openHAB

mqtt:localbroker.qos=0
mqtt:localbroker.retain=true
mqtt:localbroker.async=true

mqtt-eventbus:broker=localbroker
mqtt-eventbus:statePublishTopic=openHAB/stateUpdates/${item}/state
mqtt-eventbus:commandPublishTopic=openHAB/commandUpdates/${item}/command

folder:items=2,items
folder:sitemaps=2,sitemap
folder:rules=2,rules
folder:scripts=2,script
folder:persistence=2,persist
	""" % (oh_server_url)
	
	#xmpp action configuration
	if have_xmpp_vars:
		oh_configFile_xmpp="""
xmpp:servername=%s
xmpp:username=%s
xmpp:password=%s
xmpp:tlspin=%s
		""" % (xmpp_servername,xmpp_username,xmpp_password,xmpp_tlspin)
		oh_configFile+=oh_configFile_xmpp

	#following for mail actions with openhab
	oh_configFile_mail="""
	######################## Mail Action configuration ####################################
	#
	# The SMTP server hostname, e.g. "smtp.gmail.com"
	mail:hostname=yesenia.dizinc.com 

	# the SMTP port to use (optional, defaults to 25 (resp. 587 for TLS))
	mail:port=465

	# the username and password if the SMTP server requires authentication
	mail:username=openhab
	mail:password=pkT2UyNkr5ZQdeF

	# The email address to use for sending mails
	mail:from=openhab@circuitblue.com

	# set to "true", if TLS should be used for the connection
	# (optional, defaults to false)
	mail:tls=true

	# set to "true", if POP before SMTP (another authentication mechanism)
	# should be enabled. Username and Password are taken from the above
	# configuration (optional, default to false)
	#mail:popbeforesmtp=
	"""
	
	
	oh_sitemap_groups+="\n}\n\n"
	oh_items_file=oh_items_groups+"\n"+oh_items_sensors
	oh_sitemap_file+=oh_sitemap_groups+oh_sitemap_sensors+"\n"+oh_sitemap_alarms+"}"
	print "items file is:\n"+oh_items_file+"\n"
	print "sitemap file is:\n"+oh_sitemap_file+"\n"
	print "rules file is:\n"+oh_rules_file+"\n"
	print "creating openhab files...\n"
	f = open((output_dir + "openhab.cfg"),'w')
	f.write(oh_configFile)
	f.close()
	f = open((output_dir + openhab_project_name + ".items"),'w')
	f.write(oh_items_file)
	f.close()
	f = open((output_dir + openhab_project_name + ".sitemap"),'w')
	f.write(oh_sitemap_file)
	f.close()
	f = open((output_dir + openhab_project_name + ".rules"),'w')
	f.write(oh_rules_file)
	f.close()
	print "done creating openhab files\n"
#end if sufficient_data
else: print "do NOT have sufficient data from config file to setup arduino sensor network"

print "...end of program"