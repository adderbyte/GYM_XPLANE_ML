from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import ray
from ray.rllib.agents.ppo import PPOAgent
from ray.tune import run_experiments
import gym_xplane
import p3xpc 
import argparse
from ray.tune import run_experiments, grid_search

import gym



# def my_train_fn(config, reporter):
#     # Train for 100 iterations with high LR
#     agent1 = PPOAgent(env, config=config)
#     for _ in range(10):
#         result = agent1.train()
#         result["phase"] = 1
#         reporter(**result)
#         phase1_time = result["timesteps_total"]
#     state = agent1.save()
#     agent1.stop()

#     # Train for 100 iterations with low LR
#     config["lr"] = 0.0001
#     agent2 = PPOAgent(env, config=config)
#     agent2.restore(state)
#     for _ in range(10):
#         result = agent2.train()
#         result["phase"] = 2
#         result["timesteps_total"] += phase1_time  # keep time moving forward
#         reporter(**result)
#     agent2.stop()


if __name__ == "__main__":
    
    # parser = argparse.ArgumentParser()
    # #client = p3xpc.XPlaneConnect()
    
    
    # #parser.add_argument('--client', help='client address',default=client)
    # parser.add_argument('--clientAddr', help='xplane host address', default='10.2.168.32')
    # parser.add_argument('--xpHost', help='x plane port', default='127.0.0.1')
    # parser.add_argument('--xpPort', help='client port', default=49009)
    # parser.add_argument('--clientPort', help='client port', default=1)
    
    #args = parser.parse_args()
    ray.init(object_store_memory=10000000,redis_max_memory=10000000)
    #env = xp.xplane_Env_run(args.clientAddr, args.xpHost, args.xpPort,args.clientPort)
    
    #pic = pickle.dumps(client)
    #env = gym.make('gymXplane-v2')
    
    #register_env("corridor", lambda config: SimpleCorridor(config))
    #agent = PPOAgent(env)
    parser = argparse.ArgumentParser()
    #client = p3xpc.XPlaneConnect()
    # Create unique log dir
   
    
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
        

    
   


    run_experiments({
        "demo": {
            "run": "PPO",
            "env": env,  # or "corridor" if registered above
            "stop": {
                "timesteps_total": 10,
            },
    
        },
    })
