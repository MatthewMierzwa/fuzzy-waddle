function canPlaceFlowers(flowerbed: number[], n: number): boolean {
  let planted = 0;
  for (let i = 0; i < flowerbed.length; i++) {
    if (flowerbed[i] !== 0) {
      continue;
    }

    let w = i - 1;
    if (w >= 0 && flowerbed[w] !== 0) {
      continue;
    }

    let e = i + 1;
    if (e < flowerbed.length && flowerbed[e] !== 0) {
      continue;
    }

    flowerbed[i] = 1;
    planted++;
  }

  if (planted >= n) {
    return true;
  }
  return false;
}
