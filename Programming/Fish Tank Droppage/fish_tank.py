############################################################################
## Program: Fish Tank                                                     ##
## Programmers: John Groot, June Chew, Mitchell Vitez                     ##
## Purpose: Create the Fish Tank game as outlined in resources folder     ##
##                                                                        ##                                                                      
#  ERRORS:                                                                ##
##                                                                        ##
##                                                                        ##
##                                                                        ##
##                                                                        ##
##                                                                        ##
##                                                                        ##
############################################################################





from pandac.PandaModules import loadPrcFileData
from fish_tank_config import *
loadPrcFileData("", ORIGIN)
loadPrcFileData("", SIZE)
loadPrcFileData("", TITLE)

import sys

import direct.directbase.DirectStart                                     
from direct.showbase.DirectObject import DirectObject
from pandac.PandaModules import *
from direct.task import Task
from direct.interval.IntervalGlobal import *
from direct.gui.DirectGui import *
from direct.ETCleveleditor import LevelLoader
from direct.actor.Actor import Actor

import random


class World(DirectObject):
    def __init__(self):
        print 1
        
    def printer(self):
        print 2
        
w = World()
run()