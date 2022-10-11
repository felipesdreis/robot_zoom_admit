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

x, y = pgui.position()
print('Iniciando monitoração...')

# busca botão na tela
def buscaAdmit(x, y):
    pgui.moveTo(x, y)
    locationAdmit = pgui.locateCenterOnScreen('btn_admit.png')
    if locationAdmit:
        xAdmit = locationAdmit.x
        yAdmit = locationAdmit.y
        pgui.moveTo(xAdmit, yAdmit)
        print('admit')
        time.sleep(0.5)
        pgui.click()

# monitoração continua
while True:
    time.sleep(2)
    yInicio = y - 100
    yFim = y + 150
    for yNext in range(yInicio, yFim, 25):
        buscaAdmit(x, yNext)