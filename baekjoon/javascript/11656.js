const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", line => {
  input.push(line);
}).on("close", () => {
  let S = input[0];
  const result = [];
  for (let i = 0; i < S.length; i++) result.push(S.slice(i));
  result.sort();
  console.log(result.join("\n"));
});
