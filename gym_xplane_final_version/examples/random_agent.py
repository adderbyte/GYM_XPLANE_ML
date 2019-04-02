import argparse

import gym_xplane
import p3xpc 
import gym



class RandomAgent(object):
    def __init__(self, action_space):
        self.action_space = action_space

    def act(self):
        return self.action_space.sample()



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    #client = p3xpc.XPlaneConnect()
	
    
    #parser.add_argument('--client', help='client address',default=client)
    parser.add_argument('--clientAddr', help='xplane host address', default='0.0.0.0')
    parser.add_argument('--xpHost', help='x plane port', default='127.0.0.1')
    parser.add_argument('--xpPort', help='client port', default=49009)
    parser.add_argument('--clientPort', help='client port', default=1)
    
    args = parser.parse_args()

    env = gym.make('gymXplane-v2')
    env.clientAddr = args.clientAddr
    env.xpHost = args.xpHost
    env.xpPort = args.xpPort
    env.clientPort = args.xpPort
    

    #env.seed(123)
    agent = RandomAgent(env.action_space)

    episodes = 0
    while episodes < 50:
        obs = env.reset()
        done = False
        while not done:
            action = agent.act()
            obs, reward, done, _ = env.step(action) 

            print(obs, reward, done)
            #print(done)
        episodes += 1

    env.close()
