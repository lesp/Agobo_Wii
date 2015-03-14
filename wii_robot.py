import cwiid
import time
import agobo
import signal

button_delay = 0.1
speed = 80

agobo.init()

def forward():
    agobo.forward(speed)
    time.sleep(2)
    agobo.stop()

def left():
    agobo.spinLeft(speed)
    time.sleep(1)
    agobo.stop()

def right():
    agobo.spinRight(speed)
    time.sleep(1)
    agobo.stop()

def reverse():
    agobo.reverse(speed)
    time.sleep(2)
    agobo.stop()

print 'Press 1 + 2 on your Wii Remote now ...'
time.sleep(1)

try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print "Error opening wiimote connection"
  quit()

print 'Wii Remote connected...\n'
print 'Press some buttons!\n'
print 'Press PLUS and MINUS together to disconnect and quit.\n'

wii.rpt_mode = cwiid.RPT_BTN
 
while True:

  buttons = wii.state['buttons']


  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):  
    print '\nClosing connection ...'
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    exit(wii)  
  
  elif (buttons & cwiid.BTN_LEFT):
    print 'Left pressed'
    left()
    time.sleep(button_delay)         

  elif(buttons & cwiid.BTN_RIGHT):
    print 'Right pressed'
    right()
    time.sleep(button_delay)          

  elif (buttons & cwiid.BTN_UP):
    print 'Up pressed'
    forward()
    wii.rumble = 1
    time.sleep(button_delay)
    wii.rumble = 0
    
  elif (buttons & cwiid.BTN_DOWN):
    print 'Down pressed'
    reverse()
    wii.rumble = 1
    time.sleep(button_delay)
    wii.rumble = 0
    
  elif (buttons & cwiid.BTN_1):
    print 'Button 1 pressed'
    time.sleep(button_delay)          

  elif (buttons & cwiid.BTN_2):
    print 'Button 2 pressed'
    time.sleep(button_delay)          

  elif (buttons & cwiid.BTN_A):
    print 'Button A pressed'
    time.sleep(button_delay)          

  elif (buttons & cwiid.BTN_B):
    print 'Button B pressed'
    time.sleep(button_delay)          

  elif (buttons & cwiid.BTN_HOME):
    print 'Home Button pressed'
    time.sleep(button_delay)           
    
  elif (buttons & cwiid.BTN_MINUS):
    print 'Minus Button pressed'
    time.sleep(button_delay)   
    
  elif (buttons & cwiid.BTN_PLUS):
    print 'Plus Button pressed'
    time.sleep(button_delay)
