function solution(num_list) {
    let answer = 0;

    for (let i of num_list) {
        while (i > 1) {
            i = Math.floor(i / 2);
            answer++;
        }
    }

    return answer;
}