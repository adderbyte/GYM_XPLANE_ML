___________________________________________________________________________________
###### Data  collection for Pre-training
___________________________________________________________________________________

The main files are:
    ```
    xpc.py``` and ```
    parameters.py
     ```
. These two python files are used in the the pretraining data collection scripts for different scenario (check `Sample_Scripts`). The `xpc.py` handles connection to Xplane while the `parameters.py` contains the parameters definitions. The folder `Sample_Scripts` contains sample scripts that have been used for data collection for different tasks. This could be edited for sample scenario. The `Pretraining_data` file contains the JSON file for collected traning data.  The names of the scripts or data file would typically relect the task to be completed eg (keepHeading.py implies keep heading scenario script while the data file would be named keepHeading.json).

___________________________________________________________________________________
###### Note Pretraining_data JSON File Convention
___________________________________________________________________________________
 For each data file : A string of integer values or numbers is used as a key. For each number the first value set corresponds to state and the second value set corresponds to the action . Typically, we assume an autopilot or human pilot is flying the aircraft and at each iteration time or loop the state and action values as seen by the simulator is collected.



- [ ] update this part of the project. Change to be compatible with python3 and the gym Xplane Environment
