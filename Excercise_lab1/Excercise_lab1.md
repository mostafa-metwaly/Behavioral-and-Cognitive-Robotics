## A) python script for Cartpole environment
performs an evaluation episode by showing
the behavior and by printing the step, the observation vector, the
action vector, the reward, and the fitness (i.e. the cumulative
reward)

## B) Analyze the implementation of two classic control environment
 ### (1) what is encoded in the observation vector 
* for Cartpole-v0: \
[ 0.17513729  1.53287277 -0.22794664 -2.47505599] <class 'numpy.ndarray'> 

        Num     Observation               Min                     Max
        0       Cart Position             -4.8                    4.8
        1       Cart Velocity             -Inf                    Inf
        2       Pole Angle                -0.418 rad (-24 deg)    0.418 rad (24 deg)
        3       Pole Angular Velocity     -Inf                    Inf
* for MountainCar-v0 : \
[-0.37612938  0.01045749] <class 'numpy.ndarray'>

        Type: Box(2)
        Num    Observation               Min            Max
        0      Car Position              -1.2           0.6
        1      Car Velocity              -0.07          0.07

* for MountainCarContinuous-v0 : \
[-0.37612938  0.01045749] <class 'numpy.ndarray'>

        Type: Box(2)
        Num    Observation               Min            Max
        0      Car Position              -1.2           0.6
        1      Car Velocity              -0.07          0.07

### (2) what is encoded in the action vector 
* for Cartpole-v0: 

        Type: Discrete(2)
        Num   Action
        0     Push cart to the left
        1     Push cart to the right
* for MountainCar-v0 : 
0 <class 'int'>

        Type: Discrete(3)
        Num    Action
        0      Accelerate to the Left
        1      Don't accelerate
        2      Accelerate to the Right


* for MountainCarContinuous-v0 : 

        Type: Box(1)
        Num    Action                    Min            Max
        0      the power coef            -1.0           1.0

### (3) how the reward is calculated 

* for Cartpole-v0: \
    Reward is 1 for every step taken, including the termination step


* for MountainCar-v0 : \
-1.0 <class 'float'> \
    Reward of 0 is awarded if the agent reached the flag (position = 0.5)
    on top of the mountain. \
    Reward of -1 is awarded if the position of the agent is less than 0.5.

* for MountainCarContinuous-v0 : \

        Reward of 100 is awarded if the agent reached the flag (position = 0.45) on top of the mountain. \
        Reward is decrease based on amount of energy consumed each step.


### (4) how the initial conditions are varied by the reset method 
* for Cartpole-v0: \
     All observations are assigned a uniform random value in [-0.05..0.05]


* for MountainCar-v0 : \
-1.0 <class 'float'> \
         The position of the car is assigned a uniform random value in
         [-0.6 , -0.4]. \
         The starting velocity of the car is always assigned to 0.


* for MountainCarContinuous-v0 : \
-1.0 <class 'float'> \
         The position of the car is assigned a uniform random value in
         [-0.6 , -0.4]. \
         The starting velocity of the car is always assigned to 0.




### (5) which are the termination conditions.

* for Cartpole-v0: \
            - Pole Angle is more than 12 degrees. \
            - Cart Position is more than 2.4 (center of the cart reaches the edge of
            the display). \
            - Episode length is greater than 200. \
            - Solved Requirements: 
            Considered solved when the average return is greater than or equal to
            195.0 over 100 consecutive trials.


* for MountainCar-v0 : \
            - The car position is more than 0.5 \
            - Episode length is greater than 200


* for MountainCarContinuous-v0 : \
            - The car position is more than 0.5 \
            - Episode length is greater than 200
