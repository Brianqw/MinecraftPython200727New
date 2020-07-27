# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 10:58:34 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x=100.5
y=100.5
z=100.5
mc.player.setpos(x,y,z)
