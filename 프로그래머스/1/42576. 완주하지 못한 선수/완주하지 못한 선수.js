function solution(participant, completion) {
    const c = completion.sort();
    const p =participant.sort();
    for (let i=0; i < completion.length; i++) {
        if (c[i] !== p[i]) return p[i];
    }
    return p.at(-1);
}