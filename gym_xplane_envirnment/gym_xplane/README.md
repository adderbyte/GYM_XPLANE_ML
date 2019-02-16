# gym-xplane
Gym Xplane is an environment bundle for OpenAI Gym. 

## Installation

1. Install [OpenAI Gym](https://github.com/openai/gym) and its dependencies.

2. Uses [XPlaneConnect Connection Script](https://github.com/nasa/XPlaneConnect) and its dependencies. You can skip the torch client part. 

3. Install the package itself:
    ```
    git clone  PASTE HTTPS OR SSH HERE // if you have not cloned the repo before
    cd xplane_gym
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


    ```
    cd examples
    sudo  /path/to/anaconda/python3.6  random_agent.py  --client    $client  
    ```


    The `$client` and `$step` are the client connector  to xplane and maximum episode step respectively. This is useful
    if a new connection script  is defined or desired to be used. However, the p3xpc.py is the present
    connection script used.
    
    The `$client_ip` and `$client_port` are the ip and port of the client connecting to xplane.   
