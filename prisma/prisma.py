from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

vertices = (
    ( 1,-5,-1),
    ( 1, 5,-1),
    (-1, 5,-1),
    (-1,-5,-1),
    ( 1,-5, 1),
    ( 1, 5, 1),
    (-1,-5, 1),
    (-1, 5, 1),
    )

linhas = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
    )

faces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

cores = ( (1,0,0.5),(1,1,0.5),(0,1,0.5),(1,1,1),(1,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

def Prisma():
    glBegin(GL_QUADS)
    i = 0
    for face in faces:
        glColor3fv(cores[i])
        for vertex in face:
           glVertex3fv(vertices[vertex])
        i = i+1
    glEnd()

    glColor3f(0,0.5,0)
    glBegin(GL_LINES)
    for linha in linhas:
        for vertice in linha:
            glVertex3fv(vertices[vertice])
    glEnd()

a = 0

def desenhaPrisma():
    glPushMatrix()
    glRotatef(-a,1,1,1)
    Prisma()
    glPopMatrix()
    

def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    desenhaPrisma()
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
glutCreateWindow("PRISMA")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-20)
glutTimerFunc(50,timer,1)
glutMainLoop()


