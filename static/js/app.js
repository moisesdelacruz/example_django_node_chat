$(function() {
  // Menu
  $('#btn-menu').on('click', (e) => {
    e.stopPropagation();
    $('#menu').slideToggle();
  });

  // Profile Edit
  const input_image = document.getElementById('id_photo');
  const btn_change_image = document.getElementById('btn_change_image');
  const current_photo = document.getElementById('current_photo');

  if (btn_change_image && input_image) {
    btn_change_image.addEventListener('click', (event) => {
      event.preventDefault()
      input_image.accept = 'image/*'
      input_image.click()
    })

    input_image.addEventListener('change', (event) => {
      let file = event.target.files[0]
      current_photo.style.backgroundImage = `url(${window.URL.createObjectURL(file)})`
    })
  }

  if (input_image && current_photo) {
    input_image.addEventListener('change', (event) => {
      let file = event.target.files[0]
      current_photo.src = `${window.URL.createObjectURL(file)}`
    })
  }
});
