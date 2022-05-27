from elecsim.model.world import World 

number_of_years = 2
number_of_time_steps = 8

if __name__ == "__main__":
    world = World(2018, log_level="info", market_time_splices=8, number_of_steps=number_of_years*number_of_time_steps)
    for years in range(number_of_years):
        for time_steps in range(number_of_time_steps):
            world.step()