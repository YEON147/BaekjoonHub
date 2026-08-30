function solution(number) {
    return Math.floor(number.split('').reduce((sum, a) => (sum+a)%9));
}