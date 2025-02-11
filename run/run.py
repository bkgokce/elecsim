import sys

# import scenario_file
# sys.modules['elecsim'].scenario.scenario_data=scenario_file

from elecsim.model.world import World

import logging

# logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    world = World(2018, log_level="info", market_time_splices=8, number_of_steps=8)
    for day in range(8):
        world.step()
