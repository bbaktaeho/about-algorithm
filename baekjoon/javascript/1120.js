const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", line => {
  input.push(line);
}).on("close", () => {
  const [A, B] = input[0].split(" ");
  const aLen = A.length;
  const subLen = B.length - aLen;

  let diff = aLen;
  for (let i = 0; i < subLen + 1; i++) {
    let tempDiff = 0;
    for (let j = 0; j < aLen; j++) if (A[j] !== B[i + j]) tempDiff++;
    diff = Math.min(diff, tempDiff);
  }
  console.log(diff);
});
