---------------------------------------------
##### XPlane_ML_Reinforcement_Learning_Autopilot
-------------------------------------------------
This project documents set up of Reinforcement learning environment for flight control. This will enable each user/learner/student/flight enthusiast to come with their own RL algorithm that can interact with and control in real time an aircraft in a simulation environment. The simulator used is ***X-Plane*** (the flight environment). This gives a realistic environment to work with together with parameters to keep the simulation as close to reality as possible.

`Update: Use the leaderboard wiki Page--> `([Leaderboard](https://github.com/adderbyte/GYM_XPLANE_ML/wiki/Leaderboard)) ` to add details of your own scenario or algorithm.`

------------------
### Agent-Environment Interaction Flow
-------------------
<!-- [![Simulation Interface](https://j.gifs.com/OMgJjG.gif)](https://j.gifs.com/OMgJjG.gif) -->
![alt-text](https://github.com/adderbyte/GYM_XPLANE_ML/blob/master/images/chart.png)


------------------
### Example Training Episode
-------------------
<!-- [![Simulation Interface](https://j.gifs.com/OMgJjG.gif)](https://j.gifs.com/OMgJjG.gif) -->
![alt-text](https://github.com/adderbyte/GYM_XPLANE_ML/blob/master/images/input.gif)


------------------
### Action Space Parameters
-------------------
` The action space parameters. Select from the list the appropriate parameters for any task or scenario .` For example one might decide that the first 4 parameters are important for a defined task.

| Action Space Parameter | Action type | Action Value Range |
| --- | --- |---|
| Latitudinal Stick | [Box](http://gym.openai.com/docs/#spaces) |  [-1,1] |
| Longitudinal Stick  | [Box](http://gym.openai.com/docs/#spaces) | [-1,1] |
| Rudder Pedals | [Box](http://gym.openai.com/docs/#spaces) | [-1,1]|
| Throttle | [Box](http://gym.openai.com/docs/#spaces) | [-1/4,1] |
| Gear | [Discrete](http://gym.openai.com/docs/#spaces) | 0,1 |
| Flaps | [Box](http://gym.openai.com/docs/#spaces) | [0,1] |
| Speedbrakes | [Box](http://gym.openai.com/docs/#spaces) | [-0.5,1.5] |

------------------
### State Space Parameters
-------------------
`The state space parameters are well documented in` [XPlane Data Ref](https://www.siminnovations.com/xplane/dataref/index.php) . The number of state space parameters will  depend on the task. It is possible to use a derived state paramter. Usually a UDP connection ([XPlaneConnect](https://github.com/nasa/XPlaneConnect)) is required to read this parameter from XPlane. 

| State Space Parameter | State type | State Value Range |
| --- | --- |---|
| velocity_x | [Box](http://gym.openai.com/docs/#spaces) |  [0,120] |
| velocity_y  | [Box](http://gym.openai.com/docs/#spaces) | [0,120] |
| delta_heading | [Box](http://gym.openai.com/docs/#spaces) | [-300,300]|

The range of each parameter value would also depend on the configuration. Example of how to read parameter from Xplane is shown below:

```
client = xpc.XPlaneConnect() # UDP connector
client.getDREF("sim/flightmodel/position/P")[0][0] # moment P
client.getPOSI() # get the lat, long,altitude, pitch, roll, heading, gear

```

`client` (UDP connector) already has a function `getPOSI` that helps read the `latitude, longitude, altitude, pitch, roll, heading`. Other parameters could be added by using the client `getDREF` function. Note that the string `"sim/flightmodel/position/P"` is gotten from the Xplane Dataref referenced earlier ([XPlane Data Ref](https://www.siminnovations.com/xplane/dataref/index.php))



-------------------
#### Requirements
--------------------
* X Plane (Demo version) (main requirement)
  * [XPLane](https://www.x-plane.com/)
* XPlaneConnect (replace this with  different python udp connection file if required)
  * [XPlaneConnect](https://github.com/nasa/XPlaneConnect) [https://github.com/nasa/XPlaneConnect]
* RL Algorithm (define  your own RL algorithm or use standard baslines. )
  *  [Tensorforce](https://github.com/reinforceio/tensorforce) 
  *  [RLLIB](https://ray.readthedocs.io/en/latest/rllib.html)
  *  [OpenAI Baselines](https://github.com/openai/baselines)
* Lua Programming/[FlyWithLua](https://www.x-plained.com/flywithlua-for-x-plane-11/) (for seamless interaction with XPlane)


------------------
#### General setup
-------------------
 * GYM XPLANE ENVIRONMENT
 * MULTI AGENT ENVIRONMENT SET UP (Work in progress)


------------------
##### TO DO  
-------------------
 * Use XVFB for fake display.
 * Docker support 
 * Algorithm implementations (high priority)





