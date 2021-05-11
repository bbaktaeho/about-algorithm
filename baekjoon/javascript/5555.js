const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
let count = 0;
rl.on("line", line => {
  input.push(line);
}).on("close", () => {
  const search = input[0];
  for (let i = 2; i < input.length; i++) {
    const origin = input[i].repeat(2);
    if (origin.indexOf(search) >= 0) count++;
    // if (origin !== origin.replace(search, "")) count++;
  }
  console.log(count);
});
