function counter(name) {
  const nameSet = new Set(name);
  const alphaCounter = {};

  for (let c of nameSet) {
    let pos = name.indexOf(c);
    let count = 0;
    while (pos !== -1) {
      count++;
      pos = name.indexOf(c, pos + 1);
    }
    alphaCounter[c] = count;
  }
  return alphaCounter;
}

// 해결
function solution() {
  const name = input[0];
  const nameLen = name.length;
  const nameCounter = counter(name);

  let odd = 0;
  let oddChar = "";
  for (let c of Object.entries(nameCounter))
    if (c[1] % 2 != 0) {
      odd++;
      oddChar = c[0];
    }

  if (odd >= 2) return "I'm Sorry Hansoo";
  let result = oddChar;
  let front = "";
  if (nameCounter[oddChar] == 1) delete nameCounter[oddChar];
  for (let c of Object.keys(nameCounter).sort()) front += c.repeat(nameCounter[c] / 2);
  return front + result + front.split("").reverse().join("");
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", line => {
  input.push(line);
}).on("close", () => {
  const result = solution();
  console.log(result);
});
