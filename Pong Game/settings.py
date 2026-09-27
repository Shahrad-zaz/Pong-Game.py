import pygame
from os.path import join

WINDOWS_WIDTH, WINDOWS_HEIGHT = 1280, 720
SIZE = {'paddle':(40,100), 'ball' : (30,30)}
SPEED = {'player': 300, 'opponent': 250, 'ball': 450}
COLORS = {
    'paddle': '#ee322c',
    'paddle shadow': '#b12521',
    'ball': "#d0ff00",
    'ball shadow': "#97c124",
    'bg': '#002633'
}