function compress(chars: string[]): number {
  let ctr = 1;
  for (let i = 0; i < chars.length; i++) {
    if (i + 1 === chars.length || chars[i] !== chars[i + 1]) {
      if (ctr !== 1) {
        chars.splice(i - ctr + 1, ctr, chars[i]);
        i = i - ctr + 2;
        let ctrStringArray = ctr.toString();
        for (let y = 0; y < ctrStringArray.length; y++) {
          chars.splice(i, 0, ctrStringArray[y]);
          i++;
        }
        i--;
        ctr = 1;
      }
    } else {
      ctr++;
    }
  }

  return chars.length;
}
