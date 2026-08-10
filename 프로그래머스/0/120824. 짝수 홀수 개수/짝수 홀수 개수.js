function solution(num_list) {
    let ans = [0, 0]
    ans[0] = num_list.filter(v => v %2 ===0).length;
    ans[1] = num_list.filter(v => v %2 !==0).length;
    return ans;
}