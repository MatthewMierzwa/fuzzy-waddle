function kidsWithCandies(candies: number[], extraCandies: number): boolean[] {
  let ret = [];
  let max = 0;

  for (let c of candies) {
    if (c > max) {
      max = c;
    }
  }

  for (let c of candies) {
    if (c + extraCandies >= max) {
      ret.push(true);
    } else {
      ret.push(false);
    }
  }

  return ret;
}
