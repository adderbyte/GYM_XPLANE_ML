




def getParameters():
	'''
	This function is used to define training parameters. 
	This is separated from the main loop pf the program for ease of reference. 
	There are many  state variables
	so that having them in a separate file is a good idea. 
	'''
	  

	  # Global dictionary for acrquiring the parameters for the training
	globalDictionary = {
	 # State Variables. This together with other parameters (to be defined later) will give us the 
	 # state of the aircraft. Note that this variables will be parsed to our function and the function
	 # returns a set of values. check xplane dataref file for definition of stateVariable

		"stateVariable" : ["sim/flightmodel/position/local_vx","sim/flightmodel/position/local_vy",
		"sim/flightmodel/position/local_vz"],
		 
		# "sim/cockpit2/autopilot/gpss_status"
		"rewardVariable": "sim/cockpit2/radios/indicators/gps_dme_distance_nm", #,"sim/cockpit2/radios/indicators/gps_dme_time_min",

		"headingReward":"sim/cockpit2/radios/indicators/gps_bearing_deg_mag",
		
		# State variables values are stored in list sateVariableValue
		"stateVariableValue": [],
		
		# this is the timing data parameters from x plane DataRef. "sim/time/total_running_time_sec",
		"timer": "sim/time/total_flight_time_sec",
		"timer2": "sim/time/total_running_time_sec",  # sim/time/timer_elapsed_time_sec  sim/time/timer_is_running_sec
		# this is for timing data storage. It will be recovered from simulation
		"timerValue" : [None] ,
		"timerValue2": [None],
		"on_ground":["sim/flightmodel2/gear/on_ground"],
		"crash":["sim/flightmodel/engine/ENGN_running"],
		"resetHold": [10.],
		"NumOfStatesAndPositions": 11, 
		# Aircraft Position state Variables
		"stateAircraftPosition" : [],
		"episodeReward": 0.,
		"totalReward":0.,
		"flag": False,
		"state":[0.,0.,0.,0.,0.,0.,0.],
		"state14":{"Latitude":0,"Longitude":0, "Altitude": 0,"Pitch":0,"Roll":0, "Heading": 0,  "gear":0,"yoke_pitch_ratio":0,"yoke_roll_ratio":0, "yoke_heading_ratio":0,"alpha":0},
		"episodeStep":0,
		"reset":False

		}

	globalDictionary = dotdict(globalDictionary) # make the dot notation for dictionary possible 


	return globalDictionary

class dotdict(dict):
   """dot.notation access to dictionary attributes"""
   __getattr__ = dict.get
   __setattr__ = dict.__setitem__
   __delattr__ = dict.__delitem__
