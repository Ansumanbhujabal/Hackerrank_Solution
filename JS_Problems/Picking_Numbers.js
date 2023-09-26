/*
 * Complete the 'pickingNumbers' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY a as parameter.
 */

function pickingNumbers(a) {
  let maxCount = 0;
  for (const num of a) {
    let x = a.filter((i) => i == num).length;
    let y = a.filter((i) => i == num + 1).length;
    x = x + y;
    if (x > maxCount) {
      maxCount = x;
    }
  }
  return maxCount;
}
const inputArray = [4, 5, 5, 6, 6, 6, 7];
const result = pickingNumbers(inputArray);
console.log(result);
