#ifdef GL_ES
precision mediump float;
#endif

float voronoi(vec2 st, float numCells) {
    vec2 cell = vec2(1.0) / numCells;
    vec2 id = floor(st / cell);

    vec2 minDist = vec2(1.0);
    for (float y = -1.0; y <= 1.0; y++) {
        for (float x = -1.0; x <= 1.0; x++) {
            vec2 neighbor = id + vec2(x, y);
            vec2 offset = random(neighbor) * 0.8 + 0.1;
            vec2 p = offset + vec2(x, y);
            vec2 diff = p - fract(st / cell + offset);
            minDist = min(minDist, dot(diff, diff));
        }
    }

    float voronoiValue = 1.0 - smoothstep(0.02, 0.04, sqrt(minDist));
    gl_FragColor = vec4(vec3(voronoiValue), 1.0);
}
