function solution(myString) {
    var answer = [];
    for (const i of myString.split('x')){
        console.log(i)
        answer.push(i.length);
    }
    return answer;
}