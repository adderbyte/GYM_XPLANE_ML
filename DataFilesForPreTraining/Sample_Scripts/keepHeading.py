'''
Simply Create Python3.7 in conda environment and activate it to use.
This script helps get paramters for pretraining 
an  an agent 
Simulation Environment      : X Plane
Communication Framework     : X Plane Connect
Press 'Enter' to end script.
'''


##########################################################################################
#***************** important imports ***************************************************

import os
import sys
import p3xpc as xpc # xplane connect script for establishing udp connection
import parameters # utils for getting the dictionary containing parameters
import sys, select, os
import json  #  for saving training episodes as json file
import string # for naming file
import random # generate random name for files
from time import sleep

##########################################################################################







def main():

    '''
    This function runs the main algorithm for interacting and getting parameters from x plane.
    
    Control Logic: Interaact with the x plane using XConnect.
               (1) Get state and action of aircraft from x plane given that external expert/human control the xplane
               (2) store state to json
               (3) press enter to stop
              
    Input : None
    Output: None
    '''

    ##########################################################################################
    #***************** control parameters ***************************************************
    # get control parameters defined in parameters.py file  
    # The control parameters are already set in the parameter.py file.
    ControlParameters = parameters.getParameters()
    #****************************************************************************************
    ##########################################################################################

    ##########################################################################################
    temp = []   ## temp store for parameters
    data = {}  ## for storing each episode data
    action = None  ## no action on start
    count = 0 ## count for identifying each iteration
    minimumAltitude= 12000 # Targêt Altitude
    headingReward = 167 # target  heading
    ##########################################################################################
    with xpc.XPlaneConnect() as client:
        while True:
            # This can help clear output while running the simulation
            os.system('cls' if os.name == 'nt' else '') 
            try:    

                ##########################################################################################
                ## get the control
                tmep_action = client.getCTRL() # get the control on the simulation
                #client.pauseSim(True) # pause the simulation so that the state does not change
                ##########################################################################################
                action = [i for i in tmep_action][:4] # selection the 4 actiona parameters needed. (long stick, lat stick, rudder pedals, throttle)
                ##########################################################################################
                ## get the sate of the simulation
                ControlParameters.stateAircraftPosition = list(client.getPOSI()); # get the lat, long,altitude, pitch, roll, heading, gear
                stateVariableTemp = client.getDREFs(ControlParameters.stateVariable)  # get other parameters defined in parameter.py
                ControlParameters.stateVariableValue = [i[0] for i in stateVariableTemp] # make into a list
                state =  ControlParameters.stateAircraftPosition + ControlParameters.stateVariableValue # concatenate parameters
                ##########################################################################################
               

                ##########################################################################################
                P = client.getDREF("sim/flightmodel/position/P")[0][0] # moment P --- other parameter to use in training
                Q = client.getDREF("sim/flightmodel/position/Q")[0][0] # moment Q ---- other parameter to use for taining
                R = client.getDREF("sim/flightmodel/position/R")[0][0]  # moment R ---- other parameter to use in training
                
                ### Below is the parameter set to use in training .... 
                ### dictionary has been useed so the name could be clear
                ControlParameters.state14['roll_rate'] = P #  The roll rotation rates (relative to the flight)
                ControlParameters.state14['pitch_rate']= Q    # The pitch rotation rates (relative to the flight)
                ControlParameters.state14['altitude']= state[2] #  Altitude 
                ControlParameters.state14['Pitch']= state[3] # pitch 
                ControlParameters.state14['Roll']= state[4]  # roll
                ControlParameters.state14['velocity_x']= state[6] # local velocity x  OpenGL coordinates
                ControlParameters.state14['velocity_y']= state[7] # local velocity y  OpenGL coordinates              
                ControlParameters.state14['velocity_z']= state[8] # local velocity z   OpenGL coordinates
                ControlParameters.state14['delta_altitude']= abs(state[2] - minimumAltitude)#state[8]
                ControlParameters.state14['delta_heading']= abs(state[5] - headingReward) #state[9]
                ControlParameters.state14['yaw_rate']= R   #  The yaw rotation rates (relative to the flight)
                ##########################################################################################
                
                ##########################################################################################
                ### finally the parameter are retrieved from dictionary
                temp =  [i for i in ControlParameters.state14.values()]
                ##########################################################################################
                print(temp, len(temp))
                
                ##########################################################################################
                ## check that values are all present (11 parameters in total) and save in dictionary
                if len(temp) == ControlParameters.NumOfStatesAndPositions and count != 0:
                                    data[count] = (temp,action) 
                count = count+1
                ##########################################################################################

            except : pass

            ##########################################################################################

            #***************** stop agent on pressing enter ******************************************
            
            
            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                    string_len  = 5 # append string of length 5 to each name to genrate unique file name
                    filename = "trainingdata_"+  ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(string_len)) # generate unique file nam
                    with open( filename+(".json"), "w") as jsonFile:
                                    json.dump(data, jsonFile,sort_keys=True, indent=4)

                                    line = input()
                                    break   
            #*****************************************************************************************

            ##########################################################################################


if __name__ == "__main__":
    
    main() # run main