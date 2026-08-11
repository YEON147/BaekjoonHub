function solution(slice, n) {
    var ans = Math.floor(n/slice);
    return n%slice === 0 ? ans : ans + 1;
}