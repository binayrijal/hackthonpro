console.log("loaded service page");

document.addEventListener("DOMContentLoaded", function () {
  const span = document.querySelector(".span");
  const span1 = document.querySelector(".span1");
  var currentDate = new Date();
  // change to hours
  var currentTime = currentDate.toLocaleTimeString();
  console.log(currentTime);
  //get the time in 24 hr format
  var currentHour = currentDate.getHours();
  span.innerText = "";
  span1.innerText = "";
  console.log(currentHour);
  if (currentHour > 16) {
    span.innerText = "closed";
    span.classList.add("closed");
    span1.innerText = "opens at 10 AM ";
    span1.style.color = "green";
  } else {
    span.innerText = "open";
    span.classList.add("open");
    span1.innerHTML = "close at 4am";
    span1.style.color = "red";
  }
});
