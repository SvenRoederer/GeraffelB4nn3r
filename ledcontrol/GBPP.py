 #!/usr/bin/python
#
# pwm-test
#######################################################################
# This outputs a pattern on gpio under wiringpi
# https://projects.drogon.net/raspberry-pi/wiringpi/
#######################################################################


# Variablen entsprechen den Buchstaben des Geraffel-Banners und 
# verweisen auf den jeweiligen GPIO-Port

#Pinbelegung laut RPi-Board
G=14
E1=15
R=18
A=23
F1=24
F2=25
E2=8
L=7

gpios =    [14, 15, 18, 23, 24, 25, 8, 7]
letters = ["G", "E1", "R", "A", "F1", "f2", "E2", "L"]
frequenz=100    #PWM-Frequenz in Hz

#LEDMUSTER:
ledpattern = [
    None,
     ]
    
from time import sleep
from GBB import GBB1

def playPattern():

  end=0


  print "init GPIO-ports"
  i=0
  while i in range(8):
    print "seting up GPIO: %d" %gpios[i]
    gpio = gpios[i]                         #aktuelen GPIO aus Liste nehmen
    GPIO.setup(gpio,GPIO.OUT)               #und auf Ausgang stellen
    print "pass - GPIO.setup"
    letters[i] = GPIO.PWM(gpio,frequenz)    #Buchstabe aus 1.Liste holen und als PWM schalten mit    
    print "pass - GPIO.PWM"
    letters[i].start(ledpattern[i])          #akt. Buchstaben mit akt. PWM Wert starten        
    print "pass - PWM.start"
    sleep(0.1)
    i += 1

  print "starting pattern"
  x=0
  last=0
  while x in range(len(ledpattern)):
    
    totaltime=(ledpattern[x+8])
    blendsteps=(ledpattern[x+9])
    blendtime = totaltime/(1000*blendsteps)
    #print "_____________________________________________________________________"
    #print "Blendtime-total: ", totaltime, " Millisek.    ", "Blendtime-Steps: ", blendtime, " sek."
    if (x+10) == len(ledpattern):
        end=1
        last=len(ledpattern)
    j=0
    while j in range (int(blendsteps)):
        i=0
        while i in range(8): 
            difference =(ledpattern[x+i+10-last]-ledpattern[x+i])
            intervall = difference/blendsteps
            pwm= int(ledpattern[x+i] + intervall * (j+1))
            # print "Listenwert: ", ledpattern[x+i], "  Sollwert: ",ledpattern[x+i+10-last], "in ",int(blendsteps), " Schritten"
            # print "Differenz : ", difference, "  Steps: ", intervall,"  Cycle: ",pwm
            
            letters[i].ChangeDutyCycle(pwm)
                      
            i += 1
        
       
        sleep(blendtime)   #Pause entsprechend der softblendtime 
        
        j += 1
        #print "x=",x,"  j=",j

    x +=10
    if end==1:
            break


  #Cleanup
          
#  PWM.stop()
  for i in range(8):
    letters[i].stop()          #akt. Buchstaben mit akt. PWM Wert starten        
    print "pass - GPIO.stop"

#  GPIO.cleanup()
#  G.stop()
#  E1.stop()
#  R.stop()
#  A.stop()
#  F1.stop()
#  F2.stop()
#  E2.stop()
#  L.stop()
