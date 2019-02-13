import argparse

import gym_xplane.envs.xplane_Env as xp
import p3xpc 


class RandomAgent(object):
    def __init__(self, action_space):
        self.action_space = action_space

    def act(self):
        return self.action_space.sample()



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    client = p3xpc.XPlaneConnect()
    parser.add_argument('--client', help='client',default=client)
    
    
    args = parser.parse_args()

    env = xp.xplane_Env_run(args.client)
    #env.seed(123)
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
