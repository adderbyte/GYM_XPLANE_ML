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
` Find below,  all the action space parameters avaibliable but the paramters utilized in a specific flight task depends on the scenario.` For example in the keepHeading or Heading Hold scenario only the first 4 parameters  were utilized from the list.

| Action Space Parameter | Action type | Action Value Range |
| --- | --- |---|
| Latitudinal Stick | [Box](http://gym.openai.com/docs/#spaces) |  [-1,1] |
| Longitudinal Stick  | [Box](http://gym.openai.com/docs/#spaces) | [-1,1] |
| Rudder Pedals | [Box](http://gym.openai.com/docs/#spaces) | [-1,1]|
| Throttle | [Box](http://gym.openai.com/docs/#spaces) | [-1/4,1] |
| Gear | [Discrete](http://gym.openai.com/docs/#spaces) | 0,1 |
| Flaps | [Box](http://gym.openai.com/docs/#spaces) | [0,1] |
| Speedbrakes | [Box](http://gym.openai.com/docs/#spaces) | [-0.5,1.5] |


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





