function showAlert(city) {
    alert("Loading weather report for " + city);
}

function acceptCookies() {
    document.getElementById("cookieBox").style.display = "none";
}
let currentUnit = "C";

document.getElementById("tempUnit").addEventListener("change", function () {
    let newUnit = this.value === "°C" ? "C" : "F";

    if (newUnit === currentUnit) return;

    let highs = document.querySelectorAll(".high");
    let lows = document.querySelectorAll(".low");

    highs.forEach(el => convertTemp(el, newUnit));
    lows.forEach(el => convertTemp(el, newUnit));

    currentUnit = newUnit;
});

function convertTemp(element, unit) {
    let temp = parseInt(element.innerText);

    if (unit === "F") {
        temp = Math.round(temp * 9 / 5 + 32);
    } else {
        temp = Math.round((temp - 32) * 5 / 9);
    }

    element.innerText = temp + "°";
}