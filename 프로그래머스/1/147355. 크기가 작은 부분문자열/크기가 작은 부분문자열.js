function solution(t, p) {
    //p자리수 문자열 중에서 p 이하의 수 등장 횟수 return
    var answer = 0;
    const N = p.length
    for (let i=0; i <= t.length-N; i++){
        const str = t.slice(i, i+N);
        if (Number(str) <= Number(p)) answer += 1;
    }
    return answer;
}