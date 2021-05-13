const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", line => {
  input.push(line);
}).on("close", () => {
  let [aLen, bLen] = input[0].split(" ").map(e => +e);
  const A = new Set(input[1].split(" "));
  const B = new Set(input[2].split(" "));
  let ab = 0;
  let ba = 0;
  for (let b of B) if (A.has(b)) ab++;
  for (let a of A) if (B.has(a)) ba++;

  console.log(aLen - ab + bLen - ba);
});
