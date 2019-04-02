import ray
from ray.tune.registry import register_env
from ray.rllib.agents.ppo import PPOAgent
import gym_xplane

def env_creator(env_config):
    import gym
    return gym.make("gymXplane-v2")  # or return your own custom env

env_creator_name = "gymXplane-v2"
register_env(env_creator_name, env_creator)

ray.init()
agent = PPOAgent(env=env_creator_name, config={
    "env_config": {},  # config to pass to env creator
})

