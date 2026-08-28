function solution(num_list) {
    var answer = 0;
    return num_list.length >= 11 ? 
        num_list.reduce((sum, a) => sum+a):
        num_list.reduce((sum, a) => sum*a);
}