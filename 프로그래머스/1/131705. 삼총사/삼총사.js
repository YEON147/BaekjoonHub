function solution(number) {
    // 세명 더했을때 0이되면 3명은 삼총사, 를 만들 수 있는 방법으 ㅣ수 
    let ans = 0;
    function dfs(cnt, start, sum) {
        if (cnt === 3) {
            if (sum === 0) ans++;
            return
        }
        for (let i = start; i < number.length; i++){
            dfs(cnt+1, i+1, sum+number[i]);
        }
    }
    dfs(0, 0, 0);
    return ans;
}