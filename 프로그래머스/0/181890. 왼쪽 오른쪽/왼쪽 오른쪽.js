function solution(str_list) {
    for (i=0; i <= str_list.length-1; i++){
        if (str_list[i] === "l") return str_list.slice(0, i);
        if (str_list[i] === "r") return str_list.slice(i+1);
    }
    return [];
}