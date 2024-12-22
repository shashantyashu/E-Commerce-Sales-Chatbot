let TextInput = document.getElementById("TextInput");
let chatbot = document.getElementById("chatbot");
let btn = document.getElementById("ButtonInput");


function GetUserResponce() {
    let userText = TextInput.value;
    TextInput.value = ""

    chatbot.innerHTML += `<p id="userText"><span>${userText}</span></p>`;

    fetch(`http://127.0.0.1:8000/getResponse?userMessage=${encodeURIComponent(userText)}`)
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json(); // Parse the JSON response
    })
    .then(data => {
        chatbot.innerHTML += `<p class="botText">ChatBot: <span>${data.response}</span></p>`;
        // Log the server's response
    })
    .catch(error => {
      console.error('There was an error:', error);
    });
}

btn.addEventListener("click", GetUserResponce)