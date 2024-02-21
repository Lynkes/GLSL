import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np

Window = None
Shader_programm = None
Vao_quadrado = None
Vao_triangulo = None
Vao_Retangulo = None
Vao_Obj0 = None
Vao_Obj1 = None
Vao_Obj2 = None
Vao_Obj3 = None
Vao_retangulo_direita = None
Vao_quadrado_verde = None
Vao_Obj5 = None
WIDTH = 800
HEIGHT = 600

def redimensionaCallback(window, w, h):
    global WIDTH, HEIGHT
    WIDTH = w
    HEIGHT = h

def inicializaOpenGL():
    global Window, WIDTH, HEIGHT
    glfw.init()
    Window = glfw.create_window(WIDTH, HEIGHT, "Exemplo - renderização de um triângulo", None, None)
    if not Window:
        glfw.terminate()
        exit()
    glfw.set_window_size_callback(Window, redimensionaCallback)
    glfw.make_context_current(Window)

def inicializaTriangulo():
    global Vao_triangulo
    Vao_triangulo = glGenVertexArrays(1)
    glBindVertexArray(Vao_triangulo)
    points = [
        1.0, 0.0, 0.0,
        0.5, 0.5, 0.0,
        0.5, -0.5, 0.0
    ]
    points = np.array(points, dtype=np.float32)
    pvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, pvbo)
    glBufferData(GL_ARRAY_BUFFER, points, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
    cores = [
        1.0, 0.7, 0.2,
        1.0, 0.7, 0.2,
        1.0, 0.7, 0.2
    ]
    cores = np.array(cores, dtype=np.float32)
    cvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, cvbo)
    glBufferData(GL_ARRAY_BUFFER, cores, GL_STATIC_DRAW)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

def inicializaQuadrado():
    global Vao_quadrado
    Vao_quadrado = glGenVertexArrays(1)
    glBindVertexArray(Vao_quadrado)
    points = [
        0.5, 0.5, 0.0,
        0.5, -0.5, 0.0,
        -0.5, -0.5, 0.0,
        -0.5, 0.5, 0.0,
        0.5, 0.5, 0.0,
        -0.5, -0.5, 0.0
    ]
    points = np.array(points, dtype=np.float32)
    pvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, pvbo)
    glBufferData(GL_ARRAY_BUFFER, points, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
    cores = [
        0.2, 0.2, 0.2,
        0.2, 0.2, 0.2,
        0.2, 0.2, 0.2,
        0.2, 0.2, 0.2,
        0.2, 0.2, 0.2,
        0.2, 0.2, 0.2
    ]
    cores = np.array(cores, dtype=np.float32)
    cvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, cvbo)
    glBufferData(GL_ARRAY_BUFFER, cores, GL_STATIC_DRAW)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

def inicializaRetangulo():
    global Vao_Retangulo
    Vao_Retangulo = glGenVertexArrays(1)
    glBindVertexArray(Vao_Retangulo)
    points = [
        0.0, 0.3, 0.0,
        -0.5, 0.1, 0.0,
        -0.5, 0.3, 0.0,
        0.0, 0.1, 0.0,
        -0.5, 0.1, 0.0,
        0.0, 0.3, 0.0
    ]
    points = np.array(points, dtype=np.float32)
    pvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, pvbo)
    glBufferData(GL_ARRAY_BUFFER, points, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
    cores = [
        0.5, 0.2, 0.1,
        0.5, 0.2, 0.1,
        0.5, 0.2, 0.1,
        0.5, 0.2, 0.1,
        0.5, 0.2, 0.1,
        0.5, 0.2, 0.1
    ]
    cores = np.array(cores, dtype=np.float32)
    cvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, cvbo)
    glBufferData(GL_ARRAY_BUFFER, cores, GL_STATIC_DRAW)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

