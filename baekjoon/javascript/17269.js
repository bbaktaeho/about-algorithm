const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", line => {
  input.push(line);
}).on("close", () => {
  const alpha = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1];
  let [aLen, bLen] = input[0].split(" ");
  let minLen = Math.min(aLen, bLen);

  let [A, B] = input[1].split(" ");
  let totalName = "";
  for (let i = 0; i < minLen; i++) totalName += A[i] + B[i];
  totalName += A.slice(minLen) + B.slice(minLen);

  let init = totalName.split("").map(c => alpha[c.charCodeAt() - 65]);
  while (init.length > 2) {
    let temp = [];
    for (let i = 0; i < init.length - 1; i++) temp.push((init[i] + init[i + 1]) % 10);
    init = temp;
  }
  console.log(+init.join("") + "%");
});
