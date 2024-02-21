#version 330 core

out vec4 FragColor;
uniform float time;
uniform vec2 resolution;
uniform vec2 offset;
uniform float zoom;
uniform int maxIterations;
uniform int shaderOption; // Escolha o shader aqui (de 0 a 9)

// Funções de ruído e padrões
float random(vec2 st) {
    return fract(sin(dot(st.xy, vec2(12.9898, 78.233)) * 43758.5453));
}

float marble(vec2 st, float scale, float speed) {
    return 0.5 + 0.5 * sin(scale * st.y + time * speed + 10.0 * noise(st));
}

float hash(float n) {
    return fract(sin(n) * 43758.5453);
}

float valueNoise(vec2 P) {
    vec2 i = floor(P);
    vec2 f = fract(P);
    f = f * f * (3.0 - 2.0 * f);
    float a = hash(i);
    float b = hash(i + vec2(1.0, 0.0));
    float c = hash(i + vec2(0.0, 1.0));
    float d = hash(i + vec2(1.0, 1.0));
    return mix(mix(a, b, f.x), mix(c, d, f.x), f.y);
}

float cell(vec2 P, float rep) {
    P = mod(P, rep);
    vec2 Pi = floor(P);
    vec2 Pf = fract(P);
    float res = 8.0;
    for (int j = -1; j <= 1; j++)
        for (int i = -1; i <= 1; i++) {
            vec2 offset = vec2(float(i), float(j));
            vec2 d = offset - Pf + random(Pi + offset);
            float dist = dot(d, d);
            res = min(res, dist);
        }
    return sqrt(res);
}

void main() {
    vec2 st = gl_FragCoord.xy / resolution;
    float result = 0.0;

    if (shaderOption == 0) {
        // Ruído Perlin em 2D
        result = random(st + time);
    } else if (shaderOption == 1) {
        // Textura de Mármore
        result = marble(st, 5.0, 1.0);
    } else if (shaderOption == 2) {
        // Padrão de Grade
        vec2 grid = fract(st * 10.0);
        result = step(0.1, grid.x) * step(0.1, grid.y);
    } else if (shaderOption == 3) {
        // Padrão de Chevron
        result = step(0.5, mod(st.x, 1.0)) * step(0.5, mod(st.y, 1.0));
    } else if (shaderOption == 4) {
        // Padrão de Zebra
        result = step(0.5, mod(st.y, 1.0));
    } else if (shaderOption == 5) {
        // Padrão de Xadrez Aleatório
        result = mod(int(st.x) + int(st.y), 2);
    } else if (shaderOption == 6) {
        // Padrão de Mandelbrot
        vec2 c = (gl_FragCoord.xy + offset) / resolution;
        c = c * zoom - vec2(2.0, 1.0);
        vec2 z = vec2(0.0);
        int i;

        for (i = 0; i < maxIterations; i++) {
            z = z * z + c;
            if (length(z) > 2.0) break;
        }

        result = float(i) / float(maxIterations);
    } else if (shaderOption == 7) {
        // Ruído de Perlin em 3D
        result = random(vec3(st, time));
    } else if (shaderOption == 8) {
        // Ruído Worley (Celular)
        result = cell(st * 10.0, 10.0);
    } else if (shaderOption == 9) {
        // Ruído de Valor em 2D
        result = valueNoise(st * 10.0);
    }

    FragColor = vec4(vec3(result), 1.0);
}
