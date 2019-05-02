----------------------------
### Final gym-xplane version
-----------------------------
Includes examples for most RL libraries and a tested and working sarsa continuous state algorithm. Also, the connection script is included in the gym xplane as `xpc.py` so that the connection starts automatically within the gym environment. If one desires to write or establish the connection outside the gym environment then the first version of the gym_xplane would be fine.

-------------------------------
### Heading Hold
-------------------------------
The scenario tested here is that of keeping heading named Heading Hold. The agent should be able to learn to keep heading for throughout flight while other parameters are kept constant. See diagram below for intuition of what is to be done:

![alt-text](https://github.com/adderbyte/GYM_XPLANE_ML/blob/master/gym_xplane_final_version/axes.png)

----------------------------------
#####  Heading Hold Configuration
----------------------------

| Aircraft Parameter | Parameter Value |
| --- | --- |
| Speed | 90 Knots True |
| Pitch | 3 |
| Altitude | 1200FT MSL|
| Heading | 164 deg |

| Action Parameter | Action type | Action Value Range |
| --- | --- |---|
| Latitudinal Stick | [Box](http://gym.openai.com/docs/#spaces) |  [-1,1] |
| Longitudinal Stick  | [Box](http://gym.openai.com/docs/#spaces) | [-1,1] |
| Rudder Pedals | [Box](http://gym.openai.com/docs/#spaces) | [-1,1]|
| Throttle | [Box](http://gym.openai.com/docs/#spaces) | [-1/4,1] |


-------------------------------------------
### XPlane Settings for xplane_gym
----------------------------------------
Xplane Settings set up is explained here.

#### Required Download
  - Download and Install XPlane

  - Download XPlaneConnect Connection from the link or use the one already included in this repo.

  - Download FlyWithLua from the link or use the one already included in this repo
  
#### Clone this repo
    `git clone PASTE HTTPS OR SSH HERE`

    
#### Installation
  - Install Xplane
  - add XPlaneConnect Connection plugin to the `XPlane/Resource/plugins` folder.
  - Add FlyWithLua plugin to the `XPlane/Resource/plugins` folder.
  - Add `reloadingScript.lua` script, found above, to the scripts folder of flyWithlua. (Not in the Scripts(disabled) folder). If you use the flywithlua that came with this repo then ignore this step. But check to be sure you have a file in the script folder.
  - A situation file has been provided for direct use (`KeepHeading.sit`) . Add this file into XPlane in the `XPlane/Output/situations` folder.
  - A flight plan that corresponds to this situation has also been added (`flightPlan.fms`). ( Load this into xplane in the : `X-Plane/Output/FMS plans` folder )
