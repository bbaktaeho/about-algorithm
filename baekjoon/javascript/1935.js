const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", line => {
  input.push(line);
}).on("close", () => {
  const N = +input[0];
  const postfix = input[1];
  const postfixMap = new Map();

  for (let i = 2; i < input.length; i++) {
    const num = input[i];
    postfixMap.set(String.fromCharCode(63 + i), num);
  }

  const calc = [];
  for (let c of postfix) {
    if (postfixMap.has(c)) calc.push(+postfixMap.get(c));
    else
      switch (c) {
        case "*": {
          calc.push(calc.pop() * calc.pop());
          break;
        }
        case "/": {
          const back = calc.pop();
          calc.push(calc.pop() / back);
          break;
        }
        case "+": {
          calc.push(calc.pop() + calc.pop());
          break;
        }
        case "-": {
          const back = calc.pop();
          calc.push(calc.pop() - back);
          break;
        }
        default:
          break;
      }
  }
  console.log(calc[0].toFixed(2));
});
