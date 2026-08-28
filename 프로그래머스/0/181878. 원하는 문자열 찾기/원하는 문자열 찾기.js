function solution(myString, pat) {
    var answer = 0;
    const myStr = myString.toLowerCase();
    const lowpat = pat.toLowerCase();
    return myStr.includes(lowpat) ? 1 : 0;
}