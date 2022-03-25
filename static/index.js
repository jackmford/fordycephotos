function changeTab(film_type) {
  var tabs = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabs.length; i++) {
    tabs[i].style.display = "none";
  }

  document.getElementById(film_type).style.display = "block";
}
