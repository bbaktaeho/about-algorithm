const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", line => {
  input.push(line);
}).on("close", () => {
  let [K, L] = input
    .shift()
    .split(" ")
    .map(x => +x);
  const waiting = new Map();
  for (let i in input) waiting.set(input[i], +i);
  result = Array.from(waiting.entries()).sort((a, b) => a[1] - b[1]);
  console.log(
    result
      .slice(0, K)
      .map(x => x[0])
      .join("\n"),
  );
});
