---------------------------------------------
##### XPlane_ML_Reinforcement_Learning_Autopilot
-------------------------------------------------
This project documents set up of Reinforcement learning environment for flight control. This will enable each user/learner/student/flight enthusiast to come with their own RL algorithm that can interact with and control in real time an aircraft in a simulation environment. The simulator used is ***X-Plane*** (the flight environment). This gives a realistic environment to work with together with parameters to help keep the simulation as close to reality as possible.

`Update: Use the leaderboard wiki Page--> `([Leaderboard](https://github.com/adderbyte/GYM_XPLANE_ML/wiki/Leaderboard)) ` to add details of your own scenario or ( reinforcement learning ) algorithm.`

---------------------------------------------
##### GYM XPLANE ENVIRONMENT
-------------------------------------------------

`To install  the gym x-palne environment go through the read me file of the folder below ` 
[Gym-Xplane-final version](https://github.com/adderbyte/GYM_XPLANE_ML/tree/master/gym_xplane_final_version)
This is the latest version of the actual gym environment. 

The other folders contain  contain additional modules that might be needed for efficient training. 

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
The possible action parameters are given below. The choice of parameters would depend on the task. For example one might decide that the last three parameters are not important for the keep heading task ([Gym Xplane Wiki](https://github.com/adderbyte/GYM_XPLANE_ML/wiki/Leaderboard)) .

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
`The state space parameters are well documented in` [XPlane Data Ref](https://www.siminnovations.com/xplane/dataref/index.php). The number and configuration  of state space parameters would also  depend on the task. It is possible to use a derived state spade parameters. 

Note that, usually a UDP connection ([XPlaneConnect](https://github.com/nasa/XPlaneConnect)) is required to read any parameter parameter from XPlane. An example of how to read parameter from UDP connection is shown below:

```
client = xpc.XPlaneConnect() # UDP connector
client.getDREF("sim/flightmodel/position/P")[0][0] # moment P
client.getPOSI() # get the lat, long,altitude, pitch, roll, heading, gear

```

A typical state space  parameter configuration is shown below: 

| State Space Parameter | State type | State Value Range |
| --- | --- |---|
| velocity_x | [Box](http://gym.openai.com/docs/#spaces) |  [0,120] |
| velocity_y  | [Box](http://gym.openai.com/docs/#spaces) | [0,120] |
| delta_heading | [Box](http://gym.openai.com/docs/#spaces) | [-300,300]|

The range of each parameter value would also depend on the configuration or simulation task.

`client` (UDP connector) already has a function `getPOSI` that helps read the `latitude, longitude, altitude, pitch, roll, heading`. Other parameters could be added by using the client `getDREF` function. Note that the string `"sim/flightmodel/position/P"` is gotten from the Xplane Dataref referenced earlier ([XPlane Data Ref](https://www.siminnovations.com/xplane/dataref/index.php))

------------------
### Flight Dashboard
-------------------
To learn more about this go to :  [FlightDataVizDashBoard](https://github.com/adderbyte/GYM_XPLANE_ML/tree/master/FlightDataVizDashBoard)
![alt-text](https://github.com/adderbyte/GYM_XPLANE_ML/blob/master/images/gymXplaneDashboard.png)



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
 - [x] Use XVFB for fake display.
 - [x] Docker support (under test)
 - [ ] Algorithm implementations (high priority)
 - [ ] Real Time flight and data visualization interface.
 - [ ] Investigate Federated Learning





