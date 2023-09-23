/*
 * Complete the 'countingValleys' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER steps
 *  2. STRING path
 */

function countingValleys(steps, path) {
  let totalPath = 0;
  let totalValley = 0;
  let valley = false;
  for (let i = 0; i < steps; i++) {
    if (path[i] === "U") {
      totalPath += 1;
    } else {
      totalPath -= 1;
    }
    if (path[i] === "U" && totalPath === 0) {
      if (valley) {
        totalValley += 1;
      }
      valley = false;
    } else if (path[i] === "D") {
      valley = true;
    }
  }
  return totalValley;
}
const steps = 12;
const path = "DDUUDDUDUUUD";
console.log(countingValleys(steps, path));
