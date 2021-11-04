import gym
import time
env = gym.make('CartPole-v1')
    # Description:
    #     A pole is attached by an un-actuated joint to a cart, which moves along
    #     a frictionless track. The pendulum starts upright, and the goal is to
    #     prevent it from falling over by increasing and reducing the cart's
    #     velocity.
for i_episode in range(20):
    cumreward = []

    observation = env.reset()
    print("The initial observation is {}".format(observation))
    # Starting State:
    #     All observations are assigned a uniform random value in [-0.05..0.05]

    for t in range(200):
        env.render(mode = 'rgb_array')
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        time.sleep(0.01)
        print("Observation {} ".format(observation))
        # Num     Observation               Min                     Max
        # 0       Cart Position             -4.8                    4.8
        # 1       Cart Velocity             -Inf                    Inf
        # 2       Pole Angle                -0.418 rad (-24 deg)    0.418 rad (24 deg)
        # 3       Pole Angular Velocity     -Inf                    Inf

        print("Reward {} ".format(reward))
        # Reward is 1 for every step taken, including the termination step

        print("Action {} ".format(action))
        # Actions:
        #     Type: Discrete(2)
        #     Num   Action
        #     0     Push cart to the left
        #     1     Push cart to the right
        #     Note: The amount the velocity that is reduced or increased is not
        #     fixed; it depends on the angle the pole is pointing. This is because
        #     the center of gravity of the pole increases the amount of energy needed
        #     to move the cart underneath it

        cumreward.append(reward)


        if done:
            print("Cumulatitive reward {} ".format(sum(cumreward)))
            print("Episode finished after {} timesteps".format(t+1))
            break
        # Episode Termination:
        #     Pole Angle is more than 12 degrees.
        #     Cart Position is more than 2.4 (center of the cart reaches the edge of
        #     the display).
        #     Episode length is greater than 200.
        #     Solved Requirements:
        #     Considered solved when the average return is greater than or equal to
        #     195.0 over 100 consecutive trials.

print(reward,type(reward))
print(action,type(action))
print(observation,type(observation))

env.close()
