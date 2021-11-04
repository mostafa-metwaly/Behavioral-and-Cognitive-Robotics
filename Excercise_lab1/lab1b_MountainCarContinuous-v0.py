import gym
import time
env = gym.make('MountainCarContinuous-v0')
    #       Description:
    #     The agent (a car) is started at the bottom of a valley. For any given
    #     state the agent may choose to accelerate to the left, right or cease
    #     any acceleration.
for i_episode in range(5):
    cumreward = []
    
    observation = env.reset()
    print("The initial observation is {}".format(observation))
    # Starting State:
    #      The position of the car is assigned a uniform random value in
    #      [-0.6 , -0.4].
    #      The starting velocity of the car is always assigned to 0.

    for t in range(100):
        env.render(mode = 'rgb_array')
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        time.sleep(0.01)
        print("Observation {} ".format(observation))
        # Observation:
        #     Type: Box(2)
        #     Num    Observation               Min            Max
        #     0      Car Position              -1.2           0.6
        #     1      Car Velocity              -0.07          0.07

        print("Action {} ".format(action))
        # Actions:
        #     Type: Box(1)
        #     Num    Action                    Min            Max
        #     0      the power coef            -1.0           1.0
        #     Note: actual driving force is calculated by multiplying the power coef by power (0.0015)

        print("Reward {} ".format(reward))
        # Reward:
        #      Reward of 100 is awarded if the agent reached the flag (position = 0.45) on top of the mountain.
        #      Reward is decrease based on amount of energy consumed each step.
        cumreward.append(reward)


        if done:
            print("Cumulatitive reward {} ".format(sum(cumreward)))
            print("Episode finished after {} timesteps".format(t+1))
            break
        # Episode Termination:
        #      The car position is more than 0.45
        #      Episode length is greater than 200

print(reward,type(reward))
print(action,type(action))
print(observation,type(observation))

env.close()
