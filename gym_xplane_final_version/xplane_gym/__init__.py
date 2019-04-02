from gym.envs.registration import register

register(
    id='gymXplane-v2',
    entry_point='gym_xplane.envs:XplaneEnv',
    kwargs={'clientAddr': '0.0.0.0', 'xpHost':'127.0.0.1', 'xpPort':49009, 'clientPort':1, 'timeout':3000, 'max_episode_steps':2000,'test':False}
)
