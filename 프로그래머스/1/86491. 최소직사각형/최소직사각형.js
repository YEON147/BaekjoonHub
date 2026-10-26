function solution(sizes) {
    let [w, h] = [0, 0];
    sizes.forEach(v => {
        w = Math.max(w, ...v);
        h = Math.max(h, Math.min(...v));
    });
    return w * h;
}