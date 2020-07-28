# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:55:01 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

w=100
h=100
l=100

x,y,z=mc.player.getTilePos()
mc.setBlocks(x,y,z,x+w,y+h,z+l,1)
mc.setBlocks(x+1,y+1,z+1,
             x+w-1,y+h-1,z+l-1,0)