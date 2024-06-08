## Tildagon MMQT RBG Light

Turn your EMF Tildagon badge into a RGB light, hooked into your Home Assistant server (or other MQTT solution!) 
This process is a little bit involved than installing an app from the app store, and it's a bit hacky, sorry!

### Getting Started

### Prerequisites

You will need a way to copy code onto your Tildagon badge such as [Thonny](https://thonny.org) or [mpremote](https://docs.micropython.org/en/latest/reference/mpremote.html)

### Installation

1. You need to install the `umqtt.simple` library onto your badge. I used [Thonny](https://thonny.org); once you've got the badge connected, look under `tools > Manage Packages`

2. If you want to drive this from Home Assistant, you can add the config from [Home Assistant Config](https://github.com/AlexJMcIntyre/Tildagon-MQTT-RGB-Light/blob/main/Home%20Assistant%20Config) into HA's configuration.yaml. Reload Home Assistant and check this new Tildagon entity exists. 

3. Becasue of these requirements, I've not added this app to the badge app store. Instead you can install it manually by:
	 
  - creating a `/apps/MQTT_RGB/` directory on badge 
  
  - coping `app.py` and `metadata.json` into the `/apps/MQTT_RGB/` directory

4. In `app.py`, for the line:\
`self.client = MQTTClient(f'Tildagon1', 'homeassistant.local', 1883, 'mqttuser', 'mqttpass')`\
Replace `homeassistant.local` with the address of your home assistant server, `1883` with your port (if you're not running the default), `mqttuser` and `mqttpass` with a valid username and password for your MQTT broker
 
5. Save your changes, and reboop your badge.

Done! You should now see the RGB MQTT Light app in the badge menu. Open it up, set a colour in HA, and turn up the brightness! You can now control your badge from within HA and set up whatever automations you want to. 
