console.clear();
var arrRes = [];
var arrId = 0;
var tickCount = 0;
var nextMonth = document.querySelector(".e1okul3h1");



var timer = setInterval(tick, 3000)

function tick()
{
  console.log(document.querySelector(".css-5egot").innerHTML);
  counter = 0;
  nextMonth.click();

  var buttons = document.querySelectorAll(".ef9wlog0");

  for (let i = 0; i < buttons.length; i++)
    buttons[i].click();

  var records = document.querySelectorAll(".css-1a8b0li");

  //setTimeout(() => {
  for (let i = 0; i < records.length; i++)
    if (!records[i].innerHTML.includes("birthday")) {
      console.log(records[i].innerHTML);
      counter++;
    }
  //}, 1000);
  console.log(counter);
  if (tickCount == 3)
    clearInterval(timer);
  tickCount++;
}