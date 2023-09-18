function dayOfProgrammer(year) {
  let leapyearArray = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  let nonleapyearArray = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

  let month = 0;
  let day = "";
  if (year >= 1700 && year < 1917) {
    let totalDays = 0;
    let targetDay = 0;
    if (year % 4 === 0) {
      for (let i = 0; i < 12; i++) {
        if (totalDays + leapyearArray[i] > 256) {
          month = i + 1;
          targetDay = 256 - totalDays;
          break;
        }
        totalDays += leapyearArray[i];
      }
      if (month >= 10) {
        day = targetDay + "." + month + "." + year;
      } else {
        day = targetDay + ".0" + month + "." + year;
      }
    } else {
      for (let i = 0; i < 12; i++) {
        if (totalDays + nonleapyearArray[i] > 256) {
          month = i + 1;
          targetDay = 256 - totalDays;
          break;
        }
        totalDays += nonleapyearArray[i];
      }
      if (month >= 10) {
        day = targetDay + "." + month + "." + year;
      } else {
        day = targetDay + ".0" + month + "." + year;
      }
    }
  } else if (year === 1918) {
    day = 26;
    month = 2;
    day = targetDay + ".0" + month + "." + year;
  } else {
    let totalDays = 0;
    let targetDay = 0;
    if (year % 400 === 0 || (year % 4 === 0 && year % 100 != 0)) {
      for (let i = 0; i < 12; i++) {
        if (totalDays + leapyearArray[i] > 256) {
          month = i + 1;
          targetDay = 256 - totalDays;
          break;
        }
        totalDays += leapyearArray[i];
      }
      if (month >= 10) {
        day = targetDay + "." + month + "." + year;
      } else {
        day = targetDay + ".0" + month + "." + year;
      }
    } else {
      for (let i = 0; i < 12; i++) {
        if (totalDays + nonleapyearArray[i] > 256) {
          month = i + 1;
          targetDay = 256 - totalDays;
          break;
        }
        totalDays += nonleapyearArray[i];
      }
      if (month >= 10) {
        day = targetDay + "." + month + "." + year;
      } else {
        day = targetDay + ".0" + month + "." + year;
      }
    }
  }
  return day;
}

console.log(dayOfProgrammer(2017));
