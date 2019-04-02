"""Example of a custom training workflow. Run this for a demo.
This example shows:
  - using Tune trainable functions to implement custom training workflows
You can visualize experiment results in ~/ray_results using TensorBoard.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import ray
from ray.rllib.agents.ppo import PPOAgent
from ray.tune import run_experiments
import gym_xplane
import gym 
from ray.tune.registry import register_env


def env_creator(env_config):
    import gym
    return gym.make("gymXplane-v2")  # or return your own custom env



def my_train_fn(config, reporter):
    # Train for 100 iterations with high LR
    import gym
    import gym_xplane
    env_creator_name = "gymXplane-v2"
    #env = gym.make("gymXplane-v2")
    register_env(env_creator_name, env_creator)
    agent1 = PPOAgent(env=env_creator_name, config=config)
    for _ in range(10):
        result = agent1.train()
        result["phase"] = 1
        reporter(**result)
        phase1_time = result["timesteps_total"]
    state = agent1.save()
    agent1.stop()


    


if __name__ == "__main__":
    ray.init()
    run_experiments({
        "demo": {
            "run": my_train_fn,
            "resources_per_trial": {
                "cpu": 1,
            },
            "config": {
                "lr": 0.01,
                "num_workers": 0,
            },
        },
    })
