function detectSarcasm() {
    let userInput = document.getElementById("userInput").value;
    
    if (!userInput.trim()) {
        alert("Please enter a text!");
        return;
    }

    fetch("/detect", {
        method: "POST",
        body: new URLSearchParams({ text: userInput }),
        headers: { "Content-Type": "application/x-www-form-urlencoded" }
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById("sarcasmResult").innerText = "Error: " + data.error;
        } else {
            document.getElementById("sarcasmResult").innerHTML = data.highlighted_text;
        }
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("sarcasmResult").innerText = "Failed to get response!";
    });
}
