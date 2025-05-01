# Modules
from goto import with_goto
from stddef import *
import var
import pio
import resource
from datetime import datetime

# Peripheral Configuration Code (Do Not Edit)
#---CONFIG_BEGIN---
import cpu
import FileStore
import timer
import VFP
import Grove
import Generic
import AdafruitHATs

def peripheral_setup () :
# Peripheral Constructors
 pio.cpu=cpu.CPU ()
 pio.storage=FileStore.FileStore ()
 pio.timer=timer.Timer ()
 pio.server=VFP.VfpServer ()
 pio.grove=Grove.Grove ()
 pio.PD1=Grove.GroveLuminanceSensor (0)
 pio.M1=Generic.DCMotorV1 (pio.GPIO5, pio.GPIO4, pio.GPIO6, )
 pio.M2=Generic.DCMotorV1 (pio.GPIO21, pio.GPIO20, pio.GPIO22, )
 pio.PD2=Grove.GroveLuminanceSensor (1)
 pio.GIP1=Grove.GroveInfraredProximitySensor (2)
 pio.BTN1=Generic.Button (pio.GPIO25)
 pio.U5=AdafruitHATs.Adafruit_16_Channel_Servo_HAT ("0", "0", "0", "0", "0", "0")
 pio.LCD1=Grove.GroveRgbLcd ()
 pio.storage.begin ()
 pio.server.begin (0)
 pio.M1.begin ()
 pio.M2.begin ()
# Install interrupt handlers

def peripheral_loop () :
 pio.timer.poll ()
 pio.server.poll ()

#---CONFIG_END---
def variables_setup () :
# Flowchart Variables
 var.Lux = 0.0
 var.Lux2 = 0.0
 var.Covered = False
 var.cm = 0.0
 var.VCDis = 0.0
 var.Locked = False
 var.Covered2 = False

# Flowchart Routines
@with_goto
def chart_SETUP () :
 pio.LCD1.noDisplay ()
 pio.U5.setMaxMinAngle (0, 90, -90)
 pio.U5.setMaxMinPulse (0, 2, 1)
 pio.U5.setAngle (0, 0)
 var.Locked=False
 return

@with_goto
def chart_LOOP () :
 chart_Elock ()
 chart_P2 ()
 chart_P1 ()
 sleep((1000)*0.001)
 chart_LuminanceVolt ()
 return

@with_goto
def chart_P2 () :
 var.Lux2 = pio.PD2.readLuminance ()
 if var.Lux2>900 :
  if var.Covered2==True :
   pio.M2.stop ()
  else :
   chart_CoverP2 ()
   chart_P2TC ()
  
 else :
  if var.Covered2==True :
   chart_unCoverP2 ()
  else :
   pio.M2.stop ()
  
 
 return

@with_goto
def chart_P1 () :
 var.Lux = pio.PD1.readLuminance ()
 if var.Lux>900 :
  if var.Covered==True :
   pio.M1.stop ()
  else :
   chart_CoverP1 ()
   chart_P1TC ()
  
 else :
  if var.Covered==True :
   chart_unCoverP1 ()
  else :
   pio.M1.stop ()
  
 
 return

@with_goto
def chart_CoverP2 () :
 pio.M2.run (1, 100)
 var.Covered2=True
 sleep((2000)*0.001)
 return

@with_goto
def chart_unCoverP2 () :
 pio.M2.run (0, 100)
 var.Covered2=False
 sleep((2000)*0.001)
 return

@with_goto
def chart_CoverP1 () :
 pio.M1.run (1, 100)
 var.Covered=True
 sleep((2000)*0.001)
 return

@with_goto
def chart_unCoverP1 () :
 pio.M1.run (0, 100)
 var.Covered=False
 sleep((2000)*0.001)
 return

@with_goto
def chart_Elock () :
 var.VCDis = pio.GIP1.readVoltage ()
 if var.VCDis>2 :
  if var.Locked==False :
   pio.U5.setAngle (0, 90)
   var.Locked=True
   chart_Caution ()
   chart_CoverBoards ()
  
 else :
  if pio.BTN1() :
   if var.Locked==False :
    pio.U5.setAngle (0, 90)
    var.Locked=True
    chart_CoverBoards ()
    chart_UserCoverDis ()
   else :
    pio.U5.setAngle (0, 0)
    var.Locked=False
    chart_unCoverBoards ()
    chart_UseruncoverDis ()
   
  
 
 return

@with_goto
def chart_CoverBoards () :
 chart_CoverP1 ()
 chart_CoverP2 ()
 return

@with_goto
def chart_unCoverBoards () :
 chart_unCoverP1 ()
 chart_unCoverP2 ()
 return

@with_goto
def chart_Caution () :
 pio.LCD1.clear ()
 pio.LCD1.display ()
 pio.LCD1.print ("Caution! Please Check")
 if var.Locked==False :
  sleep((500)*0.001)
  pio.LCD1.clear ()
  pio.LCD1.noDisplay ()
  chart_LuminanceVolt ()
 
 return

@with_goto
def chart_P1TC () :
 pio.LCD1.clear ()
 pio.LCD1.display ()
 pio.LCD1.print ("Covering P1 TOO HOT weather")
 if var.Lux<900 :
  sleep((500)*0.001)
  pio.LCD1.clear ()
  pio.LCD1.noDisplay ()
 else :
  chart_LuminanceVolt ()
 
 return

@with_goto
def chart_UserCoverDis () :
 pio.LCD1.clear ()
 pio.LCD1.display ()
 pio.LCD1.print ("oreders to cover P1 & P2 ")
 sleep((1000)*0.001)
 pio.LCD1.clear ()
 pio.LCD1.noDisplay ()
 chart_LuminanceVolt ()
 return

@with_goto
def chart_UseruncoverDis () :
 pio.LCD1.clear ()
 pio.LCD1.display ()
 pio.LCD1.print ("oreders to Uncover P1 & P2 ")
 sleep((1000)*0.001)
 pio.LCD1.clear ()
 pio.LCD1.noDisplay ()
 chart_LuminanceVolt ()
 return

@with_goto
def chart_P2TC () :
 pio.LCD1.clear ()
 pio.LCD1.display ()
 pio.LCD1.print ("Covering P2 TOO HOT weather")
 if var.Lux2<900 :
  sleep((500)*0.001)
  pio.LCD1.clear ()
  pio.LCD1.noDisplay ()
  chart_LuminanceVolt ()
 else :
  chart_LuminanceVolt ()
 
 return

@with_goto
def chart_LuminanceVolt () :
 pio.LCD1.clear ()
 pio.LCD1.display ()
 pio.LCD1.print (var.Lux, "  ", var.Lux2)
 sleep((1500)*0.001)
 return

# Main function
def main () :
# Setup
 variables_setup ()
 peripheral_setup ()
 chart_SETUP ()
# Infinite loop
 while True :
  peripheral_loop ()
  chart_LOOP ()
# Command line execution
if __name__ == '__main__' :
   main()
