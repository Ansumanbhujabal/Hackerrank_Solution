/*
 * Complete the 'pageCount' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER p
 */

function pageCount(n, p) {
  const front = Math.floor(p / 2);
  let back;
  if (n % 2 === 1) {
    back = Math.floor((n - p) / 2);
  } else {
    back = Math.floor((n - p + 1) / 2);
  }
  return Math.min(front, back);
}
