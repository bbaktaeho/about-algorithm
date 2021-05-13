const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", line => {
  input.push(line);
}).on("close", () => {
  const compare = (a, b) => a - b;
  const m = input[0].split(" ")[1];
  const cardArr = input[1]
    .split(" ")
    .map(x => +x)
    .sort(compare);
  for (let i = 0; i < m; i++) {
    let total = cardArr[0] + cardArr[1];
    cardArr[0] = total;
    cardArr[1] = total;
    cardArr.sort(compare);
  }
  console.log(cardArr.reduce((acc, x) => acc + x));
});
// 아니 시바스크립트는 왜 자료구조 컬렉션을 지원안할까
