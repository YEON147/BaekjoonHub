function solution(s) {
    const exist = [];
    return [...s].map(ch => {
        const idx = exist.indexOf(ch)
        exist.unshift(ch)
        return idx > -1 ? idx + 1 : -1
    });

}