-------------------
#### gym xplane environment
-------------------
# gym-xplane
Gym Xplane is an environment bundle for OpenAI Gym. 

## Installation

1. Install [OpenAI Gym](https://github.com/openai/gym) and its dependencies.
2. Install the package itself:
    ```
    git clone  PASTE HTTPS OR SSH HERE // if you have not cloned the repo before
    cd gym_xplane
    pip install -e .
    ```

## Usage
1. Start Xplane 
2. Start random agent example from the `examples` folder

2. Run examples:

    ```
    cd Examples 
    sudo  /path/to/anaconda/python3.6  random_agent.py 
    ```
    for example a typical conda python path is /home/cat/anaconda3/envs/cat/bin/python3.6 . 

   In the random_example script you have the following configuration. 
    ```
    sudo /home/cat/anaconda3/envs/cat7/bin/python3.7  random_agent.py
    ```
    
   It is possible to configure a new python xplane connector as desired - thus replacing the client. The general pattern would be as in the pyxpc.py file. As a minimum a socket connection should be defined  together with a function to get states and send actions.
   
### TO DO
   Update reward function. (You could define your reward function for your custom scenario too)
    
