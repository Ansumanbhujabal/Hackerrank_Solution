/*
 * Complete the getMoneySpent function below.
 */
function getMoneySpent(keyboards, drives, b) {
  let maxBudget = -1;

  for (let i = 0; i < keyboards.length; i++) {
    for (let j = 0; j < drives.length; j++) {
      if (
        keyboards[i] + drives[j] <= b &&
        keyboards[i] + drives[j] > maxBudget
      ) {
        maxBudget = keyboards[i] + drives[j];
      }
    }
  }
  return maxBudget;
}
console.log(getMoneySpent([10, 2, 3], [5, 2, 8], 31));
