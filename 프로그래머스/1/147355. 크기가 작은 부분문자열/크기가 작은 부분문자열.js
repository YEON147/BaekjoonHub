function solution(t, p) {
    let cnt = 0;
    const N = p.length
    for (let i=0; i <= t.length-N; i++){
        const str = t.slice(i, i+N);
        if (+str <= +p) cnt += 1;
    }
    return cnt;
}