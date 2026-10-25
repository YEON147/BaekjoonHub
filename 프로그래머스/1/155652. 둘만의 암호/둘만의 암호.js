function solution(s, skip, index) {
    const abc = [...'abcdefghijklmnopqrstuvwxyz']
                    .filter(s => !skip.includes(s));
    return [...s].map(c => abc[(abc.indexOf(c)+index)%abc.length]).join('');
}