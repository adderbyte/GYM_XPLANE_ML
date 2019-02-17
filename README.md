## XPlane_ML_Reinforcement_Learning_Autopilot
This project documents set up of Reinforcement learning environment for flight control. This will enable each user/learner/student/flight enthusiast to come with their own RL algorithm that can interact with and control in real time an aircraft in a simulation environment. The simulator used is ***X-Plane*** (the flight environment). This gives a realistic environment to work with together with parameters to keep the simulation as close to reality as possible.


## Requirement
* X Plane (Demo version) (main requirement)
  * [XPLane](https://www.x-plane.com/)
* XPlaneConnect (replace this with  different python udp connection file if required)
  * [XPlaneConnect](https://github.com/nasa/XPlaneConnect) [https://github.com/nasa/XPlaneConnect]
* Tensorforce (Use this to test your algorithm with typical RL Benchmarks)
  *  [Tensorforce](https://github.com/reinforceio/tensorforce) [https://github.com/reinforceio/tensorforce]
* RL Algorithm (define  your own RL algorithm or use standard baslines)
* Lua Programming (for seamless interaction with XPlane)

## General setup

* Standalone: single user, single environemnt.
* Multi-agent set up: In this set up, two or more agents can collaborate or compete in the training process. A central system  co-ordinates the activities of other systems. 
* Distributed training environment: This set up uses python flask and celery to achieve distributed training on a large network. 




