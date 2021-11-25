# Excercise 3
Training the model using Reinforcement Learning \

I have used Stable Baselines3 and the zoo to be able to integrate everything in one place and train and evaluate my models

## Installation
the installation was done with the help of the [Official Documentation](https://stable-baselines3.readthedocs.io/en/master/guide/install.html) \
For me I have used a Docker image to build everything inside and using Jupyter notebook I had access to the codes there.
also you could have a look on it [Docker image](https://github.com/naruya/dl_remote)
with some added modifications I have pushed the image on my [Docker Hub](https://hub.docker.com/repository/docker/mostafametwaly/docker-rl)

## Choosing the Problem
I will start with a simple problem the CartPole-v0 from the OpenAI Gym environments 

### Building the Model 
the model is build after specifying the environment of choice 

```python3
model = PPO('MlpPolicy', env, verbose = 1)
```
### Training the model 
after that we can start the training proccess, stating the number of timesteps we want to train for.

```python3
model.learn(total_timesteps=20000)
```
### Saving the model
then we can save the model to be able to load and use if afterwards

```python3 
model.save(PPOmodel_path)
```
### Evaluation
additionally we can evaluate the model performance using the evaluate_policy 

```python3
evaluate_policy(model, env, n_eval_episodes=10, render=True)
```
