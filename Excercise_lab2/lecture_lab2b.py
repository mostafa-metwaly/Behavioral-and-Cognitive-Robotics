import time
from typing_extensions import Concatenate
import gym
import numpy as np
from numpy.core.fromnumeric import size

# Developing the algorithim with a neural network to be able to conduct the appropiate weight and bias to fit the model in.

class Network:

    def __init__(self,env , nhiddens):
        # nsensoryn = env.....
        # nmotorn = .....

        self.cumreward =[]
        self.pvariance = 0.1     # variance of initial parameters
        self.ppvariance = 0.02   # variance of perturbations
        self.nhiddens = nhiddens        # number of internal neurons
        # the number of inputs and outputs depends on the problem
        # we assume that observations consist of vectors of continuous value
        # and that actions can be vectors of continuous values or discrete actions
        self.ninputs = env.observation_space.shape[0]
        if (isinstance(env.action_space, gym.spaces.box.Box)):
            self.noutputs = env.action_space.shape[0]
        else:
            self.noutputs = env.action_space.n

        # initialize the training parameters randomly by using a gaussian
        # distribution with average 0.0 and variance 0.1
        # biases (thresholds) are initialized to 0.0
        W1 = np.random.randn(nhiddens,self.ninputs) * self.pvariance      # first connection layer
        W2 = np.random.randn(self.noutputs, nhiddens) * self.pvariance    # second connection layer
        b1 = np.zeros(shape=(nhiddens, 1))                      # bias internal neurons
        b2 = np.zeros(shape=(self.noutputs, 1))                      # bias motor neurons
        self.env_param = [W1, W2, b1, b2]


    def update(self,observation):
        W1 , W2 ,b1 ,b2  = self.env_param
        # change chape to be able to multiply the matrix between observation and connection and weights
        # convert the observation array into a matrix with 1 column and ninputs rows
        observation.resize(self.ninputs,1)
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
        cumreward = 0
        # self.env.render(mode = 'rgb_array')
        for e in range(nepisodes):
            observation = env.reset()
            done = False
            while not done :
                action = network.update(observation)
                observation, reward, done, info = env.step(action)
                cumreward += reward

                # print(sum(self.cumreward))

        return cumreward/nepisodes

    def render(self, nepisodes):

        for e in range(nepisodes):
            self.cumreward =[]
            observation = env.reset()
            done = False
            while not done :
                env.render()
                action = network.update(observation)
                observation, reward, done, info = env.step(action)
                self.cumreward.append(reward)
                time.sleep(0.05)
                print(sum(self.cumreward))
        env.close()
        return reward



    def getnparameters(self):
        all_param = np.array(self.env_param)
        a =[]
        # for idx,i in enumerate(self.env_param):
        for i in all_param:
            # print(np.shape(i))
            size = 1
            for dim in np.shape(i): 
                size *= dim
                # print(size)
            a.append(size)
            nparameters = sum(a)
        print(nparameters)
        # print("all_param : " , i.flatten())
        print(a)
        nparameters = len(all_param)
        print("nparameters " , nparameters)
        return nparameters




    def setparameters(self, genotype):
    #         setting the values of the genotype and adding the weights and biasses values.
            self.env_param = genotype
            return self.env_param

    def noise(self):
        noise = []

        pop = np.array(self.env_param)
        for i in pop:
            pops = np.random.randn(i.shape[0],i.shape[1]) * self.mutrange
            noise.append(pops)
        # print(noise)
        return noise



    def evolutionary_alg(self ):

        popsize = 10
        generange = 0.1
        self.mutrange = 0.02
        nepisodes = 3
        ngeneration = 100

        env = gym.make('CartPole-v0')

        # nparameters = network.getnparameters()
        # intialization of the population
        population = np.vstack((self.env_param for i in range(popsize) ))
        # print(population)
        self.population_const = population[0] *0+1

        
 

        # # # # return

        for g in range(ngeneration):
            fitness = []
            fit = 0 
            max_fit = []
            mean_fit = []

            for i in range(popsize):
                network.setparameters(population[i])
                fit = network.evaluate(nepisodes)
                fitness.append((fit, i))
                

            fitness.sort(key=lambda y: y[0])
            # print(fitness)
            max_fit = fitness[-1][0]
            mean_fit = (fitness[0][1]+fitness[-1][0])/popsize
            for a in range(int(popsize/2)):
                noise = network.noise()
                population[fitness[a][1]][:] = population[a + int(popsize/2)][:] + noise
            print("generation no.:",g)
            print("fitness mean :", mean_fit)
            print("max fitness :",max_fit)


# np.random.seed(2) # the Magic number is 8

env = gym.make('CartPole-v0')
network = Network(env,5)
fit = network.evolutionary_alg() 
render = network.render(1)
network.noise()