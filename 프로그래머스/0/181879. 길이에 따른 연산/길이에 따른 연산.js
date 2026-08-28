function solution(num_list) {
    return num_list.reduce((sum, a)=> num_list.length >= 11 ? sum+a : sum*a)
}