#ifdef GL_ES
precision mediump float;
#endif

float fireNoise(vec2 st) {
    return fract(sin(dot(st, vec2(12.9898,78.233)))*43758.5453123);
}

float fire(vec2 st) {
    st.y *= 3.0;
    float rnd = fireNoise(st);
    float pattern = smoothstep(0.2, 0.5, sin(st.x * 10.0) + cos(st.y * 10.0));

    return mix(0.5, pattern, rnd);
}
