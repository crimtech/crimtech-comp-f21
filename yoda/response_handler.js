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

addEventListener("keyup", function(event) {
    if (event.key === 'Enter') {
        document.getElementById("userbutton").click();
    }
});

function respond() {
    // Your Code Here
    yodaImage = document.getElementById("yodaimg");
    yodaSpeech = document.getElementById("yodaspeech");
    userInput = document.getElementById("usertext").value;
    if (userInput.includes("cute") || userInput.includes("baby"))
    {
        yodaImage.setAttribute("src", "file:///C:/Users/bryan/Coding/Repositories/crimtech-comp-f21/yoda/img/cute-std.jpg");
        yodaSpeech.innerHTML = "hmmmmmmmmmmm.";
    }
    if (userInput.includes("force"))
    {
        if (userInput.includes("dark"))
        {
            yodaImage.setAttribute("src", "file:///C:/Users/bryan/Coding/Repositories/crimtech-comp-f21/yoda/img/regular-dark.jpg");
            num = Math.floor(Math.random() * 5);
            yodaSpeech.innerHTML = dark_quotes[num];
        }
        else
        {
        yodaImage.setAttribute("src", "file:///C:/Users/bryan/Coding/Repositories/crimtech-comp-f21/yoda/img/regular-force.jpg");
        num = Math.floor(Math.random() * 5);
        yodaSpeech.innerHTML = force_quotes[num];
        }
    }
    document.getElementById("usertext").value = "";
}