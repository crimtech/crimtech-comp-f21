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

function respond() {
    let image = document.getElementById("img_yoda");
    let yodatalk = document.getElementById("yodatalk");
    let input = document.getElementById("txtbox").value;

    if (input.includes("cute") || input.includes("baby"))
    {
        image.setAttribute("src", "img/cute-dark.jpg");
        yodatalk.innerHTML = "hmmmmmmmmmmmmm";
    }
    if (input.includes("force"))
    {
        if (input.includes("dark"))
        {
            image.setAttribute("src", "img/regular-dark.jpg");
            nr = Math.floor(Math.random() * 5);
            yodatalk.innerHTML = dark_quotes[nr];
        }
        else
        {
            image.setAttribute("src", "img/regular-force.jpg");
            nr = Math.floor(Math.random() * 5);
            yodatalk.innerHTML = force_quotes[nr];
        }
    }
    document.getElementById("txtbox").value = "";
}