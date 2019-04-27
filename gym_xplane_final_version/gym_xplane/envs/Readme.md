______________________________

##### Base environment definition
_____________________________


###### Note :


  1. The simulation  regularly sends pause command to ensure no other force (perhaps due to stability or control augmentation in XPlane) is acting on the aircraft. Doing this preserves the Markov Decision Process  of the model and is critical for agent learning.
  2. Another way to do this is to adjust control sensitivity  in xplane. This is the more robust option. And would be incorporated in future update. This way there is no need for artificial pause commands.
  
______________________________

##### Control Sensitivity Settings 
_____________________________

Locate the settings icon on the the right upper end of the XPlane Window, clickling on this launches the control settings window. Select  `Joystick` as shown below: 

![alt-text](https://github.com/adderbyte/GYM_XPLANE_ML/blob/master/images/settings_main.png)

At the bottom of the page one will find the control settings button, click on it:

![alt-text](https://github.com/adderbyte/GYM_XPLANE_ML/blob/master/images/sensitivity.png )

The control settings window now appears as shown below, adjust the settings accordingly:

![alt-text](https://github.com/adderbyte/GYM_XPLANE_ML/blob/master/images/control_sense.png)
