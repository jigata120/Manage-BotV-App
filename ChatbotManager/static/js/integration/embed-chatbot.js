(function () {
    const script = document.currentScript;
    const chatbotDomain = script.getAttribute("data-domain") || "http://127.0.0.1:8080";
    const apiKey = script.getAttribute("data-api-key");
//    const botId = script.getAttribute("data-bot-id"); // Optional if bot_id needed for more granularity

    const chatbotContainer = document.querySelector(".chatbot-window");
    if (!chatbotContainer) {
        console.error("Error: No element with class 'chatbot-window' found.");
        return;
    }

    if (!apiKey) {
        chatbotContainer.textContent = "Error: API key is required.";
        return;
    }

    // Create an iframe
    const iframe = document.createElement("iframe");
    iframe.src = `${chatbotDomain}/chatbot-preview/?api_key=${apiKey}`;
    iframe.style.width = "100%";
    iframe.style.height = "100%";
    iframe.style.border = "none";
    chatbotContainer.appendChild(iframe);
})();
