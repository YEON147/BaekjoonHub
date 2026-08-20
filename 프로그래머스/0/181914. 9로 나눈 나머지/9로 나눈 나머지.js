function solution(number) {
    return Math.floor(String(number)
        .split('')
        .reduce((sum, n) => sum + Number(n), 0)%9);
}