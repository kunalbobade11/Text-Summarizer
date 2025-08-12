// Handle summarize click
async function summarize() {
    const inputBox = document.getElementById('inputText');
    const outputBox = document.getElementById('summaryOutput');

    const text = inputBox.value.trim();

    if (!text) {
        alert("Please enter some text to summarize.");
        return;
    }

    // Show loading
    outputBox.innerHTML = "<span class='loading'>Summarizing...</span>";

    try {
        const res = await fetch('/summarize', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text })
        });

        const data = await res.json();

        if (data.summary) {
            outputBox.textContent = data.summary;
        } else {
            outputBox.textContent = data.error || "Something went wrong.";
        }
    } catch (error) {
        outputBox.textContent = "Error: " + error.message;
    }
}

// Handle clear button
function clearFields() {
    document.getElementById('inputText').value = '';
    document.getElementById('summaryOutput').innerHTML = '';
}
