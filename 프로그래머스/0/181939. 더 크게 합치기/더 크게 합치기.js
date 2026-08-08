function solution(a, b) {
    const [x, y] = [a + '' + b, b + '' + a];
    return +x > +y ? +x : +y;
}