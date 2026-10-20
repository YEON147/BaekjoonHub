function solution(bandage, health, attacks) {
    var ans = health;
    const [t, x, y] = bandage;
    const N = attacks.length;
    for (let i = 0; i < N; i++){
        const [time, hp] = [...attacks[i]];

        if (i >= 1){
            let gap = time-attacks[i-1][0] - 1
            const plus = gap*x;    
            const bonus = Math.floor(gap/t)*y;

            ans = Math.min(ans+plus+bonus, health);
        }
        ans -= hp;
        if (ans <= 0) return -1;
        
    }

    return ans > 0 ? ans : -1;
}