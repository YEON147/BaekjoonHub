function solution(start_num, end_num) {
    let ans = [];
    while (start_num <= end_num) {
        ans.push(start_num);
        start_num += 1;
    }
    return ans;
}