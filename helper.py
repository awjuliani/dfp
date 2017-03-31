import numpy as np
import random
import tensorflow as tf
import scipy.misc
import os
import csv
import itertools
import tensorflow.contrib.slim as slim
from PIL import Image
from PIL import ImageDraw 
from PIL import ImageFont


# Copies one set of variables to another.
# Used to set worker network parameters to those of global network.
def update_target_graph(from_scope,to_scope):
    from_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, from_scope)
    to_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, to_scope)

    op_holder = []
    for from_var,to_var in zip(from_vars,to_vars):
        op_holder.append(to_var.assign(from_var))
    return op_holder

#Used to initialize weights for policy and value output layers
def normalized_columns_initializer(std=1.0):
    def _initializer(shape, dtype=None, partition_info=None):
        out = np.random.randn(*shape).astype(np.float32)
        out *= std / np.sqrt(np.square(out).sum(axis=0, keepdims=True))
        return tf.constant(out)
    return _initializer


#This code allows gifs to be saved of the training episode for use in the Control Center.
def make_gif(images, fname, duration=2, true_image=False):
  import moviepy.editor as mpy
  
  def make_frame(t):
    try:
      x = images[int(len(images)/duration*t)]
    except:
      x = images[-1]

    if true_image:
      return x.astype(np.uint8)
    else:
      return ((x+1)/2*255).astype(np.uint8)
  
  clip = mpy.VideoClip(make_frame, duration=duration)
  clip.write_gif(fname, fps = len(images) / duration,verbose=False)

def set_image_gridworld(frame,measurements,step,goal,hero):
    b = np.ones([840,640,3]) * 255.0
    b = Image.fromarray(b.astype('uint8'))
    draw = ImageDraw.Draw(b)
    font = ImageFont.truetype("./resources/FreeSans.ttf", 24)
    draw.text((240, 670),'Step: ' + str(step),(0,0,0),font=font)
    draw.text((240, 720),'Battery: ' + str(measurements[1]),(0,0,0),font=font)
    draw.text((240, 770),'Deliveries: ' + str(measurements[0]),(0,0,0),font=font)
    c = np.array(b)
    drone = np.array(Image.open('./resources/drone.png'))
    c[hero[0]*128:hero[0]*128+128,hero[1]*128:hero[1]*128+128,:] = drone
    battery = np.array(Image.open('./resources/battery.png'))
    c[0:128,0:128,:] = battery
    house = np.array(Image.open('./resources/house.png'))
    c[goal[0]*128:goal[0]*128+128,goal[1]*128:goal[1]*128+128,:] = house
    return c

def set_image_gridworld_reward(frame,reward,step,goal,hero):
    b = np.ones([840,640,3]) * 255.0
    b = Image.fromarray(b.astype('uint8'))
    draw = ImageDraw.Draw(b)
    font = ImageFont.truetype("./resources/FreeSans.ttf", 24)
    draw.text((240, 670),'Step: ' + str(step),(0,0,0),font=font)
    draw.text((240, 720),'Deliveries: ' + str(reward),(0,0,0),font=font)
    c = np.array(b)
    drone = np.array(Image.open('./resources/drone.png'))
    c[hero[0]*128:hero[0]*128+128,hero[1]*128:hero[1]*128+128,:] = drone
    house = np.array(Image.open('./resources/house.png'))
    c[goal[0]*128:goal[0]*128+128,goal[1]*128:goal[1]*128+128,:] = house
    return c
