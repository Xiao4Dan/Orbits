#vPython object voyage program
#simulation of object movements in space, with calculation of energy
#Ryerson University Fall2016 PCS110 A_S_
#~
from __future__ import division
from visual import *
from visual.graph import *

# CONSTANTS
G = 6.7e-11
mEarth = 6e24
mCraft = 15e3
mMoon = 7e22
delta_t = 10
t_0 = 0
t_f = 60*24*60*60        ## 60 days


# OBJECTS AND INITIAL VALUES
display( title='A space-craft voyage from the Earth to the Moon, and back',
         x = 0, y = 200, width = 1000, height = 500 )

Earth = sphere(pos=vector(0,0,0), radius=12.8e6, color=color.cyan)
craft = sphere(pos=vector(-5*Earth.radius, 0,0),radius = 3e6, color=color.yellow)
Moon = sphere(pos=vector(4e8,0,0), radius=3.5e6, color=color.red) 

vCraft = vector(0,3.27e3,0)
pCraft = mCraft*vCraft

trail = curve(color=craft.color)    ## craft trail: starts with no points

# Create graph axes for plotting the energies of the system
KUgraph = gdisplay(title = 'K, U, and K + U vs. t',
                   x = 0, y = 0, width = 500, height = 200)
Kcurve = gcurve(color = color.yellow)
Ucurve = gcurve(color = color.red)
KUcurve = gcurve(color = color.cyan)

# create the graph axes for plotting the cumulative work
Wgraph = gdisplay(title = 'Cummulative Work done on craft',
                  x = 500, y = 0, width = 200, height = 200)
Wcurve = gcurve(clor = color.green)

# CALCULATIONS
t=t_0
W=0
while t < t_f:
    rate(40000)

    ## update Gravitational Force (Earth and Spacecraft)
    rEarthCraft = craft.pos - Earth.pos
    rhatEarthCraft = rEarthCraft / mag( rEarthCraft )
    magFEarth = ((G * mCraft * mEarth) / mag2( rEarthCraft ))
    FEarth = -magFEarth * rhatEarthCraft

    ## update Gravitational Force (Moon and Spacecraft)
    rMoonCraft = craft.pos - Moon.pos
    rhatMoonCraft = rMoonCraft / mag( rMoonCraft )
    magFMoon = ((G * mCraft * mMoon) / mag2( rMoonCraft ) )
    FMoon = -magFMoon * rhatMoonCraft

    Fnet = FEarth + FMoon
    
    # check to see if the spacecraft has crashed on the Earth
    if mag( rEarthCraft ) < Earth.radius:
        break

    if mag( rMoonCraft ) < Moon.radius:
        break

    ## momentum
    pCraft = pCraft + (Fnet*delta_t)

    ## update Position
    delta_r = (pCraft/mCraft)*delta_t
    craft.pos = craft.pos + delta_r

    # Calculate energies of the system (consisting of all three objects)
    K = (Fnet.x * delta_r.x)+(Fnet.y * delta_r.y)+(Fnet.z * delta_r.z)
    ## you must complete this line
    U = -K
    ## you must complete this; omit the constant term for the Earth-Moon

    # Calculate cumulative work done internally by the system.
    W = W + K
    # you must complete this line.

    # Add the data to the 4 curves in the plots
    Kcurve.plot(pos = (t,K))
    Ucurve.plot(pos = (t,U))
    KUcurve.plot(pos = (t,K+U))
    Wcurve.plot(pos = (t,W))
    ## this adds the new position of the spacecraft to the trail
    trail.append(pos=craft.pos)
    t = t+delta_t
    
print 'Calculations finished after ', t, 'seconds'

    
