function solution(signals) {
    function gcd(a, b) { return b === 0 ? a : gcd(b, a % b); }
    function lcm(a, b) { return (a * b) / gcd(a, b); }

    const cycles = signals.map(v => v.reduce((a, c) => a + c, 0));
    const limit = cycles.reduce((a, c) => lcm(a, c));

    for (let t = 1; t <= limit; t++) {
        const allYellow = signals.every(([g, y], i) => {
            const pos = (t - 1) % cycles[i];
            return pos >= g && pos < g + y;
        });
        if (allYellow) return t;
    }
    return -1;
}