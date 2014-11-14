import launcher
import time
rockets = 0
l = launcher.launchControl() 

def reload():
    global rockets
    rockets = 4

def fire():
  global rockets
  print "click!"
  if rockets > 0:
    print "pew!"
    l.turretFire()
    rockets -= 1
  else:
    return False
  return True

def left(x):
  l.turretLeft(x/1000.0)

def right(x):
  l.turretRight(x/1000.0)

def up(x):
  l.turretUp(x/1000.0)

def down(x):
  l.turretDown(x/1000.0)

def stop():
   l.turretStop()

  
