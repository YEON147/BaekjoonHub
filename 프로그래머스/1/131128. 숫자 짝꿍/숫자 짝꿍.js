function solution(X, Y) {
    const sx = [...X].sort((a, b) => b - a);
    const sy = [...Y].sort((a, b) => b - a);
    const ans = [];
    let i = 0, j = 0;

    while (i < sx.length && j < sy.length) {
        if (sx[i] === sy[j]) {       
            ans.push(sx[i]);
            i++;
            j++;
        } else if (sx[i] > sy[j]) { 
            i++;
        } else {                 
            j++;
        }
    }

    if (ans.length === 0) return "-1"; 
    if (ans[0] === '0') return "0";    
    return ans.join('');
}