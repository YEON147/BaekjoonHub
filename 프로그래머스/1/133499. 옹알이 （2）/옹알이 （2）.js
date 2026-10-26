function solution(babbling) {
    const sounds = ["aya", "ye", "woo", "ma"];
    let answer = 0;
    for (let word of babbling) {
        let repeat = false;
        for (const s of sounds) {
            if (word.includes(s+s)) repeat = true;
        }
        if (repeat) continue;
        
        for (const s of sounds) {
            word = word.replaceAll(s, ' ');
        }
        if (word.trim() === '') answer ++;
    }
    return answer;
}