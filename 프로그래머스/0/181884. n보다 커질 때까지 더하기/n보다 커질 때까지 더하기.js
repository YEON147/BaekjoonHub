function solution(numbers, n) {
    var answer = 0;
    return numbers.reduce((sum, a) => sum > n ? sum : sum+a);
}