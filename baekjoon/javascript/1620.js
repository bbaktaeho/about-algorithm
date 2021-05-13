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
  const nameList = [];
  const nameMap = new Map();
  for (let i = 1; i <= N; i++) {
    nameList.push(input[i]);
    nameMap.set(input[i], i);
  }
  const result = [];
  for (let i = +N + 1; i < input.length; i++) {
    if (!isNaN(input[i])) result.push(nameList[+input[i] - 1]);
    else result.push(nameMap.get(input[i]));
  }
  console.log(result.join("\n"));
});
