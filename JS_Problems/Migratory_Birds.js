function migratoryBirds(arr) {
  let maxOccurence = 0;
  let maxNumber = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] == arr[i + 1]) {
      maxOccurence += 1;
    } else {
      maxOccurence += 0;
    }
  }
}
