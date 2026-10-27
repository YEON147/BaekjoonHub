function solution(food) {
    let ans = [];
    food.slice(1).forEach((v, i) => {
        cnt = Math.floor(v/2);
        console.log(i+1, v, cnt)
        ans += String(i+1).repeat(cnt);
    })
    return ans+'0'+ans.split('').reverse().join('');
}