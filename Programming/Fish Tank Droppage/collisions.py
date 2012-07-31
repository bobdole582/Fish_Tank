from pandac.PandaModules import *
## import direct.directbase.DirectStart
## from direct.showbase.DirectObject import *


def createTraverser(show = False):  
    #initialize traverser
    base.cTrav = CollisionTraverser()
    if (show == True): base.cTrav.showCollisions(render)   
    
def createHandler(type):
    #Collision traversers tell collision handlers about collisions, and then
    #the handler decides what to do with the information.
    if   (type == 'Queue'):   cHandler = CollisionHandlerQueue()
    elif (type == 'Event'):   cHandler = CollisionHandlerEvent()
    elif (type == 'Pusher'):  cHandler = CollisionHandlerPusher()
    elif (type == 'Physics'): cHandler = CollisionHandlerPhysics()
    elif (type == 'Floor'):   cHandler = CollisionHandlerFloor()
    return cHandler
    
def setColMask(object, b, type = 'Into', allOff = False):
    #Collision objects are sorted using BitMasks. BitMasks are ordinary numbers
    #with extra methods for working with them as binary bits. Every collision
    #solid has both a from mask and an into mask. Before Panda tests two
    #objects, it checks to make sure that the from and into collision masks
    #have at least one bit in common. That way things that shouldn't interact
    #won't. Normal model nodes have collision masks as well. By default they
    #are set to bit 20. If you want to collide against actual visable polygons,
    #set a from collide mask to include bit 20
    if (type == 'Into' and allOff == False):   object.node().setIntoCollideMask(BitMask32.bit(b))
    elif (type == 'Into' and allOff == True):  object.node().setIntoCollideMask(BitMask32.allOff())
    elif (type == 'From' and allOff == False): object.node().setFromCollideMask(BitMask32.bit(b))
    elif (type == 'From' and allOff == True):  object.node().setFromCollideMask(BitMask32.allOff())
    else: print 'Problem with call to setColMask'
    
def setColMask2(objnode, b, type = 'Into', allOff = False):
    #Collision objects are sorted using BitMasks. BitMasks are ordinary numbers
    #with extra methods for working with them as binary bits. Every collision
    #solid has both a from mask and an into mask. Before Panda tests two
    #objects, it checks to make sure that the from and into collision masks
    #have at least one bit in common. That way things that shouldn't interact
    #won't. Normal model nodes have collision masks as well. By default they
    #are set to bit 20. If you want to collide against actual visable polygons,
    #set a from collide mask to include bit 20
    if (type == 'Into' and allOff == False):   objnode.setIntoCollideMask(BitMask32.bit(b))
    elif (type == 'Into' and allOff == True):  objnode.setIntoCollideMask(BitMask32.allOff())
    elif (type == 'From' and allOff == False): objnode.setFromCollideMask(BitMask32.bit(b))
    elif (type == 'From' and allOff == True):  objnode.setFromCollideMask(BitMask32.allOff())
    else: print 'Problem with call to setColMask'
    
def TrevAddCol(colNode, cHandler):
    #Add the collision nodes that can create a collision to the
    #traverser. The traverser will compare these to all others nodes in the
    #scene. There is a limit of 32 CollisionNodes per traverser
    #We add the collider, and the handler to use as a pair
    base.cTrav.addCollider(colNode, cHandler)
    
def TrevRemoveCol(colNode):
    #Remove the collision nodes that can create a collision to the
    #traverser. 
    base.cTrav.removeCollider(colNode)
    
def HandAddCol(fromObject, moveNode, cHandler):
    #The CollisionHandlerPusher needs to have a handle to the NodePath that it 
    #will push back on, for each from object. This should be the node that is 
    #actually moving. This is often, but not always, the same NodePath as the 
    #CollisionNode itself, but it might be different if the CollisionNode is set 
    #up as a child of the node that is actually moving.  
    #If PhysicsCollisionHandler then the moveNode must be an actor
    #If CollisionHandlerFloor then moveNode is, again, the object that is to be 
    #physically moved. 
    cHandler.addCollider(fromObject, moveNode)
    
def addPattern(cHandler, Str, dir = 'In'):
    #the CollisionHandlerEvent will construct an event name out of the names of the from and 
    #into objects that were involved in the collision. The exact event name is controlled by a 
    #pattern string that you specify. 
    #Str should be in the format '%fn-into-%in', '%fn-outof-%in', or '%fn-again-%in'
    #Dir = In - event is called when a collision occurs in this pass but not the previous pass
    #Dir = Again - event is called when a collision occurs in this pass and the previous pass
    #Dir = Out - event is called when the objects are no longer colliding
    if (dir == 'In'):    cHandler.addInPattern(Str)
    elif (dir == 'Again'): cHandler.addAgainPattern(Str)
    elif (dir == 'Out'):   cHandler.addOutPattern(Str)
  
  ############################################################################
  ## Collsions Solids
  ############################################################################
    
def createColSphere(obj, name, scale = 1.1, show = False):
    #Create a collision sphere - return the collision node
    cNode = CollisionNode(name)
    cNode.addSolid(CollisionSphere(0,0,0,scale))
    objC = obj.attachNewNode(cNode)
    if (show == True): objC.show()
    return objC

def createColRay(obj, origin, dir, name):
    #create a ray to start at the origin and cast in the direction dir. This is to
    #Determine the height an object should be at and the angle the floor is
    #tilting. 
    # Return the collisionNode
    Ray = CollisionRay()     #Create the ray
    Ray.setOrigin(origin)    #Set its origin
    Ray.setDirection(dir)    #And its direction
    #Collision solids go in CollisionNode
    Col = CollisionNode(name)  #Create and name the node
    Col.addSolid(Ray) #Add the ray
    objC = obj.attachNewNode(Col)
    return objC

def createColTube(obj, name, length, radius = 1.1, show = False):
    #Create a collision tube - return the collision node
    cNode = CollisionNode(name)
    cNode.addSolid(CollisionTube(0,0,0,length,0,0,radius))
    objC = obj.attachNewNode(cNode)
    if (show == True): objC.show()
    return objC