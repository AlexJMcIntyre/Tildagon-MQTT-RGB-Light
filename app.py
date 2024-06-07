import app
import simple_tildagon as st

from system.eventbus import eventbus
from system.patterndisplay.events import *
from events.input import Buttons, BUTTON_TYPES
from umqtt.simple import MQTTClient


command_topic = "tildagon1/switch"
brightness_command_topic = "tildagon1/brightness/set"
rgb_command_topic = "tildagon1/color/set"

r = .5
g = .5
b = .5
brightness = .5
status = True

def sub(topic, msg):
    global r, g, b, brightness, status

    stopic = topic.decode("utf-8")
    smsg = msg.decode ("utf-8")
    
    if stopic == rgb_command_topic:
        tr,tg,tb = (smsg.split(","))
        r = float(tr)/255
        g = float(tg)/255
        b = float(tb)/255
    elif stopic == brightness_command_topic:
        brightness = float(smsg)/255
    elif stopic == command_topic:
        if smsg == "ON":
            status = True
        else:
            status = False 
      
class MQTT_RGB(app.App):
    def __init__(self):
        print("Loading")
        self.button_states = Buttons(self)
        #Update the following line with your own details. 
        self.client = MQTTClient('Tildagon1', 'homeassistant.local', 1883, 'mqttuser', 'mqttpass')
        self.client.set_callback(sub)
        self.client.connect()
        self.client.subscribe("tildagon1/#")
        

    def update(self, delta):
        eventbus.emit(PatternDisable())
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            # The button_states do not update while you are in the background.
            # Calling clear() ensures the next time you open the app, it stays open.
            # Without it the app would close again immediately.
            self.button_states.clear()
            self.minimise()
        self.client.check_msg()
    
    def draw(self, ctx):
        global r, g, b, brightness, status
        ctx.font_size = 10
        ctx.save()
        if status:
            # screen brightness is 0 - 1
            ctx.rgb(r * brightness,g * brightness,b * brightness).rectangle(-120,-120,240,240).fill()
             # led brightness is 0 - 255
            for i in range (1,13):
                st.led.set(i, [int(r * brightness * 255),int(g * brightness * 255),int(b * brightness * 255)])
        else:
            # screen brightness is 0 - 1
            ctx.rgb(0, 0 ,0).rectangle(-120,-120,240,240).fill()
             # led brightness is 0 - 255
            for i in range (1,13):
                st.led.set(i,[0,0,0])
        ctx.restore()

__app_export__ = MQTT_RGB

