function sequentialSizes(val:number) {
    let answer = "";
    // Only change code below this line
    switch(answer){
      case "1":
      case "2":
      case "3":
          return "Low";
          break;
      case "4":
      case "5":
      case "6":
          answer = "Mid";
          break;
      case "7":
      case "8":
      case "9":
          answer = "High";
          break;
    }
    // Only change code above this line
    return answer;
  }
  
  sequentialSizes(3);