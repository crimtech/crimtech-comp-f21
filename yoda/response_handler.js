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

let send_button = document.getElementById("send");
let input_field = document.getElementById("yoda_input");
let chat_text = document.getElementById("response");
let image = document.getElementById("yoda_image");

document.addEventListener("keydown", function(event) {
    
    if (event.key === "Enter")
    {
        send_button = document.getElementById("send");
        send_button.click();
    }
});

function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}

function respond() {

    input_field = document.getElementById("yoda_input");
    chat_text = document.getElementById("response");
    image = document.getElementById("yoda_image");

    let dialogue = "";
    let new_img = "img/";

    all_quotes = dark_quotes.concat(force_quotes, std_quotes);

    if(input_field.value.toLowerCase().includes("baby") || input_field.value.toLowerCase().includes("cute"))
    {
        new_img += "cute-";
    }
    else
    {
        new_img += "regular-";
        dialogue = all_quotes[getRandomInt(all_quotes.length)];
    }

    if (input_field.value.toLowerCase().includes("force"))
    {
        if (input_field.value.toLowerCase().includes("dark"))
        {
            new_img += "dark";
        }
        else
        {
            new_img += "force"
        }
    }
    else
    {
        new_img += "std";
    }

    // Add file extension to image path.
    new_img += ".jpg";

    // Update image path and chat content on site.
    image.src = new_img;

    // Add to dialogue

    hmmm = " Yes, H";
    for (let i = 0, n = getRandomInt(12) + 6; i < n; i++)
    {
        hmmm += "m";
    }
    hmmm += ".";

    chat_text.innerHTML = dialogue + hmmm;

    // Reset input field after job is done.
    input_field.value = "";
    
}