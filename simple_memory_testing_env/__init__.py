from .env import *

import gym
from gym.envs.registration import register

env_dict = gym.envs.registration.registry.env_specs.copy()

for env in env_dict:
    if 'SimpleMemoryTestingEnv' in env:
        del gym.envs.registration.registry.env_specs[env]

register(
    id='SimpleMemoryTestingEnv-v0',
    entry_point='simple_memory_testing_env.env:generate_env'
)
