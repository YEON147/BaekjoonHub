function solution(str_list) {
    var answer = [];
    const [l, r] = ["l", "r"].map(x => {
    const index = str_list.indexOf(x);
    return index === -1 ? 100 : index;
    });
    return l < r 
        ? str_list.slice(0, l)
        : str_list.slice(r+1);
}