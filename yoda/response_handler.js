// Declaring variables that you may want to use.
let names = ['cute', 'regular'];
let moods = ['dark', 'force', 'std'];

let dark_quotes = ["Once you start down the dark path, forever will it dominate your destiny, consume you it will.",
"In a dark place we find ourselves, and a little more knowledge lights our way.",
"Fear is the path to the dark side. Fear leads to anger. Anger leads to hate. Hate leads to suffering.",
"Always two there are, no more, no less. A master and an apprentice.",
"In the end, cowards are those who follow the dark side."];
let force_quotes = ["Luminous beings are we, not this crude matter.",
"A Jedi uses the Force for knowledge and defense, never for attack.",
"Clear your mind must be, if you are to find the villains behind this plot.",
"The force. Life creates it, makes it grow. Its energy surrounds us and binds us.",
"My ally is the Force, and a powerful ally it is."];
let std_quotes = ["Patience you must have, my young padawan.",
"When nine hundred years old you reach, look as good you will not.",
"No! Try not! Do or do not, there is no try.",
"Judge me by my size, do you?",
"Difficult to see. Always in motion is the future."
];

document.addEventListener('DOMContentLoaded', function () {
    var input = document.getElementById("input");
    var button = document.getElementById("submit");
    input.addEventListener("keyup", function (event) {
        if (event.key !== "Enter") {
            return;
        }
        button.click();
        event.preventDefault();
    });
});

function respond() {
    var text = document.getElementById("input").value;
    document.getElementById("input").value = "";

    let name;
    if (text.includes("cute") || text.includes("baby")) {
        name = names[0];
    } else {
        name = names[1];
    }
    
    let mood, quotes;
    if (text.includes("force")) {
        if (text.includes("dark")) {
            mood = moods[0];
            quotes = dark_quotes;
        } else {
            mood = moods[1];
            quotes = force_quotes;
        }
    } else {
        mood = moods[2];
        quotes = std_quotes;
    }

    if (name == 'cute') {
        hmm = "H" + 'm'.repeat(3 + Math.floor(Math.random() * 10)) + ".";
        document.querySelector('#text').innerHTML = hmm;
    } else {
        document.querySelector('#text').innerHTML = quotes[Math.floor(Math.random() * quotes.length)];
    }
        
    let image = "img/" + name + "-" + mood + ".jpg";
    document.getElementById("pic").setAttribute("src", image);
    
    console.log(text);
}