export const compute = (a, b) => {
  let c = 0;
  if (a === b) {
    return c;
  } else if (a.length !== b.length) {
    if (a.length == 0) {
      throw new Error("left strand must not be empty");
    } else if (b.length == 0) {
      throw new Error("right strand must not be empty");
    } else {
      throw new Error("left and right strands must be of equal length");
    }
  } else {
    return a.split("").filter((item, index) => item != b.charAt(index)).length;
  }
};