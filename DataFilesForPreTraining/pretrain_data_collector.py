'''
Simply Create Python3.7 in conda environment and activate it to use.
This script implements the main control logic to interact with an X Plane
for the control of an aircraft autonomously.
Simulation Environment		: X Plane
Communication Framework  	: X Plane Connect
Press 'Enter' to end script.
'''



import os
import sys
import xpc
import parameters
import sys, select, os
import json
# This dictionary contains required variables. It is placed here so ease of accessibility 









def main():

	'''
	This function runs the main algorithm for interacting and getting parameters from x plane.
	It is the control or brain of the simulation.
	
	Control Logic: Interaact with the x plane using XConnect.
			   (1) Get state of aircraft from x plane
			   (2) Give state to agents. Agent process the states and returns actions. 
			   (3) Actions (Control Parameters) are sent sent over UDP (XConnect) to control aircraft
			   (3) Compute the reward after Each episode or simulation run. The timer variable array
			   is used to track this. Restart simulation if time elapses or plane crashes
			   (4) Press enter to end the simulation all together
	Input : None
	Output: None
	'''

	
	#***************** control parameters ***************************************************
	# get control parameters defined in parameters.py file 	
	# The control parameters are already set in the parameter.py file.
	# Here we just call to use the model	
	ControlParameters = parameters.getParameters()
	#****************************************************************************************


	

	temp = []
	data = {}
	ctrl = None
	count = 0
	with xpc.XPlaneConnect() as client:
		while True:
			# This can help clear output while running the simulation
			os.system('cls' if os.name == 'nt' else '')	
			try:    
				#sleep(0.3)
				# ************ Get the state variables of the aircraft ************************
				# Aorcraft Position
				ControlParameters.stateAircraftPosition = list(client.getPOSI());
				#print ( "Position acf : ", ControlParameters.stateAircraftPosition) 
				# store state variables temporary here . The variables come with brackets from x plane 
				# we need to discard this for easy computation

				
				stateVariableTemp = client.getDREFs(ControlParameters.stateVariable) 
				#print('ailerons: ',client.getDREF('sim/cockpit2/controls/aileron_trim') )
				
				#print('heading: ',client.getDREF('sim/cockpit/misc/compass_indicated') )
				
				#print('gps status fire: ', client.getDREF("sim/cockpit2/annunciators/engine_fire") )
				#print('gps status: ', client.getDREF("sim/cockpit2/annunciators/engine_fires")[0][0] )
				# sim/operation/failures/rel_depres_slow	int	y	failure_enum	Slow cabin leak - descend or black out
				# sim/operation/failures/rel_depres_fast	int
				# Reove brackets from state variable and store in the dictionary
				ControlParameters.stateVariableValue = [i[0] for i in stateVariableTemp]
				#print ( "State Variables acf: ", ControlParameters.stateVariableValue) 

				

				#print('position + state variables ... ', len(temp))

				#**********************************************************************************

				#********** Parse state to the agents and get back the action****************
				# The action 
				
				#print("I am long action",temp)
				
				#-----print('Actions Computed by Agent...', actions)
				# send controls back to aircraft
				# compute time
				#ControlParameters.timerValue = [i[0] for i in client.getDREF(ControlParameters.timer)]
				#print('timer up', ControlParameters.timerValue )

				
				# check that all values have been collected. There should be total of 14
				# if len(ControlParameters.stateVariableValue) != 7:
				# 	print('HI... Something went wrong')
				# 	ControlParameters.stateVariableValue  = [0.,0.,0.,0.,0.,0.,0.]

				temp = ControlParameters.stateAircraftPosition + ControlParameters.stateVariableValue
				# Set control surfaces for level flight
				#values = [0.0F, 0.0F, 0.0F, 0.8F, 0.0F, 0.0F]
				#client.sendCTRL(values)
				client.sendWYPT(1,[0.00000,43.3066667,-122.437500])	
				print('waypoints')
				if len(temp) == ControlParameters.NumOfStatesAndPositions and count != 0:
									ctrl = client.getCTRL(0)
									#print('I am the control',ctrl)
									data[count] = (temp,ctrl)	


								

				
				#**********************************************************************
				#ctrl = client.getCTRL();
				#print('I am the control',ctrl)
				count = count+1
				print(count)
				
				#sleep(0.9)
				

			except : pass
				
				 
			# else: 

			# 	if all(v <= 0. for v in ControlParameters.stateVariableValue) and ControlParameters.flag == 0 :
					
			# 		print('Restarting Simulation ...')
					
			# 		subprocess.call(restart_Bash_File + "restart.sh")
			# 		sleep(1.5)
			# 		ControlParameters.flag  = 1
			# 		print('After restart = ' , ControlParameters.flag)
			

			#***************** Resetting the Flag after restart ************************************************************************
			# ControlParameters.flag = parameters.resetflag(ControlParameters.resetHold,ControlParameters.timerValue,ControlParameters.flag)
			# print('flag >>> ', ControlParameters.flag )
			#******************************************************************************************************************************
			
			#***************** stop agent on pressing enter ************************************************************************
			if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
					with open("waypointsData4.json", "w") as jsonFile:
									json.dump(data, jsonFile,sort_keys=True, indent=4)

									line = raw_input()
									break	
			#*****************************************************************************************************************************


if __name__ == "__main__":
	
	main()