-------------------------
#### gym-xplane
---------------------
Gym Xplane is an environment bundle for OpenAI Gym. 

------------------------
#### Installation
---------------------------

1. Install [OpenAI Gym](https://github.com/openai/gym) and its dependencies.

2. Uses [XPlaneConnect Connection Script](https://github.com/nasa/XPlaneConnect) and its dependencies. You can skip the torch client part. 


3. Install the package itself:
    ```
    git clone  PASTE HTTPS OR SSH HERE // if you have not cloned the repo before
    cd gym_xplane_envirnment/gym_xplane/xplane_gym
    pip install -e .
    ```
-------------------------------
#### Heading Hold
-------------------------------
The scenario tested here is that of keeping heading and altitude. The agent should be able to learn to keep heading and altitude  throughout flight while other parameters are kept constant. This could be extended to scenarion where agents follows waypoints in the flight plan. See diagram below for intuition of what is to be done:

![alt-text](https://github.com/adderbyte/GYM_XPLANE_ML/blob/master/gym_xplane_envirnment/gym_xplane/alt_hold.png)

-------------------------
#### Usage
--------------------------
1. Start Xplane 
2. Run examples:

    ```
    cd Examples
    sudo  /path/to/anaconda/python3.6  random_agent.py 
    ```
    for example a typical conda python path is /home/cat/anaconda3/envs/cat/bin/python3.6 . 

   In the random_example script you have the following configuration. 
    ```
    client = p3xpc.XPlaneConnect()
    env.client = client
    ```
    
   It is possible to configure a new python xplane connector as desired - thus replacing the client. The general pattern would be as in the pyxpc.py file. As a minimum a socket connection should be defined  together with a function to get states and send actions.
   
### TO DO
   Update reward function. (You could define your reward function for your custom scenario too)
    
