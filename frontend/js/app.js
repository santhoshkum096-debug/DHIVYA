const form = document.getElementById("documentForm");
const editor = document.getElementById("documentContent");
const statusBox = document.getElementById("status");
const generateBtn = document.getElementById("generateBtn");

function showStatus(message) {
    statusBox.textContent = message;
    statusBox.style.display = "block";
}

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const payload = {
        document_type: document.getElementById("document_type").value,
        party_one: document.getElementById("party_one").value,
        party_two: document.getElementById("party_two").value,
        effective_date: document.getElementById("effective_date").value,
        jurisdiction: document.getElementById("jurisdiction").value,
        terms: document.getElementById("terms").value,
        additional_details: document.getElementById("additional_details").value
    };

    generateBtn.disabled = true;
    generateBtn.textContent = "Generating...";
    showStatus("Generating your legal document...");

    try {
        const response = await fetch("/api/generate", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(payload)
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Generation failed.");
        }

        editor.value = data.content;
        showStatus("Document generated successfully. You can edit the preview.");
    } catch (error) {
        showStatus("Error: " + error.message);
    } finally {
        generateBtn.disabled = false;
        generateBtn.textContent = "Generate Document";
    }
});

async function downloadFile(format) {
    const content = editor.value.trim();

    if (!content) {
        showStatus("Generate or enter a document before downloading.");
        return;
    }

    try {
        const response = await fetch("/api/export/" + format, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({content})
        });

        if (!response.ok) {
            throw new Error("Export failed.");
        }

        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = "LegalEase_Document." + format;
        document.body.appendChild(a);
        a.click();
        a.remove();
        window.URL.revokeObjectURL(url);

        showStatus(format.toUpperCase() + " downloaded successfully.");
    } catch (error) {
        showStatus("Error: " + error.message);
    }
}
