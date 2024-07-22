function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() === '') return;

    const chatLog = document.getElementById('chatlog');
    const userMessageDiv = document.createElement('div');
    userMessageDiv.textContent = 'You: ' + userInput;
    chatLog.appendChild(userMessageDiv);

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        const botMessageDiv = document.createElement('div');
        botMessageDiv.textContent = 'Bot: ' + data.response;
        chatLog.appendChild(botMessageDiv);
    });

    document.getElementById('user-input').value = '';
}

