import argparse

#import gym_xplane.envs.xplane_Env as xp
import p3xpc 
import gym
import gym_xplane

class RandomAgent(object):
    def __init__(self, action_space):
        self.action_space = action_space

    def act(self):
        return self.action_space.sample()
	
def __init__():
	pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    client = p3xpc.XPlaneConnect()
    parser.add_argument('--client', help='client',default=client)
    #print(gym.__file__)
    #print(client)
    env=gym.make('gymXplane-v0')
    env.client = client
    
    agent = RandomAgent(env.action_space)
    
    
    episodes = 0
    while episodes < 100:
        obs = env.reset()
        done = False
        while not done:
            action = agent.act()
            obs, reward, done, _ = env.step(action) 

            print(obs, reward, done)
            
        episodes += 1

    env.close()
