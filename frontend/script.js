const chatBox = document.getElementById("chat-box");
const input = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");
const suggestionBtns = document.querySelectorAll(".suggestion");

const API_URL = "/chat"; // Flask backend

function addMessage(text, sender) {
    const msg = document.createElement("div");
    msg.classList.add("message");
    msg.classList.add(sender === "user" ? "user-message" : "bot-message");
    msg.textContent = text;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
    const text = input.value.trim();
    if (!text) return;

    addMessage(text, "user");
    input.value = "";

    addMessage("Thinking...", "bot");

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question: text })
        });

        const data = await response.json();

        // remove "Thinking..."
        if (chatBox.lastChild) {
            chatBox.lastChild.remove();
        }

        addMessage(data.answer, "bot");

    } catch (err) {
        chatBox.lastChild.remove();
        addMessage("Error connecting to server.", "bot");
    }
}

sendBtn.addEventListener("click", sendMessage);

input.addEventListener("keypress", (e) => {
    if (e.key === "Enter") sendMessage();
});

suggestionBtns.forEach(btn => {
    btn.addEventListener("click", () => {
        input.value = btn.textContent;
        sendMessage();
    });
});