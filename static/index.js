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

document.getElementById('iphone').style.display = "none";
