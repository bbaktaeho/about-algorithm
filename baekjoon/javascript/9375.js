const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", line => {
  input.push(line);
}).on("close", () => {
  let testCount = input.shift();
  while (testCount--) {
    let count = input.shift();
    const cloth = {};
    for (let i = 0; i < count; i++) {
      const [_, key] = input.shift().split(" ");
      if (cloth[key]) cloth[key]++;
      else cloth[key] = 1;
    }
    let result = 1;
    for (const i of Object.values(cloth)) result *= i + 1;
    console.log(result - 1);
  }
});
