#ifdef GL_ES
precision mediump float;
#endif

float concentricCircles(vec2 st) {
    float distance = length(st - 0.5);
    return smoothstep(0.4, 0.41, distance) - smoothstep(0.5, 0.51, distance);
}
