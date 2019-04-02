import gym
from scipy.spatial.distance import pdist, squareform

import gym_xplane.xpc as xp
import gym_xplane.parameters as parameters
import gym_xplane.space_definition as envSpaces
import numpy as np
import itertools
from time import sleep, clock

class initial:

	def connect( clientAddr, xpHost, xpPort  , clientPort, timeout ,max_episode_steps):
			return xp.XPlaneConnect(clientAddr,xpHost,xpPort,clientPort,timeout ,max_episode_steps)

class XplaneEnv(gym.Env):

	#@staticmethod
	
	

	

	def __init__(self,clientAddr, xpHost, xpPort  , clientPort, timeout=3000 ,max_episode_steps=303,test=False):
		#CLIENT = client
		XplaneEnv.CLIENT = None
		#print(parameters)
		envSpace = envSpaces.xplane_space()
		
		
		self.ControlParameters = parameters.getParameters()
		self.action_space = envSpace._action_space()
		self.observation_space = envSpace._observation_space()
		#self.episode_steps = 0
		self.ControlParameters.episodeStep =0
		self.max_episode_steps = max_episode_steps
		self.statelength = 10
		self.actions = [0,0,0,0]
		self.test=test
		try:
			XplaneEnv.CLIENT = initial.connect(clientAddr,xpHost,xpPort,clientPort,timeout ,max_episode_steps)
		except:
			print("connection error. Check your paramters")
		print('I am client', XplaneEnv.CLIENT )
		#self.clientAddr = clientAddr
		#self.xpHost = xpHost
		#self.xpPort= xpPort
		#self.clientPort = clientPort
		#self.timeout = timeout
		#self.max_episode_steps=max_episode_steps
		#self.count = 0
		#CLIENT = initial.connect(clientAddr,xpHost,xpPort,clientPort,timeout ,max_episode_steps)
		#CLIENT = xp.XPlaneConnect(self.clientAddr,self.xpHost,self.xpPort,self.clientPort,self.timeout ,self.max_episode_steps)
		 
	

	def close(self):
		XplaneEnv.CLIENT.close()
	
	def rewardCalcul(self,target_state,xplane_state,sigma=0.45):
		'''
		input : target state (a list containing the target heading, altitude and runtime)
				xplane_state(a list containing the aircraft heading , altitude at present timestep, and the running time)
				Note: if the aircraft crashes then the run time is small, thus the running time captures crashes
		output: Gaussian kernel similarîty between the two inputs. A value between 0 and 1



		'''
		

		data = np.array([target_state,xplane_state])
	   
		pairwise_dists = pdist(data,'cosine')
		#print('pairwise distance',pairwise_dists)
		similarity = np.exp(-pairwise_dists ** 2 / sigma ** 2)

		return pairwise_dists


	def step(self, actions):
	 

		self.test=False
		self.ControlParameters.flag = False
		#self.ControlParameters.episodeReward = 0
		#ControlParameters.totalReward = 0
		#self.episode_steps += 1
		reward = 0.
		tempreward2 =0.
		tempreward3 = 0.
		perturbationAllowed = 3.5
		actions_ = []
		minimumPitch = 3.0
		
		j=0  # getting simulaion timing measurement
		
		try:
			
			#############################################
			# chck pevious acion is sam as he ain on control
			print("prevous action",self.actions) # prvious ation
			print("action on ctrl ...",XplaneEnv.CLIENT.getCTRL()) # action on control surface
			# if this is not sae then there are unaccounted forcs that could affct ainin
			# cnage the sleep time ater actio is sent in odr to ensure that training is synchronise
			# an the actins prined hee are same
			#############################################
			
			#############################################
			i=clock() # get he im up til now
			XplaneEnv.CLIENT.pauseSim(False) # unpause x plane simulation
			XplaneEnv.CLIENT.sendCTRL(actions) # sen acion
			sleep(0.0003)  # sleep for a while so hat ation is excued
			self.actions = actions	# set the previous action to curent action. 
									# This will be compared to action on control in nxt iteraion
			XplaneEnv.CLIENT.pauseSim(True) # pau imulation s tha no oher action acts on he aicaft
			j=clock() # get the time now, i-j is the time a which he simulaion is unpaused and actio exeuted
			# fom this point the simulation is paued so that we compute rewad and state-action value
			################################################# 
			
			#################################################
			# tenporary variable for holding stae values
			state = [];
			state14 = []
			################################################
			
			#################################################
			# get he state variabls here . The paameter file has all the required variables
			# we only need to call te cient intrface and get parameters defined as stateVariable
			# in parameter file
			stateVariableTemp = XplaneEnv.CLIENT.getDREFs(self.ControlParameters.stateVariable) 
			# the client interface automaically gets the position paameters
			self.ControlParameters.stateAircraftPosition = list(XplaneEnv.CLIENT.getPOSI());
			# Remove brackets from state variable and store in the dictionary
			self.ControlParameters.stateVariableValue = [i[0] for i in stateVariableTemp]
			# combine th position and other state parameters in temporar variable here
			state =  self.ControlParameters.stateAircraftPosition + self.ControlParameters.stateVariableValue
			########################################################

			########################################################
			# other paameters requie for training
			# there are numeous parameter and we could xpimnt hee
			# rewardVector : distance to the target . This is st along he hading and alitude.
			# this is set to motivate he agent to mov forad in time . Accumulate disance
			rewardVector = XplaneEnv.CLIENT.getDREF(self.ControlParameters.rewardVariable)[0][0] 
			headingReward = 164 # tagt heading
			minimumAltitude= 12000 # Targrt Altitude
			minimumRuntime = 210.50 # Target runtime
			P = XplaneEnv.CLIENT.getDREF("sim/flightmodel/position/P")[0][0] # moment P
			Q = XplaneEnv.CLIENT.getDREF("sim/flightmodel/position/Q")[0][0] # moment Q
			R = XplaneEnv.CLIENT.getDREF("sim/flightmodel/position/R")[0][0]  # moment R
			hstab = XplaneEnv.CLIENT.getDREF("sim/flightmodel/controls/hstab1_elv2def")[0][0]
			vstab = XplaneEnv.CLIENT.getDREF("sim/flightmodel/controls/vstab2_rud1def")[0][0]
			################################################################################3

			##############################################################################
			# make sure the state variabl is of appopriate length
			# it is amso possible to overwit some state vaiable
			# the ditionary name a not inicativ of the variable name  times. his is used for aining

			if len(state) == self.statelength:
				
				self.ControlParameters.state14['Latitude'] = hstab #abs(state[5] - headingReward)
				self.ControlParameters.state14['Longitude']= vstab    #abs(state[2] - minimumAltitude)
				self.ControlParameters.state14['Altitude']= P # state[2] 
				self.ControlParameters.state14['Pitch']= state[3]
				self.ControlParameters.state14['Roll']= state[4]
				self.ControlParameters.state14['Heading']= Q
				self.ControlParameters.state14['gear']= int(state[6])                
				self.ControlParameters.state14['yoke_pitch_ratio']= state[7]
				self.ControlParameters.state14['yoke_roll_ratio']= abs(state[2] - minimumAltitude)#state[8]
				self.ControlParameters.state14['yoke_heading_ratio']= abs(state[5] - headingReward) #state[9]
				self.ControlParameters.state14['alpha']= R
				#self.ControlParameters.state14['wing_sweep_ratio']= state[11] 
				#self.ControlParameters.state14['flap_ratio']= state[12]
				#self.ControlParameters.state14['speed']=state[13]
				#state14 = [i for i in self.ControlParameters.state14.values()]
			   
				self.ControlParameters.state14 = self.ControlParameters.state14 #self.ControlParameters.state14
				if self.test :
					# if testing use append longiud and laituede ans dn change the stat variable
					state.append(R)
					state14 = state # state variabl this inclue lat long for ploting

				else:
					# lat long have ben ovride so we use
					state14 = [i for i in self.ControlParameters.state14.values()]
			######################################################################
			
			###########################################################################
			# parameters required for reward
			# time is not used here
			timer =  XplaneEnv.CLIENT.getDREF(self.ControlParameters.timer2)[0][0] # running time of simulation
			target_state = [abs(headingReward),minimumAltitude,0.25]  # taget situation -heading, alitude, and istance 
			xplane_state = [ abs(state[5]),state[2],rewardVector]  # present situation -heading, alitude, and istance 
			# if the heading and altitude are within small pertubation set good reward othewise penalize it.
			if  (abs( abs(state[5])-headingReward)) < perturbationAllowed and (state[2]-minimumAltitude) < perturbationAllowed:
				reward = self.rewardCalcul(target_state,xplane_state,sigma=0.85)[0]
				self.ControlParameters.episodeReward = reward
			else:
				reward = self.rewardCalcul(target_state,xplane_state)
				self.ControlParameters.episodeReward = -reward[0]
			self.ControlParameters.episodeStep += 1
			#############################################################################

			###########################################################################
			# end of episode setting
			# detect cash and pnalize oherwise good reward
			if XplaneEnv.CLIENT.getDREFs(self.ControlParameters.on_ground)[0][0] >= 1 or XplaneEnv.CLIENT.getDREFs( self.ControlParameters.crash)[0][0] <=0:
				self.ControlParameters.flag = True # end of episode flag
				self.ControlParameters.reset = False # this checks that duplicate penalizaion is not aplied especiall when sim 
													 # frequency is high
				if self.ControlParameters.episodeStep <= 1.:
					self.ControlParameters.reset = True
					#print('reset', self.ControlParameters.reset )
				elif not self.ControlParameters.reset:
					self.episodeReward -=  3.
					print("crash", self.ControlParameters.episodeReward)
					self.ControlParameters.totalReward = self.ControlParameters.episodeReward
					#self.ControlParameters.totalReward -= 1
				else: 
					pass
				
			elif self.ControlParameters.episodeStep > self.max_episode_steps:
				self.ControlParameters.flag = True
				self.ControlParameters.totalReward  = self.ControlParameters.episodeReward
			###########################################################################
	
			###########################################################################
			# end of pisode is ue then reset end of episode paameters
			if self.ControlParameters.flag:
				reward = self.ControlParameters.totalReward 
				#print(reward, 'reward' , self.ControlParameters.totalReward, self.ControlParameters.episodeReward )
				#self.ControlParameters.flag = True
				self.ControlParameters.totalReward=0.
				self.ControlParameters.episodeStep = 0
				#self.episode_steps=0
				self.actions = [0,0,0,0] 
			else:
				reward = self.ControlParameters.episodeReward
			###########################################################################
			

		except:
			reward = self.ControlParameters.episodeReward
			self.ControlParameters.flag = False
			self.ControlParameters.state14 =  self.ControlParameters.state14
			if test:
				state.append(0)
				state14 = state
			else:
				state14 = [i for i in self.ControlParameters.state14.values()]
		#print(reward, 'reward' , self.ControlParameters.totalReward, self.ControlParameters.episodeReward )
		q=clock() # end of loop timer 
		#print("pause estimate", q-j)
		return  np.array(state14),reward,self.ControlParameters.flag,self._get_info() #self.ControlParameters.state14


   

  

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
		self.actions = [0,0,0,0] 
		self.ControlParameters.stateAircraftPosition = []
		self.ControlParameters.stateVariableValue = []
		self.ControlParameters.episodeReward  = 0.
		self.ControlParameters.totalReward  = 0.
		self.ControlParameters.flag = False
		#self.episode_steps = 0
		self.ControlParameters.episodeStep = 0
		self.ControlParameters.state14 = dict.fromkeys(self.ControlParameters.state14.keys(),0)
		#print(self.ControlParameters.state14)
		#stater  = [0,4]
		#state = {'value':  np.array([stater[0], stater[1]]).shape(2,)}
		#print(state)
		#val = 1
		state = np.zeros(11)
		
		return state # self.ControlParameters.state14
