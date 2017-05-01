(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
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
});

},{}]},{},[1]);
