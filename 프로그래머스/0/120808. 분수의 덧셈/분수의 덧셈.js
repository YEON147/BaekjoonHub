function solution(numer1, denom1, numer2, denom2) {
    // 최대공약수
    const gcd = (a, b) => b === 0 ? a : gcd(b, a % b);

    // 최소공배수
    const lcm = denom1 * denom2 / gcd(denom1, denom2);

    // 통분 후 더하기
    let numer = numer1 * (lcm / denom1) + numer2 * (lcm / denom2);

    // 약분
    const g = gcd(numer, lcm);

    return [numer / g, lcm / g];
}