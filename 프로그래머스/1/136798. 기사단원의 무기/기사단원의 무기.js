function solution(number, limit, power) {
    const num = Array.from({ length: number }, (_, i) => i + 1);

    return num.map(v => {
        let cnt = 0;
        for (let n = 1; n * n <= v; n++) {
            if (v % n === 0) {
                cnt += (n * n === v) ? 1 : 2;
            }
        }
        return cnt <= limit ? cnt : power;
    }).reduce((a, c) => a + c, 0);
}