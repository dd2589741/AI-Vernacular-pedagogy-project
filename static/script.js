async function translateLesson() {

    const tamilText = document
        .getElementById("tamilInput")
        .value
        .trim();

    const output = document.getElementById("translationOutput");

    if (!tamilText) {

        output.innerText = "Please enter a lesson!";

        return;

    }

    output.innerText = "Translating...";

    try {

        const response = await fetch("/translate", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                text: tamilText
            })

        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Translation failed");
        }

        output.innerText = data.translation;

    }

    catch (error) {

        output.innerText = "Translation failed.";

        console.error(error);

    }

}


function speakLesson() {

    const text = document.getElementById("translationOutput").innerText;

    if (!text || text === "Your lesson will appear here!") {

        alert("Translate the lesson first!");

        return;

    }

    const speech = new SpeechSynthesisUtterance(text);

    speech.lang = "ta-IN";

    speech.rate = 0.85;

    window.speechSynthesis.cancel();

    window.speechSynthesis.speak(speech);

}