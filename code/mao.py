import pgzrun
from camera import cameracool as camera

WIDTH = 1000
HEIGHT = 100

FPS = 30

vel = 0 #max 5

carro = Actor('carro1', (WIDTH//2, 50))

def process():
    global vel
    if camera.class_name[2:] == "Like" and int(camera.np.round(camera.confidence_score * 100)) > 80:
        vel = 5
    elif camera.class_name[2:] == "No like" and int(camera.np.round(camera.confidence_score * 100)) > 80:
        vel = -5
    elif camera.class_name[2:] == "Pare" and int(camera.np.round(camera.confidence_score * 100)) > 80:
        vel = 0

def draw():
    screen.fill((255, 255, 255))
    carro.draw()

def update():
    process()

    if carro.x < WIDTH - (carro.width/2) and carro.x > 0 + (carro.width/2):
        carro.x = carro.x + vel 
    
    #Para evitar que o carro trave/saia da tela
    if carro.x >= WIDTH - (carro.width/2): #Direita
        carro.x = WIDTH - (carro.width/2 - 1)
    elif carro.x <= 0 + (carro.width/2): #Esquerda
        carro.x = 0 + (carro.width/2 + 1)
    
    #debug com teclado
    if keyboard.right:
        carro.x = carro.x + 5
    elif keyboard.left:
        carro.x = carro.x - 5

pgzrun.go()