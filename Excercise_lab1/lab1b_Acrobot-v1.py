import gym
import time
env = gym.make('Acrobot-v1')
#  Acrobot is a 2-link pendulum with only the second joint actuated.
#     Initially, both links point downwards. The goal is to swing the
#     end-effector at a height at least the length of one link above the base.
#     Both links can swing freely and can pass by each other, i.e., they don't
#     collide when they have the same angle.


for i_episode in range(5):
    cumreward = []
    observation = env.reset()    
    print("The initial observation is {}".format(observation))


    for t in range(200):
        env.render(mode = 'rgb_array')
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        # time.sleep(0.01)
        print("Observation {} ".format(observation))

        # The state consists of the sin() and cos() of the two rotational joint
        # angles and the joint angular velocities :
        # [cos(theta1) sin(theta1) cos(theta2) sin(theta2) thetaDot1 thetaDot2].
        # For the first link, an angle of 0 corresponds to the link pointing downwards.
        # The angle of the second link is relative to the angle of the first link.
        # An angle of 0 corresponds to having the same angle between the two links.
        # A state of [1, 0, 1, 0, ..., ...] means that both links point downwards.

        print("Action {} ".format(action))
        # The action is either applying +1, 0 or -1 torque on the joint between
        # the two pendulum links.
        
        print("Reward {} ".format(reward))
        # Reward is 1 for every step taken, including the termination step

        
        cumreward.append(reward)


        if done:
            print("Cumulatitive reward {} ".format(sum(cumreward)))
            print("Episode finished after {} timesteps".format(t+1))
            break

        
print(reward,type(reward))
print(action,type(action))
print(observation,type(observation))

env.close()
