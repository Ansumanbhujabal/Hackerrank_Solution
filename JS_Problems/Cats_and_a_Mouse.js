// Complete the catAndMouse function below.
function catAndMouse(x, y, z) {
  if (Math.abs(z - x) === Math.abs(z - y)) {
    return "Mouse C";
  } else if (Math.abs(z - x) > Math.abs(z - y)) {
    return "Cat B";
  } else {
    return "Cat A";
  }
}
