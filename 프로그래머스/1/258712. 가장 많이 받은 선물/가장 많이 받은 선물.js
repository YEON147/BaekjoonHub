function solution(friends, gifts) {
    let ans = 0;
    const count = new Map();
    //최다선물 수신자의 선물수 return
    const n = friends.length;
    // r: 준사람 | c: 받은사람 
    const giftCount = Array.from(
        { length: n },
        () => Array(n).fill(0)
    );
    // 선물지수 저장
    const score = new Map();
    for (const gift of gifts){
        const [from, to] = gift.split(' ');
        // 2차원 배열 저장
        const from_idx = friends.indexOf(from);
        const to_idx = friends.indexOf(to);
        giftCount[from_idx][to_idx] += 1;
         // 선물지수 계산
        score.set(from_idx, (score.get(from_idx)||0) + 1);
        score.set(to_idx, (score.get(to_idx)||0) - 1);
    }
    for (let i=0; i < n; i ++){
        for (let j=i+1; j < n; j++){
            if (giftCount[i][j] > giftCount[j][i]){
                count.set(i, (count.get(i)||0) + 1)
            } else if (giftCount[i][j] < giftCount[j][i]) {
                count.set(j, (count.get(j) || 0) + 1);
                };
            // 주고받은 기록이 하나도 없거나 수가 같을 때
            if (giftCount[i][j] === giftCount[j][i]) {
                // 선물 지수가 더 큰사람 +1
                const scoreI = score.get(i) || 0;
                const scoreJ = score.get(j) || 0;

                if (scoreI > scoreJ) {
                    count.set(i, (count.get(i) || 0) + 1);
                } else if (scoreJ > scoreI) {
                    count.set(j, (count.get(j) || 0) + 1);
                };
            };
        };
    };
    console.log(count);
    
    // const ans = Math.max(...list.values())
    return Math.max(0, ...count.values());;
};