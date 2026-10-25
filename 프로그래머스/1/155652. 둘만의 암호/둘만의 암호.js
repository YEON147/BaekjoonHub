function solution(s, skip, index) {
    const alphabet = [...'abcdefghijklmnopqrstuvwxyz']
    const abc = alphabet.filter(s => !skip.includes(s));
    const str = [...s]
    return str.map(c => abc[(abc.indexOf(c)+index)%abc.length]).join('');
}