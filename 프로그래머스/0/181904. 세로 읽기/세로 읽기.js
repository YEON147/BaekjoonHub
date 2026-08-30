function solution(my_string, m, c) {
    var answer = [];
    const myStr = [...my_string]
    for (i=c-1; i < my_string.length; i += m){
        answer.push(myStr[i])
    }
    return answer.join('');
}