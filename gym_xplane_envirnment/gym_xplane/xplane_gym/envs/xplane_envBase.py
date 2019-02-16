import gym

import gym_xplane.parameters as parameters
import gym_xplane.space_definition as envSpaces
import numpy as np

class XplaneEnv(gym.Env):
    
    def __init__(self,client,max_episode_steps):
        #self.client = xp.XPlaneConnect(clientAddr,xpHost,xpPort,clientPort,timeout ,max_episode_steps)
        self.client = client
        #print(parameters)
        
        
        envSpace = envSpaces.xplane_space()
        self.ControlParameters = parameters.getParameters()
        self.action_space = envSpace._action_space()
        self.observation_space = envSpace._observation_space()
        self.episode_steps = self.ControlParameters.episodeStep
        self.max_episode_steps = max_episode_steps
        #print(self.client)
        #self.step = self._step(action)
    #def __del__(self):
     #   self.client.close()

    def _close():
        self.client.close()
        
    def step(self, actions):
        #print('....',self.client)
        
        
        self.ControlParameters.flag = False
        self.ControlParameters.episodeReward = 0
        #ControlParameters.totalReward = 0
        self.episode_steps += 1
        tempreward = 0.
        tempreward2 =0.
        tempreward3 = 0.
        perturbationAllowed = 15.0
        minimumAltitude= 550 #meters
        minimumRuntime = 80.50
        minimumDistance = 0.5;
        
        #print('param', self.ControlParameters.stateAircraftPosition)
       
        try:
            #print('inside')
            act = [actions['Latitudinal Stick']]

            

            #print('acting...' , act )
            act.extend([actions['Longitudinal Stick'],actions['Rudder Pedals'],actions['Throttle'],int(actions['Gear']),actions['Flaps'],actions['Speedbrakes']])
            
            # sebd action
            self.client.sendCTRL(act)
            
            #***************** control parameters ***************************************************
            # get control parameters defined in parameters.py file  
            # The control parameters are already set in the parameter.py file.
            # Here we just call to use the model  

            state = [];
           
            

            #print('state: ',ControlParameters.stateAircraftPosition)
            #****************************************************************************************
            stateVariableTemp = self.client.getDREFs(self.ControlParameters.stateVariable) 
            self.ControlParameters.stateAircraftPosition = list(self.client.getPOSI());
            # Reove brackets from state variable and store in the dictionary
            self.ControlParameters.stateVariableValue = [i[0] for i in stateVariableTemp]
           
            # 14 prameters
            state =  self.ControlParameters.stateAircraftPosition + self.ControlParameters.stateVariableValue
            
            if len(state) == 14:
                self.ControlParameters.state14 = state
            else:
                self.ControlParameters.state14 = self.ControlParameters.state14
            #print(len(temp) == ControlParameters.NumOfStatesAndPositions  and all(v != 0. for v in ControlParameters.stateVariableValue))
            #print('monitor: ...', ControlParameters.NumOfStatesAndPositions)
            #print(not(all(v == 0. for v in ControlParameters.stateVariableValue))
            #*******************************************************************************************
            # flag for model 
            #ControlParameters.flag = flag
            #*******************************************************************************************
            #***********Reward definition*****************************************************************

            rewardVector = self.client.getDREF(self.ControlParameters.rewardVariable) 
            headingReward = self.client.getDREF(self.ControlParameters.headingReward)[0][0]
            #crash_indiocator = client.getDREF("sim/cockpit2/annunciators/engine_fires")[0][0]
                        

           
            if self.ControlParameters.stateAircraftPosition[5] > headingReward + perturbationAllowed :
                tempreward -= 1.
                #ControlParameters.stateAircraftPosition[5] = headingReward
                
            else :
                tempreward += 1.


            if self.ControlParameters.stateAircraftPosition[5] < minimumAltitude:
                tempreward2 -=1.
            else:
                tempreward2 += 1.

            if  rewardVector[0][0] > minimumDistance:
                tempreward3 -=0.5
            else:
                tempreward3 +=0.5

           
            self.ControlParameters.episodeReward = (tempreward +tempreward2 +tempreward3)/3.
            
            # tempreward,tempreward2,tempreward3,rewardSum=parameters.rewardReset(tempreward,tempreward2,tempreward3,rewardSum)
            # print('temporary reward Normalized', tempreward,tempreward2,tempreward3 )
            self.ControlParameters.totalReward += self.ControlParameters.episodeReward

            if self.client.getDREFs(self.ControlParameters.on_ground)[0][0] >= 1 or CLIENT.getDREFs( self.ControlParameters.crash)[0][0] <=0:
                #tempreward,tempreward2,tempreward3,rewardSum=parameters.rewardReset(tempreward,tempreward2,tempreward3,rewardSum)
                #print('reward reset', tempreward,tempreward2,tempreward3,rewardSum)
                #print('temporary reward Un-normalized', tempreward,tempreward2,tempreward3 )
                self.ControlParameters.flag = True
                #print('temporary reward Normalized', tempreward,tempreward2,tempreward3 )
                self.ControlParameters.totalReward  -= 2
                
                
            elif self.client.getDREF(ControlParameters.timer2)[0][0] > minimumRuntime :
                self.ControlParameters.flag = True
                self.ControlParameters.totalReward  += 2

        #***************** reformat and send  action ***************************************************
            
            if self.episode_steps >= self.max_episode_steps:
                    self.ControlParameters.flag = True
                    reward = self.ControlParameters.totalReward
            

            
            ### final episode or loop episode
            if self.ControlParameters.flag:
                reward = self.ControlParameters.totalReward
                #print('final reward', self.ControlParameters.totalReward )
                self.ControlParameters.flag = True
                self.ControlParameters.totalReward=0.
            else:
                reward = self.ControlParameters.episodeReward
                #print('total before',reward  )
            #agent.observe(state, actions);
            # print('flag; ',ControlParameters.flag,' episode reward: ',ControlParameters.episodeReward,
            #               ' Total reward',ControlParameters.totalReward, ' reward:',reward)
            #print('reward table',self.ControlParameters.episodeReward,self.ControlParameters.totalReward)

        except:
            reward = self.ControlParameters.episodeReward
            self.ControlParameters.flag = False
            self.ControlParameters.state14 = self.ControlParameters.state14


        return  self.ControlParameters.state14,reward,self.ControlParameters.flag,self._get_info()


  

    def _get_info(self):
        """Returns a dictionary contains debug info"""
        return {'control Parameters':self.ControlParameters, 'actions':self.action_space }

    def render(self, mode='human', close=False):
        pass


    def reset(self):
        """
        Reset environment and setup for new episode.
        Returns:
            initial state of reset environment.
        """
        self.ControlParameters.stateAircraftPosition = []
        self.ControlParameters.stateVariableValue = []
        self.ControlParameters.episodeReward  = 0.
        self.ControlParameters.totalReward  = 0.
        self.ControlParameters.flag = False
        self.episode_steps = 0
        self.ControlParameters.episodeStep = 0


        self.ControlParameters.state14  = np.zeros(shape=(14,))
        #return self.ControlParameters.state14
