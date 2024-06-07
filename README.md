Turn your EMF Tildagon badge into a RGB light, hooked into your Home Assistant server (or other MQTT solution!) 
This process is a little bit involved

1.) You need to install the umqtt.simple library onto your badge. I used Thonny; once you've got the badge connected, look under tools > Manage Packages

2.) If you want to drive this from Home Assistant, you can add the config from https://github.com/AlexJMcIntyre/Tildagon-MQTT-RGB-Light/blob/main/Home%20Assistant%20Config into HA's configuration.yaml. Reload Home Assistant and check this new Tildagon entity exists. 

3.) Becasue of these requirements, I've not added this app to the badge app store. Instead you can install it manually by:
	 -creating a /apps/MQTT_RGB/ directory on badge 
	 -copy app.py and metadata.json into the /apps/MQTT_RGB/ directory

4.) In app.py, for the line:

self.client = MQTTClient(f'Tildagon1', 'homeassistant.local', 1883, 'mqttuser', 'mqttpass')

Replace homeassistant.local with the address of your home assistant server, 1883 with your port (if you're not running the default), 'mqttuser' and 'mqttpass' with a valid username and password for your MQTT broker
 
5.) Save your changes, and reboop your badge. From within the badge settings, menu turn the LED pattern to 'Off' (else the badge will constantly overwrite your desired colour with the default led behaviour)

Done! You should now see the RGB MQTT Light app in the badge menu. Open it up, set a colour in HA, and turn up the brightness! You can now control your badge from within HA and set up whatever automations you want to. 
