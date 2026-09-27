import pygame
from os.path import join

WINDOWS_WIDTH, WINDOWS_HEIGHT = 1280, 720
SIZE = {'paddle':(15,100), 'ball' : (30,30)}
POS1 = {'player':(WINDOWS_WIDTH-20, WINDOWS_HEIGHT/2), 'opponent' :(20, WINDOWS_HEIGHT/2)}
SPEED = {'player': 600, 'opponent': 600, 'ball': 550}
COLORS = {
    'paddle': "#06bbf7",
    'paddle shadow': "#0687b1",
    'ball': "#d0ff00",
    'ball shadow': "#5b6d0e0d",
    'bg': "#083949",
    'bg ditail': "#004a63"
}