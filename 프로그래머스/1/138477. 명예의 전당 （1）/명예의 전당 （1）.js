function solution(k, score) {
    var answer = [];
    const stage = [];
    for (const s of score) {
        stage.push(s);
        // 내림차순 정렬 
        stage.sort((a,b) => b-a);
        if (stage.length > k) stage.pop();
        answer.push(stage.at(-1));
    }
    return answer;
}