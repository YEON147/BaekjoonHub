function solution(myString, pat) {
    const changed = myString
        .split("")
        .map(c => c === 'A' ? 'B' : 'A')
        .join('');
    return changed.includes(pat) ? 1 : 0;
}