function solution(friends, gifts) {
  const n = friends.length;
  const idx = new Map(friends.map((f, i) => [f, i]));
  const giftCount = Array.from(
      { length: n }, () => Array(n).fill(0)); // r: 준 사람 | c: 받은 사람
  const score = Array(n).fill(0); // 선물지수
  const count = Array(n).fill(0); // 다음 달 받을 선물 수

  for (const gift of gifts) {
    const [from, to] = gift.split(' ').map((name) => idx.get(name));
    giftCount[from][to]++;
    score[from]++;
    score[to]--;
  }

  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      // 주고받은 수가 같으면(0 포함) 선물지수로 비교
      const diff = (giftCount[i][j] - giftCount[j][i]) || (score[i] - score[j]);
      if (diff > 0) count[i]++;
      else if (diff < 0) count[j]++;
    }
  }

  return Math.max(...count);
}