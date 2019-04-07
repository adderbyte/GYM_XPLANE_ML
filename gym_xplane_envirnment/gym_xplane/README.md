# gym-xplane
Gym Xplane is an environment bundle for OpenAI Gym. 

## Installation

1. Install [OpenAI Gym](https://github.com/openai/gym) and its dependencies.

2. Uses [XPlaneConnect Connection Script](https://github.com/nasa/XPlaneConnect) and its dependencies. You can skip the torch client part. 

3. Install the package itself:
    ```
    git clone  PASTE HTTPS OR SSH HERE // if you have not cloned the repo before
    cd gym_xplane_envirnment/gym_xplane/xplane_gym
    pip install -e .
    ```

## Usage
1. Start Xplane and add [XPlaneConnect Connection Script](https://github.com/nasa/XPlaneConnect) plugin to the XPlane/Resource/plugins folder.
2. Add [FlyWithLua](https://github.com/nasa/XPlaneConnect) plugin to the XPlane/Resource/plugins folder.
3. Add envirommentRestart.lua script to the scripts folder of flightWithlua.



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
    
