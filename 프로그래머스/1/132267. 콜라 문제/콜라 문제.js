function solution(a, b, n) {
    let ans = 0;
    while (n >= a) {
        const ex = Math.floor(n / a);
        ans += ex * b;           
        n = ex * b + (n % a);          
    }
    return ans;
}