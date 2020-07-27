# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:32:53 2020

@author: user
"""
x=50
y=100
z=100
import time
x,y,z=mc.player.getTilePos()
time.sleep(5)

y=y+100
mc.player.setTilePos()
time.sleep(5)

y=y+100

mc.player.setTilePos(x,y,z)
time.sleep(5)
y=y+100
mc.player.setTilePos(x,y,z)

