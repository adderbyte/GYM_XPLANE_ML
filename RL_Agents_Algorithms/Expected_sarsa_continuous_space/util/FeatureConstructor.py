
class FeatureConstructor(object):
    
    def __init__(self,state agentName = "None"):
        self.agentName = agentName
        self.typeOfAgent = self.AgentType()
        

    def AgentType(self):
        '''
        This function enables to specify the kind of agent we want to use
        Add as many agent as you want here.

        '''
         
        if self.agentName == 'RadialBasis':
            #return self.agentPPO()
            pass
	
	elif self.agentName == 'Nystreum':
            #return self.agentPPO2()
            pass

        elif self.agentName == "TiledCoding":
            pass
        elif self.agentName == "TiledCoding":
            pass
        else:
            'Error: agent name in'
        

    def RadialBasis(self):

        '''
        This is where the agent  defined.
        output: returns the agent definition

        '''
      

        return agent #agent.act(np.array(ctrl1))

    def agentPPO2(self):

        '''
        This is where the agent  defined.
        output: returns the agent definition

        '''
        agent = PPOAgent(
            states=dict(type='float', shape=(7,)),
            actions=dict(
                            speedbrakes= dict(type='float', shape=(), min_value=-0.5, max_value=1.5),
                            flaps= dict(type='float', shape=(), min_value=0, max_value=1),
                            gear=dict(type='int',shape=(), num_actions=2),
                            Latitudinal= dict(type='float', shape=(), min_value=-1, max_value=1),
                            Longitudinal= dict(type='float', shape=(), min_value=-1, max_value=1),
                            Rudder= dict(type='float', shape=(), min_value=-1, max_value=1),
                            Throttle=dict(type='float', shape=(), min_value=-1, max_value=1),
                            
                            
                            
                            ),
            network=[
                dict(type='dense', size=64),
                dict(type='dense', size=64)
            ],
            batching_capacity=1,
            step_optimizer=dict(
                type='adam',
                learning_rate=1e-6
            ),

            summarizer=dict(directory='/home/cat/Desktop/start/tensorboard/',
                        labels=[
                            'total-loss',
                            'states',
                            'actions'
                            ]
                    ),
            update_mode = dict(batch_size = 5,
                                units = 'timesteps'
                        
                    )
        )

        #ctrl1 = np.random.uniform(low=0.1, high=1, size=(7,))

        return agent #agent.act(np.array(ctrl1))

    def agentDDQ(self):

        '''
        This is where the agent  defined.
        output: returns the agent definition


        '''
        # Network as list of layers
        network_spec = [
            dict(type='dense', size=64, activation='tanh'),
            dict(type='dense', size=64, activation='relu')
            ]

       
        
        agent = TRPOAgent(
          
            states=dict(type='float', shape=(7,)),
            actions=dict(
                            speedbrakes= dict(type='float', shape=(), min_value=-0.5, max_value=1.5),
                            flaps= dict(type='float', shape=(), min_value=0, max_value=1),
                            gear=dict(type='int',shape=(), num_actions=2),
                            Latitudinal= dict(type='float', shape=(), min_value=-1, max_value=1),
                            Longitudinal= dict(type='float', shape=(), min_value=-1, max_value=1),
                            Rudder= dict(type='float', shape=(), min_value=-1, max_value=1),
                            Throttle=dict(type='float', shape=(), min_value=-1, max_value=1),
                            
                            
                            
                            ),
            network= network_spec,
            summarizer=dict(directory='/home/cat/Desktop/start/trainboard',
                        labels=[
                            'gradients_scalar',
                            'graph',
                            'states',
                            'actions',
                            'gradients',
                            'variables',
                            'total-loss'
                            ]
                    ),
             learning_rate=1e-6

            
        )


                

        #ctrl1 = np.random.uniform(low=0.1, high=1, size=(7,))

        return agent #agent.act(np.array(ctrl1))

    def action(self,state):
        '''
        output: action . The shape of the action should be as specified in the 
                agent specification.
                Action typically consist of :
                  * Latitudinal Stick [-1,1]
                  * Longitudinal Stick [-1,1]
                  * Rudder Pedals [-1, 1]
                  * Throttle [-1, 1]
                  * Gear (0=up, 1=down)
                  * Flaps [0, 1]
                  * Speedbrakes [-0.5, 1.5]
        input: the state of the environments 

        '''
        return self.typeOfAgent.act(state)

    def observer(self,reward):
        '''
        output: action . The shape of the action should be as specified in the 
                agent specification.
                Action typically consist of :
                  * Latitudinal Stick [-1,1]
                  * Longitudinal Stick [-1,1]
                  * Rudder Pedals [-1, 1]
                  * Throttle [-1, 1]
                  * Gear (0=up, 1=down)
                  * Flaps [0, 1]
                  * Speedbrakes [-0.5, 1.5]
        input: the state of the environments 

        '''
        #if count > 20:
        print('reward submitted')
        self.typeOfAgent.observe(reward,True)
        
            #return 'observed Terminal'
        # else:
        #     self.typeOfAgent.observe(reward,False)
        #     return 'observed '
    

    def observer2(self,state,action,reward):
        '''
        output: action . The shape of the action should be as specified in the 
                agent specification.
                Action typically consist of :
                  * Latitudinal Stick [-1,1]
                  * Longitudinal Stick [-1,1]
                  * Rudder Pedals [-1, 1]
                  * Throttle [-1, 1]
                  * Gear (0=up, 1=down)
                  * Flaps [0, 1]
                  * Speedbrakes [-0.5, 1.5]
        input: the state of the environments 

        '''
        #if count > 20:
        #print('reward submitted')
        self.typeOfAgent.observe(state=state,action=action,reward=reward,terminal=True)


    def reset(self):
        """
        Resets the agent to its initial state (e.g. on experiment start). Updates the Model's internal episode and
        time step counter, internal states, and resets preprocessors.
        """
        #self.typeOfAgent.episode, self.typeOfAgent.timestep, self.typeOfAgent.next_internals = self.typeOfAgent.model.reset()
        #self.typeOfAgent.current_internals = self.typeOfAgent.next_internals
        self.typeOfAgent.reset()
        

