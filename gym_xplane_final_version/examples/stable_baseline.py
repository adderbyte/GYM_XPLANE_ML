import argparse

import gym_xplane
import p3xpc 
import gym
import os
import time

from stable_baselines.common.policies import MlpPolicy,LstmPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import PPO2
from stable_baselines.common.vec_env import SubprocVecEnv
from stable_baselines.bench import Monitor





if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    #client = p3xpc.XPlaneConnect()
    # Create unique log dir
    log_dir = "./gym/{}".format(int(time.time()))
    os.makedirs(log_dir, exist_ok=True)
    
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
    
    env = Monitor(env, log_dir, allow_early_resets=True)

    #env.seed(123)
    
    n_cpu = 1

    env = DummyVecEnv([lambda: env])  # The algorithms require a vectorized environment to run
   
    
    
    model = PPO2(MlpPolicy, env, verbose=1)
    model.learn(total_timesteps=1000000)
    #PPO2('MlpPolicy', env, verbose=1).learn(1000)
   


