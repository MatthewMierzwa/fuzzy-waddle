function reverseWords(s: string): string {
  let l = [];
  let found = false;
  let subStr = "";
  const reg = /[a-zA-Z0-9]/g;
  let endLength = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i].match(reg)) {
      found = true;
      subStr += s[i];
      if (i + 1 === s.length) {
        l.push(subStr);
        endLength++;
      }
    } else if (s[i] === " " && found === true) {
      found = false;
      l.push(subStr);
      endLength++;
      subStr = "";
    }
  }

  let ret = "";
  for (let i = 0; i < endLength; i++) {
    if (i === endLength - 1) {
      ret += l.pop();
    } else {
      ret = ret + l.pop() + " ";
    }
  }

  return ret;
}
