/*
 * Complete the 'bonAppetit' function below.
 *
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY bill
 *  2. INTEGER k
 *  3. INTEGER b
 */

function bonAppetit(bill, k, b) {
  let actualCost = 0;
  let totalCost = 0;
  for (let i = 0; i < bill.length; i++) {
    if (i === k) {
      totalCost += 0;
    } else {
      totalCost += bill[i];
      actualCost = b - totalCost / 2;
    }
  }
  if (totalCost / 2 == b) {
    console.log("Bon Appetit");
  } else {
    console.log(actualCost);
  }
}
bonAppetit([3, 10, 2, 9], 1, 12);
