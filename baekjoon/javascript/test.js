// const arr = [6, 4, 9, 4, 2, 1, 20, 15, 22, 10];
// arr.sort((a, b) => {
//   console.log("뒤:", a, "앞:", b);
//   if (a < b) return -1; // 뒤를 앞으로 가져옴
//   else if (a == b) return 0; // 그대로 유지
//   else return 1; // 뒤가 더 클 때 뒤쪽이 뒤로 오게
// });

// console.log(arr);

var items = [
  { name: "Edward", value: 21 },
  { name: "Sharpe", value: 37 },
  { name: "And", value: 45 },
  { name: "The", value: -12 },
  { name: "Magnetic", value: 13 },
  { name: "Zeros", value: 37 },
];

// value 기준으로 정렬
items.sort(function (a, b) {
  if (a.value > b.value) {
    return 1;
  }
  if (a.value < b.value) {
    return -1;
  }
  // a must be equal to b
  return 0;
});

console.log(items);

// name 기준으로 정렬
items.sort(function (a, b) {
  var nameA = a.name.toUpperCase(); // ignore upper and lowercase
  var nameB = b.name.toUpperCase(); // ignore upper and lowercase
  if (nameA < nameB) {
    return -1;
  }
  if (nameA > nameB) {
    return 1;
  }

  // 이름이 같을 경우
  return 0;
});

console.log(items);
