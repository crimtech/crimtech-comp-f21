
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

function searchKeyPress(e) {
    // look for window.event in case event isn't passed in
    e = e || window.event;
    if (e.keyCode == 13)
    {
        document.getElementById('butt').click();
        return false;
    }
    return true;
}

function respond() {
    // Your Code Here
    let imageSource = "img/regular-std.jpg";
    console.log(box.value);

    selection = 3 * Math.random();
    quoteSelect = Math.floor(5 * Math.random());
    text = box.value.toLowerCase();

    if (text.includes("baby") || text.includes("cute")) {
        document.getElementById("quote").innerHTML = "Mommyyyy";
        if (text.includes("force")) {
            imageSource = "img/cute-force.jpg";
        } else if (selection < 1) {
            imageSource = "img/cute-dark.jpg";
        } else if (selection < 2) {
            imageSource = "img/cute-force.jpg";
        } else {
            imageSource = "img/cute-std.jpg";
        }
    } else if (text.includes("dark") && text.includes("force")) {
        imageSource = "img/regular-dark.jpg";
        if (selection < 1.5) {
            document.getElementById("quote").innerHTML = dark_quotes[quoteSelect];
        } else {
            document.getElementById("quote").innerHTML = force_quotes[quoteSelect];
        } 
    } 
    else if (text.includes("force")) {
        imageSource = "img/regular-force.jpg";
        document.getElementById("quote").innerHTML = force_quotes[quoteSelect];
    } 
    else if (text.includes("dark")) {
        imageSource = "img/regular-dark.jpg";
        document.getElementById("quote").innerHTML = dark_quotes[quoteSelect];
    } 
    else {
        imageSource = "img/regular-std.jpg";
        document.getElementById("quote").innerHTML = std_quotes[quoteSelect];
    }
    document.getElementById("image").src = imageSource;
    box.value = "";

    hm = "hm";
    hm += "m".repeat(100 * Math.random());
    document.getElementById("hm").innerHTML = hm;
}