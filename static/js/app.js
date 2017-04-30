$(function() {
  // Menu
  $('#btn-menu').on('click', (e) => {
    e.stopPropagation();
    $('#menu').slideToggle();
  });
});
