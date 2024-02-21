#ifdef GL_ES
precision mediump float;
#endif

float water(vec2 st, float time) {
    float wave = sin(st.x * 10.0 + time) + sin(st.y * 10.0 + time);
    return 0.5 + 0.5 * sin(wave);
}

