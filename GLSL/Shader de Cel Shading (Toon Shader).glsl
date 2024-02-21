#ifdef GL_ES
precision mediump float;
#endif

vec3 toonShading(vec3 color, float numLevels) {
    float shade = floor(color.r * numLevels) / numLevels;
    return vec3(shade, shade, shade);
}
