# available versions

from gym.envs.registration import register

register(
        id='binpacking_posco-v0',
        entry_point='binpacking_posco.envs:binpacking_posco_v0',
)