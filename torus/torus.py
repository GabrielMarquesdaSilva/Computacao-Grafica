from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import numpy as np

r = 1
n = 50
halfpi = math.pi/2
R = 2
cor1= np.array ([255,255,0])/255
cor2= np.array ([0,144,144])

def f(u, v):
    theta = (u*2*math.pi)/(n-1)
    phi = (v*2*math.pi)/(n-1)
    x = (R + r*math.cos(theta))*math.cos(phi)
    y = (R + r*math.cos(theta))*math.sin(phi)
    z = r*math.sin(theta)
    return x, y, z

def get_color(t,t_max,cor1,cor2): 
    p = t/t_max
    new_color = cor1 + p*(cor2-cor1)         
    return new_color.astype(int)


def desenhaTorus():
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(n):
        for j in range(n):
            cor = get_color(i,n, cor1, cor2)
            glColor3fv(cor)
            glVertex3fv(f(i,j))
            glVertex3fv(f(i+1,j))
    glEnd()

a = 0

def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(a,1,1,1)
    desenhaTorus()    
    glPopMatrix()
    glutSwapBuffers()
    a += 1
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Torus")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-8)
glutTimerFunc(50,timer,1)
glutMainLoop()
