from gym.envs.registration import register

register(
    id='gymXplane-v0',
    entry_point='gym_xplane.envs:XplaneEnv',
)
