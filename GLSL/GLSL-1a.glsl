#ifdef GL_ES
precision mediump float;
#endif
uniform vec2 u_resolution;
void main() {
 vec2 st = gl_FragCoord.xy/u_resolution;
 gl_FragColor = vec4(0.0,1.0,1.0,1.0);
}