const solution = (a, b) => {
  let sum = 0;
  for (const i in a) sum += a[i] * b[i];
  return sum;
};
// 테스트 1 〉	통과 (0.46ms, 30.4MB)
// 테스트 2 〉	통과 (0.08ms, 30MB)
// 테스트 3 〉	통과 (0.08ms, 30MB)
// 테스트 4 〉	통과 (0.08ms, 30.1MB)
// 테스트 5 〉	통과 (0.07ms, 30.1MB)
// 테스트 6 〉	통과 (0.36ms, 30.3MB)
// 테스트 7 〉	통과 (0.39ms, 30.4MB)
// 테스트 8 〉	통과 (0.44ms, 30.4MB)
// 테스트 9 〉	통과 (0.32ms, 30.3MB)

const solution = (a, b) => a.reduce((acc, v, i) => acc + v * b[i], 0);
// 테스트 1 〉	통과 (0.10ms, 30.1MB)
// 테스트 2 〉	통과 (0.05ms, 30MB)
// 테스트 3 〉	통과 (0.07ms, 30.1MB)
// 테스트 4 〉	통과 (0.07ms, 30.2MB)
// 테스트 5 〉	통과 (0.06ms, 30.1MB)
// 테스트 6 〉	통과 (0.11ms, 30MB)
// 테스트 7 〉	통과 (0.12ms, 30MB)
// 테스트 8 〉	통과 (0.08ms, 30.1MB)
// 테스트 9 〉	통과 (0.14ms, 30.1MB)
