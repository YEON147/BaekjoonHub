function solution(n, m, section) {
    // n미터의 벽, 롤러 m미터, 페인트 재작접 필요구역 section
    // 롤러 < n 
    var ans = 0;
    let cur = 0;
    for (const i of section) {
        if (cur >= n) break
        
        if (cur < i){
            ans += 1
            cur = i + (m-1)
        }
    };
    return ans;
}