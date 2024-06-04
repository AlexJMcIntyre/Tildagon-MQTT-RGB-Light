1.) You need to install the umqtt.simple library onto your badge

2.) If you want to drive this from Home Assistant, you can add this code into configuration.yaml:


mqtt:
	light:
 		name: "Lix's Tildagon"
		state_topic: "attic/tildagon1"
		command_topic: "attic/tildagon1/switch"
		brightness_state_topic: "attic/tildagon1/brightness"
		brightness_command_topic: "attic/tildagon1/brightness/set"
		rgb_state_topic: "attic/tildagon1/color"
		rgb_command_topic: "attic/tildagon1/color/set"
		effect_state_topic: "attic/tildagon1/effect"
		effect_command_topic: "attic/tildagon1/effect/set"
 