def inicializaObj0():
    global Vao_Obj0
    Vao_Obj0 = glGenVertexArrays(1)
    glBindVertexArray(Vao_Obj0)
    points = [
        0.2, 0.4, 0.0,
        0.2, 0.2, 0.0,
        -0.1, 0.2, 0.0
    ]
    points = np.array(points, dtype=np.float32)
    pvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, pvbo)
    glBufferData(GL_ARRAY_BUFFER, points, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
    cores = [
        0.5, 0.5, 0.5,
        0.5, 0.5, 0.5,
        0.5, 0.5, 0.5
    ]
    cores = np.array(cores, dtype=np.float32)
    cvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, cvbo)
    glBufferData(GL_ARRAY_BUFFER, cores, GL_STATIC_DRAW)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

def inicializaShaders():
    vertex_code = """
        attribute vec4 position;
        attribute vec3 color;
        varying vec4 outColor;
        void main()
        {
            gl_Position = position;
            outColor = vec4(color, 1.0);
        }
    """

    fragment_code = """
        varying vec4 outColor;
        void main()
        {
            gl_FragColor = outColor;
        }
    """

    # Compila e linka os programas
    VertexShader = OpenGL.GL.shaders.compileShader(vertex_code, GL_VERTEX_SHADER)
    FragmentShader = OpenGL.GL.shaders.compileShader(fragment_code, GL_FRAGMENT_SHADER)

    global Shader_programm
    Shader_programm = OpenGL.GL.shaders.compileProgram(VertexShader, FragmentShader)

def inicializaObj1():
    global Vao_Obj1
    Vao_Obj1 = glGenVertexArrays(1)
    glBindVertexArray(Vao_Obj1)
    points = [
        0.15, 0.1, 0.0,
        0.15, -0.1, 0.0,
        -0.15, -0.1, 0.0,
        0.15, 0.1, 0.0,
        -0.15, 0.1, 0.0,
        -0.15, -0.1, 0.0
    ]
    points = np.array(points, dtype=np.float32)
    pvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, pvbo)
    glBufferData(GL_ARRAY_BUFFER, points, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
    cores = [
        0.6, 0.6, 0.6,
        0.6, 0.6, 0.6,
        0.6, 0.6, 0.6,
        0.6, 0.6, 0.6,
        0.6, 0.6, 0.6,
        0.6, 0.6, 0.6
    ]
    cores = np.array(cores, dtype=np.float32)
    cvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, cvbo)
    glBufferData(GL_ARRAY_BUFFER, cores, GL_STATIC_DRAW)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

def inicializaObj2():
    global Vao_Obj2
    Vao_Obj2 = glGenVertexArrays(1)
    glBindVertexArray(Vao_Obj2)
    points = [
        0.12, 0.08, 0.0,
        0.12, -0.08, 0.0,
        -0.08, -0.08, 0.0,
        0.12, 0.08, 0.0,
        -0.08, 0.08, 0.0,
        -0.08, -0.08, 0.0
    ]
    points = np.array(points, dtype=np.float32)
    pvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, pvbo)
    glBufferData(GL_ARRAY_BUFFER, points, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
    cores = [
        0.0, 0.5, 1.0,
        0.0, 0.5, 1.0,
        0.0, 0.5, 1.0,
        0.0, 0.5, 1.0,
        0.0, 0.5, 1.0,
        0.0, 0.5, 1.0
    ]
    cores = np.array(cores, dtype=np.float32)
    cvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, cvbo)
    glBufferData(GL_ARRAY_BUFFER, cores, GL_STATIC_DRAW)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

def inicializaObj3():
    global Vao_Obj3
    Vao_Obj3 = glGenVertexArrays(1)
    glBindVertexArray(Vao_Obj3)
    points = [
        0.05, 0.05, 0.0,
        0.05, -0.05, 0.0,
        -0.05, -0.05, 0.0,
        0.05, 0.05, 0.0,
        -0.05, 0.05, 0.0,
        -0.05, -0.05, 0.0
    ]
    points = np.array(points, dtype=np.float32)
    pvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, pvbo)
    glBufferData(GL_ARRAY_BUFFER, points, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
    cores = [
        0.0, 0.0, 0.0,
        0.0, 0.0, 0.0,
        0.0, 0.0, 0.0,
        0.0, 0.0, 0.0,
        0.0, 0.0, 0.0,
        0.0, 0.0, 0.0
    ]
    cores = np.array(cores, dtype=np.float32)
    cvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, cvbo)
    glBufferData(GL_ARRAY_BUFFER, cores, GL_STATIC_DRAW)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

