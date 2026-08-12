function solution(array) {
    const count = array.reduce((a, v) => (a[v] = (a[v] || 0) + 1, a), {});
    const max = Math.max(...Object.values(count));
    const modes = Object.keys(count).filter(k => count[k] === max);
    return modes.length > 1 ? -1 : +modes[0];
}