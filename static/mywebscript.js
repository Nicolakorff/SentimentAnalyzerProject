let RunSentimentAnalysis = () => {
    const textToAnalyze = document.getElementById("textToAnalyze").value;
    const encodedText = encodeURIComponent(textToAnalyze);

    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 4) {
            const output = document.getElementById("system_response");
            if (this.status === 200) {
                output.innerHTML = this.responseText;
            } else {
                output.innerHTML = "❌ Error en la solicitud.";
            }
        }
    };

    xhttp.open("GET", `/emotionDetector?textToAnalyze=${encodedText}`, true);
    xhttp.send();
};

