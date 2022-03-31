function changeTab(film_type, btn_name) {
  var tabs = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabs.length; i++) {
    tabs[i].style.display = "none";
  }

  document.getElementById(film_type).style.display = "block";

  var selected = document.getElementsByClassName("active");
  if (selected.length > 0) {
    selected[0].className = "";
  }
  document.getElementById(btn_name).className = "active";
}

document.getElementById('film_button').className = "active";
document.getElementById('iphone').style.display = "none";

window.onbeforeunload = function () {
  window.scrollTo(0, 0);
}

const loader = document.querySelector(".loader");
window.onload = function(){
  setTimeout(function(){
      loader.style.opacity = "0";
      setTimeout(function(){
          loader.style.display = "none";
          }, 500);
      },1500);
}
