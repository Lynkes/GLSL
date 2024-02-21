import glfw
import glm
from OpenGL.GL import *
import numpy as np
from OpenGL.GL.shaders import compileProgram, compileShader
import glm

# Defina a posição da câmera, ponto de destino e vetor para cima
viewPos = glm.vec3(0, 0, 2)
viewTarget = glm.vec3(0, 0, 0)
up = glm.vec3(0, 1, 0)

# Crie a matriz de visualização manualmente
view = glm.lookAt(viewPos, viewTarget, up)

projection = glm.perspective(glm.radians(45.0), (800 / 600), 0.1, 100.0)


# Função para criar um programa de shader
def createShaderProgram(vertex_shader_source, fragment_shader_source):
    vertex_shader = compileShader(vertex_shader_source, GL_VERTEX_SHADER)
    fragment_shader = compileShader(fragment_shader_source, GL_FRAGMENT_SHADER)
    shader_program = compileProgram(vertex_shader, fragment_shader)
    return shader_program

# Função para desenhar um objeto
def desenhaObjeto(objeto):
    glUniform1f(glGetUniformLocation(Shader_program, "KaR"), objeto["KaR"])
    glUniform1f(glGetUniformLocation(Shader_program, "KaG"), objeto["KaG"])
    glUniform1f(glGetUniformLocation(Shader_program, "KaB"), objeto["KaB"])
    glUniform1f(glGetUniformLocation(Shader_program, "KdR"), objeto["KdR"])
    glUniform1f(glGetUniformLocation(Shader_program, "KdG"), objeto["KdG"])
    glUniform1f(glGetUniformLocation(Shader_program, "KdB"), objeto["KdB"])
    glUniform1f(glGetUniformLocation(Shader_program, "KsR"), objeto["KsR"])
    glUniform1f(glGetUniformLocation(Shader_program, "KsG"), objeto["KsG"])
    glUniform1f(glGetUniformLocation(Shader_program, "KsB"), objeto["KsB"])
    glUniform1f(glGetUniformLocation(Shader_program, "n"), objeto["n"])
    glUniform1f(glGetUniformLocation(Shader_program, "Tx"), objeto["Tx"])
    glUniform1f(glGetUniformLocation(Shader_program, "Ty"), objeto["Ty"])
    glUniform1f(glGetUniformLocation(Shader_program, "Sx"), objeto["Sx"])
    glUniform1f(glGetUniformLocation(Shader_program, "Sy"), objeto["Sy"])
    glUniform1f(glGetUniformLocation(Shader_program, "Rotacao"), objeto["Rotacao"])

    glBindVertexArray(objeto["VAO"])
    glDrawArrays(GL_TRIANGLES, 0, len(objeto["vertices"]) // 3)
    glBindVertexArray(0)

# Inicializa o GLFW
glfw.init()
glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
Window = glfw.create_window(800, 600, "Cena 2D", None, None)
glfw.make_context_current(Window)

# Define os vértices da casa
vertices_casa = np.array([
    -0.3, -0.5, 0.0,
    0.3, -0.5, 0.0,
    0.3, 0.5, 0.0,
    -0.3, -0.5, 0.0,
    -0.3, 0.5, 0.0,
    0.3, 0.5, 0.0,
], dtype=np.float32)

# Define os vértices do objeto 1
vertices_objeto1 = np.array([
    -0.1, -0.2, 0.0,
    0.1, -0.2, 0.0,
    0.1, 0.2, 0.0,
    -0.1, -0.2, 0.0,
    -0.1, 0.2, 0.0,
    0.1, 0.2, 0.0,
], dtype=np.float32)

# Define os vértices do objeto 2
vertices_objeto2 = np.array([
    -0.15, -0.3, 0.0,
    0.15, -0.3, 0.0,
    0.15, -0.2, 0.0,
    -0.15, -0.3, 0.0,
    -0.15, -0.2, 0.0,
    0.15, -0.2, 0.0,
], dtype=np.float32)

# Define os vértices do telhado
vertices_telhado = np.array([
    0.0, 0.5, 0.0,
    -0.2, 0.2, 0.0,
    0.2, 0.2, 0.0,
], dtype=np.float32)

# Define os vértices da porta
vertices_porta = np.array([
    -0.05, -0.5, 0.0,
    0.05, -0.5, 0.0,
    0.05, 0.0, 0.0,
    -0.05, -0.5, 0.0,
    -0.05, 0.0, 0.0,
    0.05, 0.0, 0.0,
], dtype=np.float32)

# Configuração da casa
objeto_casa = {
    "VAO": glGenVertexArrays(1),
    "VBO": glGenBuffers(1),
    "vertices": vertices_casa,
    "KaR": 0.3, "KaG": 0.3, "KaB": 0.3,
    "KdR": 0.9, "KdG": 0.9, "KdB": 0.9,
    "KsR": 0.8, "KsG": 0.8, "KsB": 0.8,
    "n": 32,
    "Tx": 0.0, "Ty": 0.0, "Sx": 1.0, "Sy": 1.0, "Rotacao": 0.0
}

# Configuração do objeto 1
objeto_objeto1 = {
    "VAO": glGenVertexArrays(1),
    "VBO": glGenBuffers(1),
    "vertices": vertices_objeto1,
    "KaR": 0.5, "KaG": 0.5, "KaB": 0.5,
    "KdR": 0.2, "KdG": 0.8, "KdB": 0.2,
    "KsR": 0.5, "KsG": 0.5, "KsB": 0.5,
    "n": 64,
    "Tx": -0.2, "Ty": 0.0, "Sx": 1.0, "Sy": 1.0, "Rotacao": 0.0
}

# Configuração do objeto 2
objeto_objeto2 = {
    "VAO": glGenVertexArrays(1),
    "VBO": glGenBuffers(1),
    "vertices": vertices_objeto2,
    "KaR": 0.7, "KaG": 0.2, "KaB": 0.2,
    "KdR": 0.8, "KdG": 0.2, "KdB": 0.2,
    "KsR": 0.1, "KsG": 0.1, "KsB": 0.1,
    "n": 128,
    "Tx": 0.2, "Ty": 0.0, "Sx": 1.0, "Sy": 1.0, "Rotacao": 0.0
}

# Configuração do telhado
objeto_telhado = {
    "VAO": glGenVertexArrays(1),
    "VBO": glGenBuffers(1),
    "vertices": vertices_telhado,
    "KaR": 0.3, "KaG": 0.3, "KaB": 0.3,
    "KdR": 0.9, "KdG": 0.9, "KdB": 0.9,
    "KsR": 0.8, "KsG": 0.8, "KsB": 0.8,
    "n": 32,
    "Tx": 0.0, "Ty": 0.35, "Sx": 1.0, "Sy": 1.0, "Rotacao": 0.0
}

# Configuração da porta
objeto_porta = {
    "VAO": glGenVertexArrays(1),
    "VBO": glGenBuffers(1),
    "vertices": vertices_porta,
    "KaR": 0.6, "KaG": 0.4, "KaB": 0.2,
    "KdR": 0.6, "KdG": 0.4, "KdB": 0.2,
    "KsR": 0.1, "KsG": 0.1, "KsB": 0.1,
    "n": 64,
    "Tx": 0.0, "Ty": -0.2, "Sx": 1.0, "Sy": 1.0, "Rotacao": 0.0
}

# Define os shaders
vertex_shader_source = """
#version 330 core
layout(location = 0) in vec3 aPos;
out vec3 FragPos;
uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;
void main()
{
    gl_Position = projection * view * model * vec4(aPos, 1.0);
    FragPos = vec3(model * vec4(aPos, 1.0));
}
"""

fragment_shader_source = """
#version 330 core
out vec4 FragColor;
in vec3 FragPos;
uniform vec3 lightPos;
uniform vec3 viewPos;
uniform vec3 lightColor;
uniform vec3 objectColor;
uniform float KaR, KaG, KaB;
uniform float KdR, KdG, KdB;
uniform float KsR, KsG, KsB;
uniform float n;
uniform float Tx, Ty, Sx, Sy, Rotacao;
void main()
{
    vec3 lightDir = normalize(lightPos - FragPos);
    vec3 viewDir = normalize(viewPos - FragPos);
    vec3 normal = normalize(cross(dFdx(FragPos), dFdy(FragPos)));
    float ambientStrength = 0.1;
    vec3 ambient = ambientStrength * lightColor;
    float diff = max(dot(normal, lightDir), 0.0);
    vec3 diffuse = diff * lightColor;
    float spec = pow(max(dot(reflect(-lightDir, normal), viewDir), 0.0), n);
    vec3 specular = spec * lightColor;
    vec3 objectColorAdjusted = vec3(KaR, KaG, KaB) * objectColor + vec3(KdR, KdG, KdB) * objectColor * diff + vec3(KsR, KsG, KsB) * specular;
    FragColor = vec4(objectColorAdjusted, 1.0);
}
"""

# Compila os shaders
Shader_program = createShaderProgram(vertex_shader_source, fragment_shader_source)
glUseProgram(Shader_program)


viewPos = glm.vec3(0, 0, 2)
viewTarget = glm.vec3(0, 0, 0)
up = glm.vec3(0, 1, 0)

# Crie a matriz de visualização manualmente
view = glm.lookAt(viewPos, viewTarget, up)

projection = glm.perspective(glm.radians(45.0), (800 / 600), 0.1, 100.0)




# Configuração da câmera
model = np.eye(4, dtype=np.float32)
view = np.eye(4, dtype=np.float32)
projection = np.eye(4, dtype=np.float32)

viewPos = np.array([0.0, 0.0, 2.0], dtype=np.float32)
lightPos = np.array([1.0, 1.0, 2.0], dtype=np.float32)
lightColor = np.array([1.0, 1.0, 1.0], dtype=np.float32)
objectColor = np.array([1.0, 0.5, 0.31], dtype=np.float32)

# Matriz de visualização (view)
view = np.eye(4, dtype=np.float32)
view = glm.lookAt(glm.vec3(0, 0, 2), glm.vec3(0, 0, 0), glm.vec3(0, 1, 0))

projection = np.eye(4, dtype=np.float32)
projection = glm.perspective(glm.radians(45.0), (800 / 600), 0.1, 100.0)


model_loc = glGetUniformLocation(Shader_program, "model")
view_loc = glGetUniformLocation(Shader_program, "view")
proj_loc = glGetUniformLocation(Shader_program, "projection")
viewPos_loc = glGetUniformLocation(Shader_program, "viewPos")
lightPos_loc = glGetUniformLocation(Shader_program, "lightPos")
lightColor_loc = glGetUniformLocation(Shader_program, "lightColor")
objectColor_loc = glGetUniformLocation(Shader_program, "objectColor")

glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)
glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)
glUniform3fv(viewPos_loc, 1, viewPos)
glUniform3fv(lightPos_loc, 1, lightPos)
glUniform3fv(lightColor_loc, 1, lightColor)
glUniform3fv(objectColor_loc, 1, objectColor)

# Loop principal
while not glfw.window_should_close(Window):
    glfw.poll_events()
    
    glClearColor(0.2, 0.3, 0.3, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    
    glUseProgram(Shader_program)
    glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)
    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)
    
    desenhaObjeto(objeto_casa)
    desenhaObjeto(objeto_objeto1)
    desenhaObjeto(objeto_objeto2)
    desenhaObjeto(objeto_telhado)
    desenhaObjeto(objeto_porta)
    
    glUseProgram(0)
    
    glfw.swap_buffers(Window)

glfw.terminate()
