import pyautogui as pgui
import time
from progress.bar import Bar
pgui.FAILSAFE = False
print('Posicione o mouse em cima do seu nome na lista de participantes')
input("Aperte Enter para continuar...")
print("=============================")
print('POSICIONE O MOUSE...')
bar = Bar('Tempo para posicionar mouse', max=15)
for i in range(15):
    # Do some work
    time.sleep(1)
    bar.next()
bar.finish()

x,y = pgui.position()
print('Iniciando monitoração...')

while True:
    #up
    time.sleep(5)
    pgui.moveTo(x,y+50)
    time.sleep(1)
    locationAdmit = pgui.locateCenterOnScreen('btn_admit.png')
    #print(locationAdmit)
    if locationAdmit:        
        xAdmit = locationAdmit.x 
        yAdmit = locationAdmit.y 
        pgui.moveTo(xAdmit,yAdmit)
        print('admit')
        time.sleep(0.5)
        pgui.click()
    pgui.moveTo(x,y+100)
    time.sleep(1)
    locationAdmit = pgui.locateCenterOnScreen('btn_admit.png')
    #print(locationAdmit)
    if locationAdmit:        
        xAdmit = locationAdmit.x 
        yAdmit = locationAdmit.y 
        pgui.moveTo(xAdmit,yAdmit)
        print('admit')
        time.sleep(0.5)
        pgui.click()
    #down
    time.sleep(5)
    pgui.moveTo(x,y-50)
    time.sleep(1)
    locationAdmit = pgui.locateCenterOnScreen('btn_admit.png')
    #print(locationAdmit)
    if locationAdmit:        
        xAdmit = locationAdmit.x 
        yAdmit = locationAdmit.y 
        pgui.moveTo(xAdmit,yAdmit)
        print('admit')
        time.sleep(0.5)
        pgui.click()
    pgui.moveTo(x,y-100)
    time.sleep(1)
    locationAdmit = pgui.locateCenterOnScreen('btn_admit.png')
    #print(locationAdmit)
    if locationAdmit:        
        xAdmit = locationAdmit.x 
        yAdmit = locationAdmit.y 
        pgui.moveTo(xAdmit,yAdmit)
        print('admit')
        time.sleep(0.5)
        pgui.click()
