function solution(hp) {
    var count = 0;
    const a = Math.floor(hp/5);
    hp %= 5;
    const b = Math.floor(hp/3);
    hp %= 3;
    const c = Math.floor(hp/1);
    return a+b+c;
}