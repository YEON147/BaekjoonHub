function solution(s) {
  let answer = 0;
  let count = 0;
  let cur = '';

  for (const ch of s) {
    if (count === 0) {  
      cur = ch;
      answer++;
    }
    // 같은문자면 +1 다른 문자면 -1 | count가 0이 될 때 same==diff
    count += ch === cur ? 1 : -1;
  }

  return answer;
}