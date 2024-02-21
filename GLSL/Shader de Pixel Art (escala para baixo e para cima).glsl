#ifdef GL_ES
precision mediump float;
#endif

vec3 pixelate(vec2 st, vec2 resolution, float pixelSize) {
    vec2 pixel = vec2(1.0) / resolution;
    vec2 uv = floor(st / pixelSize) * pixelSize;
    return texture(someTexture, uv).rgb;
}
