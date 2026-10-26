function solution(k, m, score) {
    let ans = 0;
    score.sort((a,b) => b-a);
    for (let i=m-1; i < score.length; i+=m) {
        ans += score[i]*m
    }
    return ans;
}