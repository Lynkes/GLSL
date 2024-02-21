#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;

vec3 getColor(vec2 st) {
    vec3 blue = vec3(0.0, 0.2353, 1.0); // Amarelo
    vec3 yellow = vec3(1.0, 0.9843, 0.0);   // Azul

    st.x = 1.0 - st.x;

    float diagonalIntensity = smoothstep(0.2, 0.8, (st.x + st.y) / 2.0);
    return mix(blue, yellow, diagonalIntensity);
}

void main() {
    vec2 st = gl_FragCoord.xy / u_resolution;
    vec3 color = getColor(st);
    gl_FragColor = vec4(color, 1.0);
}
