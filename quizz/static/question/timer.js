var count = 120;
var interval = setInterval(function () {
  document.getElementById("timer").innerHTML = count + " sec left";
  count--;
  if (count == -2) {
    clearInterval(interval);
    document.getElementById("button").form.submit();
    alert("You're out of time!");
  }
}, 1000);
