#vPython object voyage program
#simulation of object movements in space
#Ryerson University Fall2016 PCS110 A_S_
#~
from __future__ import division 
from visual import * 

scene.width =1024 
scene.height = 760 

#CONSTANTS 
G = 6.7e-11 
mEarth = 6e24
mmoon = 7e22
mcraft = 15e3 
deltat = 10

#OBJECTS AND INITIAL VALUES 
Earth = sphere(pos=vector(0,0,0), radius=6.4e6, color=color.cyan)
Moon = sphere(pos=vector(4e8,0,0), radius = 1.75e6, color=color.white)
craft = sphere(pos=vector(-10*Earth.radius, 0,0), radius = 5e5, color=color.yellow) 
vcraft = vector(0,3.27e3,0) 
pcraft = mcraft*vcraft 
trail = curve(color=craft.color)    ## craft trail: starts with no points 
t = 0 
scene.autoscale = 0       ## do not allow camera to zoom in or out 

#CALCULATIONS 
while t < 60*24*60*60: 
    ##rate(200)       ## slow down motion to make animation look nicer 
    ## you must add statements for the iterative update of 
    ## gravitational force, momentum, and position
    rearth = craft.pos - Earth.pos
    remag = sqrt((rearth.x)**2+(rearth.y)**2+(rearth.z)**2)
    rehat = rearth/remag
    Fearth = G*mEarth*mcraft/(remag**2)
    
    rmoon = craft.pos - Moon.pos
    rmmag = sqrt((rmoon.x)**2+(rmoon.y)**2+(rmoon.z)**2)
    rmhat = rmoon/rmmag
    Fmoon = G*mmoon*mcraft/(rmmag**2)
    
    F = -Fearth*rehat-Fmoon*rmhat
    pcraft = pcraft + F*deltat
    craft.pos = craft.pos + pcraft* deltat/mcraft
    ## check to see if the spacecraft has crashed on the Earth. 
    ## if so, get out of the calculation loop 
    if remag < Earth.radius:
        break
    if rmmag < Moon.radius:
        break

    trail.append(pos=craft.pos) ## this adds the new position of the spacecraft to the trail 
    t = t+deltat 
print( 'Calculations finished after '),t,#('"seconds'")
