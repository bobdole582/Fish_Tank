#Basic imports
import sys
import time
## from random import randint, random

#Panda specific imports
from direct.showbase.ShowBase import ShowBase
from pandac.PandaModules import *
from direct.gui.DirectGui import *
from direct.task import Task 
from direct.actor import Actor 
from direct.interval.IntervalGlobal import * 


#Program specific imports
from joystick import *

class MyApp(DirectObject):
 
    def __init__(self):
        
        #Load the first environment model 
        self.panda = Actor.Actor("models/panda-model",{"walk":"models/panda-walk4"}) 
        self.panda.setScale(.005) 
        self.panda.reparentTo(render) 
        ## self.pandaP1.loop("walk") 
        # create the carot object to aid in moving the panda forward
        self.pandaCarot=NodePath("Carot")
        self.pandaCarot.reparentTo(self.panda)
        self.pandaCarot.setPos(0,-400,0)  # large distance to offset the panda scale
        
        # set the camera
        base.disableMouse()
        base.camera.setPosHpr(15,-70,55, 12, -40, 10) 
    

        
        
        # setup general accepts
        self.accept("escape", self.exit)                        # Exit the program when escape is pressed 
        
        # setup input devices
        self.setJoysticks()
        
        
        
        

################## GAME FUNCTIONS ############################################


                                    
                                    
                            
            
            
###################### JOYSTICKS #############################################

    def setJoysticks(self):
        #set up joysticks
        self.numSticks = 0
        self.events = []
        self.js = []
        self.js_axis = []
        for i in range(self.numSticks):
            self.events.append( self.setupButtonEvents(i))
            self.js.append(joystick.Joy(self.events[i],i))
            self.js_axis.append([0,0,0,0])
        # uncomment to poll the axis sticks
        ## taskMgr.doMethodLater(.1,self.pollAxis, 'pollAxisTask')
        
    def setupButtonEvents(self,num):
        # create button event handler conections
        events = {}
        self.accept(str(num) + "_joyButton0-up",self.ButtonHit, [num, 0, 1])                                                                                                                     
        self.accept(str(num) + "_joyButton0-down",self.ButtonHit, [num, 0, 0])
        events[0] = "joyButton0"
        self.accept(str(num) + "_joyButton1-up",self.ButtonHit, [num, 1, 1])
        self.accept(str(num) + "_joyButton1-down",self.ButtonHit, [num, 1, 0])
        events[1] = "joyButton1"
        self.accept(str(num) + "_joyButton2-up",self.ButtonHit, [num, 2, 1])
        self.accept(str(num) + "_joyButton2-down",self.ButtonHit, [num, 2, 0])
        events[2] = "joyButton2"
        self.accept(str(num) + "_joyButton3-up",self.ButtonHit, [num, 3, 1])
        self.accept(str(num) + "_joyButton3-down",self.ButtonHit, [num, 3, 0])
        events[3] = "joyButton3"
        self.accept(str(num) + "_joyButton4-up",self.ButtonHit, [num, 4, 1])
        self.accept(str(num) + "_joyButton4-down",self.ButtonHit, [num, 4, 0])
        events[4] = "joyButton4"
        self.accept(str(num) + "_joyButton5-up",self.ButtonHit, [num, 5, 1])
        self.accept("joyButton5-down",self.ButtonHit, [num, 5, 0])
        events[5] = "joyButton5"
        self.accept(str(num) + "_joyButton6-up",self.ButtonHit, [num, 6, 1])
        self.accept(str(num) + "_joyButton6-down",self.ButtonHit, [num, 6, 0])
        events[6] = "joyButton6"
        self.accept(str(num) + "_joyButton7-up",self.ButtonHit, [num, 7, 1])
        self.accept(str(num) + "_joyButton7-down",self.ButtonHit, [num, 7, 0])
        events[7] = "joyButton7"
        self.accept(str(num) + "_joyButton8-up",self.ButtonHit, [num, 8, 1])
        self.accept(str(num) + "_joyButton8-down",self.ButtonHit, [num, 8, 0])
        events[8] = "joyButton8"
        self.accept(str(num) + "_joyButton9-up",self.ButtonHit, [num, 9, 1])
        self.accept(str(num) + "_joyButton9-down",self.ButtonHit, [num, 9, 0])
        events[9] = "joyButton9"
        self.accept(str(num) + "_joyButton10-up",self.ButtonHit, [num, 10, 1])
        self.accept(str(num) + "_joyButton10-down",self.ButtonHit, [num, 10, 0])
        events[10] = "joyButton10"
        self.accept(str(num) + "_joyButton11-up",self.ButtonHit, [num, 11, 1])
        self.accept(str(num) + "_joyButton11-down",self.ButtonHit, [num, 11, 0])
        events[11] = "joyButton11"
        
        self.accept(str(num) + "_joyHatUp",self.ButtonHit, [num, 12, False])
        events[12] = "joyHatUp"
        self.accept(str(num) + "_joyHatDown",self.ButtonHit, [num, 13, False])
        events[13] = "joyHatDown"
        self.accept(str(num) + "_joyHatLeft",self.ButtonHit, [num, 14, False])
        events[14] = "joyHatLeft"
        self.accept(str(num) + "_joyHatRight",self.ButtonHit, [num, 15, False])
        events[15] = "joyHatRight"
        self.accept(str(num) + "_joyHatCenter",self.ButtonHit, [num, 16, False])
        events[16] = "joyHatCenter"
        return events
        
    def ButtonHit(self,control,button,up):
        # handle joystick button hits
        ## print button,up
        #Button 0 
        if (button == 0):
            if (up):  # UP
                print "button0 up for control", control
            else:     # DOWN
                print "button0 down for control", control
        #Button 1 
        elif (button == 1):
            if (up):  # UP
                print "button1 up for control", control
            else:     # DOWN
                print "button1 down for control", control
        #Button 2 
        elif (button == 2):
            if (up):  # UP
                print "button2 up for control", control
            else:     # DOWN
                print "button2 down for control", control
        #Button 3 
        elif (button == 3):
            if (up):  # UP
                print "button3 up for control", control
            else:     # DOWN
                print "button3 down for control", control
        #Button 4 
        elif (button == 4):
            if (up):  # UP
                print "button4 up for control", control
            else:     # DOWN
                print "button4 down for control", control
        #Button 5 
        elif (button == 5):
            if (up):  # UP
                print "button5 up for control", control
            else:     # DOWN
                print "button5 down for control", control
        #Button 6 
        elif (button == 6):
            if (up):  # UP
                print "button6 up for control", control
            else:     # DOWN
                print "button6 down for control", control
        #Button 7 
        elif (button == 7):
            if (up):  # UP
                print "button7 up for control", control
            else:     # DOWN
                print "button7 down for control", control
        #Button 8 
        elif (button == 8):
            if (up):  # UP
                print "button8 up for control", control
            else:     # DOWN
                print "button8 down for control", control
        #Button 9 
        elif (button == 9):
            if (up):  # UP
                print "button9 up for control", control
            else:     # DOWN
                print "button9 down for control", control
        #Button 10 
        elif (button == 10):
            if (up):  # UP
                print "button10 up for control", control
            else:     # DOWN
                print "button10 down for control", control
        #Button 11 
        elif (button == 11):
            if (up):  # UP
                print "button11 up for control", control
            else:     # DOWN
                print "button11 down for control", control
        
        
        #Button 12 - hat 
        elif (button == 12):
            print "button hat up for control", control
        #Button 13 - hat 
        elif (button == 13):
            print "button hat down for control", control
        #Button 14 - hat 
        elif (button == 14):
            print "button hat left for control", control
        #Button 15 - hat 
        elif (button == 15):
            print "button hat right for control", control
        #Button 16 - hat 
        elif (button == 16):
            print "button hat center for control", control
          

    def pollAxis(self,task):
        # poll the axis sticks on the joystick
        for i in range(4):
            for j in range(self.numSticks):
                ## # raw data - range -1to1
                ## self.js_axis[j][i] = self.js[j].getAxis(i)
                ## # inverted
                ## self.js_axis[j][i] = self.js[j].getAxis(i,True)
                ## # convert to range 0to2
                ## self.js_axis[j][i] = self.js[j].getAxis(i) + 1
                # rounded to two decimal places
                self.js_axis[j][i] = round(self.js[j].getAxis(i),2)
                print "joy", j,"axis", i, ":", self.js_axis[j][i]

        return task.again
                
      
###################### SYSTEM ################################################

    def exit(self):
        print 'bye'
        sys.exit()
        
        
app = MyApp()
## app.run()
run()