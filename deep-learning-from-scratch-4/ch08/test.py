import gym
import pygame
from gym.utils.play import play
from gym.utils.play import PlayPlot
mapping = {(pygame.K_LEFT,): 0, (pygame.K_RIGHT,): 2}


def callback(obs_t, obs_tp1, action, rew, done, info):
    return [rew, ]


plotter = PlayPlot(callback, 30 * 5, ["reward"])
env = gym.make("MountainCar-v0")
play(env, callback=plotter.callback, keys_to_action=mapping)
