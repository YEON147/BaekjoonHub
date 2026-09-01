function solution(numbers, n){
    return numbers.reduce((sum, a) => sum > n ? sum : sum+a);
}