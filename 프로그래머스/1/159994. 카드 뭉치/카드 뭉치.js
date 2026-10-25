function solution(cards1, cards2, goal) {
    var answer = '';
    cards1.reverse()
    cards2.reverse()
    for (const ch of goal){
        if (ch === cards1.at(-1)) cards1.pop()
        else if (ch === cards2.at(-1)) cards2.pop()
        else return "No"
    }
    return "Yes";
}