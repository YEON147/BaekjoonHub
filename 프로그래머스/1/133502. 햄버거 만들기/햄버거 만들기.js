function solution(ingredient) {
    let stack = [];
    let ans = 0;
    for (const i of ingredient) {
        stack.push(i);
        if (stack.length >= 4) {
            if (stack.slice(-4).join('') === '1231') {
                stack.length -= 4;
                ans++
            }
        }
    }
    return ans;
}