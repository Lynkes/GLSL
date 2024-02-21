#ifdef GL_ES
precision mediump float;
#endif

float tvStatic(vec2 st, float time) {
    float staticNoise = 0.1 * perlinNoise(st * 10.0 + time);
    return smoothstep(0.5, 0.51, staticNoise);
}
