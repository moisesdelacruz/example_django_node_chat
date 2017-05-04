const content_comments = document.getElementById('comments')
const input_comment = document.getElementById('comment')
const btn_send = document.getElementById('btn_send')

// connect to socket.io
const socket = io.connect('http://173.214.160.232:4000/');
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
