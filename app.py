import app
import simple_tildagon as st

from events.input import Buttons, BUTTON_TYPES
from umqtt.simple import MQTTClient


command_topic= "attic/tildagon1/switch"
brightness_state_topic= "attic/tildagon1/brightness"
brightness_command_topic= "attic/tildagon1/brightness/set"
rgb_state_topic= "attic/tildagon1/color"
rgb_command_topic= "attic/tildagon1/color/set"
effect_state_topic= "attic/tildagon1/effect"
effect_command_topic= "attic/tildagon1/effect/set"


r = 0
g = 0
b = 0
brightness = 0
stopic = ""
smsg = ""

def sub(topic, msg):
    global r, g, b, brightness, stopic, smsg
    stopic = topic.decode("utf-8")
    smsg = msg.decode ("utf-8")
    
    if stopic == rgb_command_topic:
        tr,tg,tb = (smsg.split(","))
        r = int(tr)
        g = int(tg)
        b = int(tb)
    elif stopic == brightness_command_topic:
        brightness = int(smsg)
    

class Lix_MQTT(app.App):
    def __init__(self):
        self.button_states = Buttons(self)
        self.client = MQTTClient(f'LixTildagon', "homeassistant.local", 1883, "mqttuser", "mqttpass")
        self.client.set_callback(sub)
        self.client.connect()
        self.client.subscribe("attic/tildagon1/#")
    
    def update(self, delta):
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            # The button_states do not update while you are in the background.
            # Calling clear() ensures the next time you open the app, it stays open.
            # Without it the app would close again immediately.
            self.button_states.clear()
            self.minimise()
        self.client.check_msg()
    

    
    def draw(self, ctx):
        global r, g, b, brightness
        ctx.font_size = 10
        ctx.save()
        ctx.rgb(r*brightness/65025,g*brightness/65025,b*brightness/65025).rectangle(-120,-120,240,240).fill()
        ctx.rgb(0,0,0).move_to(-80,-10).text(stopic)
        ctx.rgb(0,0,0).move_to(-80,10).text(smsg)
        ctx.restore()
        for i in range (1,13):
            st.led.set(i, [int(r*brightness/255),int(g*brightness/255),int(b*brightness/255)])
        

__app_export__ = Lix_MQTT

