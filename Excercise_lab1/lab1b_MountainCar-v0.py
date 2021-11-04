import gym
import time
env = gym.make('MountainCar-v0')
    # Description:
    #     The agent (a car) is started at the bottom of a valley. For any given
    #     state the agent may choose to accelerate to the left, right or cease
    #     any acceleration.


for i_episode in range(20):
    cumreward = []
    observation = env.reset()
    print("The initial observation is {}".format(observation))
    # Starting State:
    #      The position of the car is assigned a uniform random value in
    #      [-0.6 , -0.4].
    #      The starting velocity of the car is always assigned to 0.


    for t in range(500):
        env.render(mode = 'rgb_array')
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        time.sleep(0.001)
        print("Observation {} ".format(observation))
        # Observation:
        #     Type: Box(2)
        #     Num    Observation               Min            Max
        #     0      Car Position              -1.2           0.6
        #     1      Car Velocity              -0.07          0.07


        print("Action {} ".format(action))
        # Actions:
        #     Type: Discrete(3)
        #     Num    Action
        #     0      Accelerate to the Left
        #     1      Don't accelerate
        #     2      Accelerate to the Right
        #     Note: This does not affect the amount of velocity affected by the
        #     gravitational pull acting on the car.

        print("Reward {} ".format(reward))
        # Reward:
        #      Reward of 0 is awarded if the agent reached the flag (position = 0.5)
        #      on top of the mountain.
        #      Reward of -1 is awarded if the position of the agent is less than 0.5.


        cumreward.append(reward)

        if done:
            print("Cumulatitive reward {} ".format(sum(cumreward)))
            print("Episode finished after {} timesteps".format(t+1))
            break
            # Episode Termination:
            #   The car position is more than 0.5
            #   Episode length is greater than 200

print(reward,type(reward))
print(action,type(action))
print(observation,type(observation))

env.close()
