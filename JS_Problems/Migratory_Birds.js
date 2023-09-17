/*
 * Complete the 'migratoryBirds' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

function migratoryBirds(arr) {
  for (let i = 0; i < arr.length; i++) {
    let count = new Array(6).fill(0);
    for (let bird of arr) {
      count[bird]++;
    }
    return count.indexOf(Math.max(...count));
  }
}
