import gym
import numpy as np


class Network:

    def __init__(self,env , nhiddens):
        # nsensoryn = env.....
        # nmotorn = .....


        pvariance = 0.1     # variance of initial parameters
        ppvariance = 0.02   # variance of perturbations
        nhiddens = 5        # number of internal neurons
        # the number of inputs and outputs depends on the problem
        # we assume that observations consist of vectors of continuous value
        # and that actions can be vectors of continuous values or discrete actions
        ninputs = env.observation_space.shape[0]
        if (isinstance(env.action_space, gym.spaces.box.Box)):
            noutputs = env.action_space.shape[0]
        else:
            noutputs = env.action_space.n

        # initialize the training parameters randomly by using a gaussian
        # distribution with average 0.0 and variance 0.1
        # biases (thresholds) are initialized to 0.0
        W1 = np.random.randn(nhiddens,ninputs) * pvariance      # first connection layer
        W2 = np.random.randn(noutputs, nhiddens) * pvariance    # second connection layer
        b1 = np.zeros(shape=(nhiddens, 1))                      # bias internal neurons
        b2 = np.zeros(shape=(noutputs, 1))                      # bias motor neurons
        self.env_w = [W1 , W2 ,b1 ,b2 ,ninputs]

    def update(self,observation):
        W1 , W2 ,b1 ,b2 ,ninputs = self.env_w
        # change chape to be able to multiply the matrix between observation and connection and weights
        # convert the observation array into a matrix with 1 column and ninputs rows
        observation.resize(ninputs,1)
        # compute the netinput of the first layer of neurons
        Z1 = np.dot(W1, observation) + b1
        # compute the activation of the first layer of neurons with the tanh function
        A1 = np.tanh(Z1)
        # compute the netinput of the second layer of neurons
        Z2 = np.dot(W2, A1) + b2
        # compute the activation of the second layer of neurons with the tanh function
        A2 = np.tanh(Z2)
        # if the action is discrete
        #  select the action that corresponds to the most activated unit
        if (isinstance(env.action_space, gym.spaces.box.Box)):
            action = A2 # if the action is integer [0 , 1]
        else:
            action = np.argmax(A2)  #

        return(action)

    def evaluate(self, nepisodes):
        # env.render(mode = 'rgb_array')
        for e in range(nepisodes):
            observation = env.reset()
            done = 1
            reward = 0
            while not done :
                action = network.update(observation)
                observation, reward, done, info = env.step(action)
                print("done")
        return reward


#     def getnparameters(self):
#         adding all the parameters (w , b ..)



#         return nparameters




#     def setparameters(self, genotype):
        



# popsize = 10


env = gym.make('CartPole-v0')
network = Network(env,5)
fitness = network.evaluate(3)
