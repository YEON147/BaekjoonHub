function solution(today, terms, privacies) {
    const dict = {};
    terms.forEach((v) => {
        const [t, m] = v.split(' ');
        dict[t] = Number(m);
    });

    // 날짜를 day로 변환 (모든 달이 28일)
    function toDays(str) {
        const [y, m, d] = str.split('.').map(Number);
        return y * 12 * 28 + m * 28 + d;
    }

    const todayDays = toDays(today);
    const answer = [];

    privacies.forEach((v, i) => {
        const [date, type] = v.split(' ');
        const expire = toDays(date) + dict[type] * 28; // 만료되는 날
        if (expire <= todayDays) answer.push(i + 1);
    });

    return answer;
}