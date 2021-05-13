const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", line => {
  input.push(line);
}).on("close", () => {
  const [N, M] = input[0].split(" ");
  const A = new Set(input[1].split(" "));
  const B = new Set(input[2].split(" "));
  for (let b of B) if (A.has(b)) A.delete(b);
  const result = Array.from(A.values()).sort((a, b) => a - b);
  console.log(result.length);
  console.log(...result);
  process.exit();
});
