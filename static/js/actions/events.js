const btn_menu = document.getElementById('btn-menu');
const menu = document.getElementById('menu');
const btn_dropdown = document.getElementById('btn-dropdown');
const dropdown = document.getElementById("dropdown");

// events
btn_menu.addEventListener('click', menuToggle);
btn_dropdown.addEventListener('click', userDropDown);

// methods
function menuToggle (event) {
  if (!menu.classList.contains('show')) {
    event.currentTarget.classList.toggle("change");
    menu.classList.toggle('show');
    return;
  }
  event.currentTarget.classList.remove("change");
  menu.classList.remove('show');
}

function userDropDown (event) {
  dropdown.classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = (event) => {
  if (!event.target.matches('.dropbtn') && !event.target.matches('.dropbtn span')) {

    var dropdowns = document.getElementsByClassName("user-drowdown");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}
