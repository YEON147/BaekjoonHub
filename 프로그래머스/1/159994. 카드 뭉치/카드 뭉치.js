function solution(cards1, cards2, goal) {
    let [i, j] = [0, 0];
    for (const ch of goal){
        if (cards1[i] === ch) i++;
        else if (cards2[j] === ch) j++;
        else return "No"
    }
    return "Yes";
}