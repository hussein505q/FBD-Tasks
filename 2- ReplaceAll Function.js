function replaceAll(str, unwanted, wanted) {
    //1. splited str into substrings without the unwanted string
    //2. rejoin the splited string str into one with the wanted string
    return str.split(unwanted).join(wanted);
}
var str = "a replaceAll function: the string.prototype.replace only replaces one occurance, make a version that replaces all.";
console.log(replaceAll(str, "replace", "change"));
//3. Expected output: "a changeAll function: the string.prototype.change only changes one occurance, make a version that changes all."