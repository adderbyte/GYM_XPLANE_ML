import numpy as np

from gym import spaces


import gym_xplane.envs.xplane_envBase as xp



class xplane_Env_run(xp.XplaneEnv):
    def __init__(self,client,max_episode_steps=2000):
        super(xplane_Env_run, self).__init__(client,max_episode_steps)


        
        

    def _action_space(self):
        # attack or move, move_degree, move_distance
       
        return  spaces.Dict({"Latitudinal Stick":  spaces.Box(low=-1, high=1, shape=()),
            "Longitudinal Stick":  spaces.Box(low=-1, high=1, shape=()),
            "Rudder Pedals":  spaces.Box(low=-1, high=1, shape=()),"Throttle":  spaces.Box(low=-1, high=1, shape=()),
            "Gear":  spaces.Discrete(2),"Flaps":  spaces.Box(low=0, high=1, shape=()),
            "Speedbrakes": spaces.Box(low=-0.5, high=1.5, shape=())})

    def _observation_space(self):
        # hit points, cooldown, ground range, is enemy, degree, distance (myself)
        # hit points, cooldown, ground range, is enemy (enemy)
        #obs_low = [-1., -1., -1., -1., -1.0, 0., 0.0, -0.5]
        #obs_high = [1., 1., 1., 1.0, 1.0, 1., 1.0, 1.5]
        return spaces.Dict({"Latitude":  spaces.Box(low=0, high=360, shape=()),
            "Longitude":  spaces.Box(low=0, high=360, shape=()),
            "Altitude":  spaces.Box(low=0, high=8500, shape=()),"Pitch":  spaces.Box(low=-290, high=290, shape=()),
            "Heading":  spaces.Box(low=0, high=360, shape=()),
            "Gear":  spaces.Discrete(2),"yoke_roll_ratio":  spaces.Box(low=-2.5, high=2.5, shape=()),
            "yoke_heading_ratio":  spaces.Box(low=-2.5, high=2.5, shape=()),"pitch_ratio":  spaces.Box(low=-180, high=180, shape=()),
            "wing_sweep_ratio":  spaces.Box(low=-2.5, high=2.5, shape=()),"flap_ratio":  spaces.Box(low=-2.5, high=2.5, shape=()),
            "speed": spaces.Box(low=-2205, high=-2205, shape=())})
        
   