def inicializaObj4():
    global Vao_retangulo_direita
    Vao_retangulo_direita = glGenVertexArrays(1)
    glBindVertexArray(Vao_retangulo_direita)
    points = [
        0.4, 0.5, 0.0,
        0.4, -0.5, 0.0,
        0.35, -0.5, 0.0,
        0.4, 0.5, 0.0,
        0.35, 0.5, 0.0,
        0.35, -0.5, 0.0
    ]
    points = np.array(points, dtype=np.float32)
    pvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, pvbo)
    glBufferData(GL_ARRAY_BUFFER, points, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
    cores = [
        0.0, 0.5, 0.1,
        0.0, 0.5, 0.1,
        0.0, 0.5, 0.1,
        0.0, 0.5, 0.1,
        0.0, 0.5, 0.1,
        0.0, 0.5, 0.1
    ]
    cores = np.array(cores, dtype=np.float32)
    cvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, cvbo)
    glBufferData(GL_ARRAY_BUFFER, cores, GL_STATIC_DRAW)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

def inicializaObj5():
    global Vao_Obj5
    Vao_Obj5 = glGenVertexArrays(1)
    glBindVertexArray(Vao_Obj5)
    points = [
        -0.1, -0.5, 0.0,
        0.1, -0.5, 0.0,
        0.1, 0.0, 0.0,
        -0.1, -0.5, 0.0,
        0.1, 0.0, 0.0,
        -0.1, 0.0, 0.0,
        -0.25, 0.0, 0.0,
        0.25, 0.0, 0.0,
        0.0, 0.3, 0.0
    ]
    points = np.array(points, dtype=np.float32)
    pvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, pvbo)
    glBufferData(GL_ARRAY_BUFFER, points, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
    cores = [
        0.5-5, 0.2, 0.1,
        0.5-5, 0.2, 0.1,
        0.5-5, 0.2, 0.1,
        0.5-5, 0.2, 0.1,
        0.5-5, 0.2, 0.1,
        0.5-5, 0.2, 0.1,
        0.0-5, 0.5, 0.1,
        0.0-5, 0.5, 0.1,
        0.0-5, 0.5, 0.1
    ]
    cores = np.array(cores, dtype=np.float32)
    cvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, cvbo)
    glBufferData(GL_ARRAY_BUFFER, cores, GL_STATIC_DRAW)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

def atualizaDesenho():
    global Shader_programm
    glClearColor(0.9, 0.9, 0.9, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glUseProgram(Shader_programm)
    glBindVertexArray(Vao_triangulo)
    glDrawArrays(GL_TRIANGLES, 0, 3)
    glBindVertexArray(Vao_quadrado)
    glDrawArrays(GL_TRIANGLES, 0, 6)
    glBindVertexArray(Vao_Retangulo)
    glDrawArrays(GL_TRIANGLES, 0, 6)
    glBindVertexArray(Vao_Obj0)
    glDrawArrays(GL_TRIANGLES, 0, 3)
    glBindVertexArray(Vao_Obj1)
    glDrawArrays(GL_TRIANGLES, 0, 6)
    glBindVertexArray(Vao_Obj2)
    glDrawArrays(GL_TRIANGLES, 0, 6)
    glBindVertexArray(Vao_Obj3)
    glDrawArrays(GL_TRIANGLES, 0, 6)
    glBindVertexArray(Vao_retangulo_direita)
    glDrawArrays(GL_TRIANGLES, 0, 6)
    glBindVertexArray(Vao_Obj5)
    glDrawArrays(GL_TRIANGLES, 0, 9)
    glUseProgram(0)
    glfw.swap_buffers(Window)

def main():
    global Window
    inicializaOpenGL()
    inicializaShaders()
    inicializaTriangulo()
    inicializaQuadrado()
    inicializaRetangulo()
    inicializaObj0()
    inicializaObj1()
    inicializaObj2()
    inicializaObj3()
    inicializaObj4()
    inicializaObj5()
    while not glfw.window_should_close(Window):
        glfw.poll_events()
        atualizaDesenho()
    glfw.terminate()

if __name__ == "__main__":
    main()