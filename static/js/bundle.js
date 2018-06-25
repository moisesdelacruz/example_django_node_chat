(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}var p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(var u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){
// Profile Edit
const input_image = document.getElementById('id_photo');
const btn_change_image = document.getElementById('btn_change_image');
const current_photo = document.getElementById('current_photo');

if (btn_change_image && input_image) {
  btn_change_image.addEventListener('click', (event) => {
    event.preventDefault();
    input_image.accept = 'image/*';
    input_image.click();
  });

  input_image.addEventListener('change', (event) => {
    let file = event.target.files[0];
    current_photo.style.backgroundImage = `url(${window.URL.createObjectURL(file)})`;
  });
}

if (input_image && current_photo) {
  input_image.accept = 'image/*';
  input_image.addEventListener('change', (event) => {
    let file = event.target.files[0];
    current_photo.src = `${window.URL.createObjectURL(file)}`;
  });
}

},{}],2:[function(require,module,exports){
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

},{}],3:[function(require,module,exports){
document.addEventListener("DOMContentLoaded", (event) => { 
  require('./actions/events.js')
  require('./actions/change_photo.js')
  require('./comments/index.js')
});

},{"./actions/change_photo.js":1,"./actions/events.js":2,"./comments/index.js":4}],4:[function(require,module,exports){
const content_comments = document.getElementById('comments')
const input_comment = document.getElementById('comment')
const btn_send = document.getElementById('btn_send')

// connect to socket.io
const socket = io.connect('localhost:3000');
// events
socket.on('connect', () => {
  console.log("connect");
});

// send message
if (btn_send) {
  btn_send.addEventListener("click", send_message, false);
  input_comment.addEventListener('keypress', (event) => {
    //When enter is pressed send input value to node server
    if(event.keyCode === 13 && !event.shiftKey) {
      event.preventDefault()
      send_message(event);
    }
  });
}

// focus set
if (input_comment) {
  input_comment.focus();
}

socket.on('message', (message) => {
  //Escape HTML characters
  // var data = message.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");

  //Append message to the top of the list
  receive_message(message);
  // scroll top
  content_comments.scrollTop += -10000000000;

});

function send_message(event) {
  let exp = /.\S/i
  let msg = input_comment.value
  let publishing = input_comment.getAttribute('data-id');
  if(exp.test(msg)){
     socket.emit('send_message', {'text': msg, 'publishing': publishing}, (data) => {
          console.log(data);
     });
     //Clear input value
     input_comment.value = '';
  }
}

function receive_message(message) {
  let exp = {
    http: /(\b(https?|ftps?|git):\/\/[-A-Z0-9+&@#\/%?=~_|!:,.;]*[-A-Z0-9+&@#\/%=~_|])/ig,
    regx: /\B@[a-z0-9_-]+/gi,
    blank: /\r?\n/g,
  }

  text = message.text.replace(exp.regx, match => `<a href="/${match}">${match}</a>`)
                    .replace(exp.http, '<a href="$1" target="_blank">$1</a>')
                    .replace(exp.blank, '<br/>')

  content_comments.insertAdjacentHTML('afterbegin', `<article class="comment">
    <p class="username">
      <strong><a href="/@${message.user}">${message.user}</a></strong>
    </p>
    <p class="comment-text">
      ${text}
    </p>
    <p class="date comment-created">
      ${message.date}
    </p>
  </article>`);
}

},{}]},{},[3]);
