import numpy as np

from gym import spaces
import gym




class xplane_space():
 
    def _action_space(self):
        
        '''
        return  spaces.Dict({"Latitudinal_Stick":  spaces.Box(low=-1, high=1, shape=()),
            "Longitudinal_Stick":  spaces.Box(low=-1, high=1, shape=()),
            "Rudder_Pedals":  spaces.Box(low=-1, high=1, shape=()),"Throttle":  spaces.Box(low=-1, high=1, shape=()),
            "Gear":  spaces.Discrete(2),"Flaps":  spaces.Box(low=0, high=1, shape=()),
            "Speedbrakes": spaces.Box(low=-0.5, high=1.5, shape=())})
        '''
        return spaces.Box(np.array([ -1, -1, -1,-1/4]),np.array([1,1,1,1]))

    def _observation_space(self):
        
        '''
        return spaces.Dict({"Latitude":  spaces.Box(low=0, high=360, shape=()),
            "Longitude":  spaces.Box(low=0, high=360, shape=()),
            "Altitude":  spaces.Box(low=0, high=8500, shape=()),"Pitch":  spaces.Box(low=-290, high=290, shape=()),"Roll":  spaces.Box(low=-100, high=100, shape=()),"Heading":  spaces.Box(low=0, high=360, shape=()),"gear":  spaces.Discrete(2),"yoke_pitch_ratio":  spaces.Box(low=-2.5, high=2.5, shape=()),"yoke_roll_ratio":  spaces.Box(low=-300, high=300, shape=()),"yoke_heading_ratio":  spaces.Box(low=-180, high=180,shape=()),"alpha":  spaces.Box(low=-100, high=100,shape=()),
            "wing_sweep_ratio":  spaces.Box(low=-100, high=100, shape=()),"flap_ratio":  spaces.Box(low=-100, high=100, shape=()),
            "speed": spaces.Box(low=-2205, high=2205, shape=())})
        '''
        return spaces.Box(np.array([ -360, -360, 0 ,-290,-100,-360,-360,-1000,-1300,-1000,-1000]),np.array([360,360,8500,290,100,360,360,1000,1300,1000,1000]))
      
