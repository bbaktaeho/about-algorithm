const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", line => {
  input.push(line);
}).on("close", () => {
  input.shift();

  const Q = [];
  const result = [];
  for (let data of input) {
    let command = data.split(" ");
    if (command[0] == "push") Q.push(command[1]);
    else if (command[0] == "pop") result.push(Q.length ? Q.shift() : -1);
    else if (command[0] == "size") result.push(Q.length);
    else if (command[0] == "empty") result.push(Q.length ? 0 : 1);
    else if (command[0] == "front") result.push(Q.length ? Q[0] : -1);
    else if (command[0] == "back") result.push(Q.length ? Q[Q.length - 1] : -1);
    console.log(Q);
  }
  console.log(result.join("\n"));
});
