function solution(spell, dic) {
    const target = spell.sort().join("");

    for (const x of dic) {
        if (x.split("").sort().join("") === target) {
            return 1;
        }
    }

    return 2;
}