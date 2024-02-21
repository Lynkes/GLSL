#ifdef GL_ES
precision mediump float;
#endif

float marble(vec2 st, float scale, float turbulence) {
    float marbleValue = st.y + 0.5 * sin(scale * st.x + turbulence * perlinNoise(st));
    return 0.5 * sin(marbleValue * 10.0) + 0.5;
}
