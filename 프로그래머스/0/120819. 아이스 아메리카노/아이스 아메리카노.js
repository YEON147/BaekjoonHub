function solution(money) {
    var count = 0;
    while (money >= 5500){
        count += 1;
        money -= 5500;
    };
    return [count, money];
}