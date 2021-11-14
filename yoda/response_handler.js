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
let all_quotes = dark_quotes.concat(force_quotes, std_quotes);

function respond() {
    // Your Code Here
    var text = document.querySelector("#textbox").value;
    var random_quote = all_quotes[Math.floor(Math.random() * 15)];
    if(text.includes("cute") || text.includes("baby"))
    {
        if(text.includes("force"))
        {
            if(text.includes("dark"))
            {
                text = "img/cute-dark.jpg";
            }
            else{
                text = "img/cute-force.jpg";
            }
            
        }
        else{
            text = "img/cute-std.jpg";
        }
    }
    else
    {
        if(text.includes("force"))
        {
            if(text.includes("dark"))
            {
                text = "img/regular-dark.jpg";
            }
            else{
                text = "img/regular-force.jpg";
            }
        }
        else{
            text = "img/regular-std.jpg";
        }
    }
    document.getElementById("image").src = text;
    document.getElementById("quote").innerText = random_quote + " h" + "m".repeat(Math.floor(Math.random() * 10));
    document.getElementById("textbox").value = "";
    console.log(random_quote);
    document.getElementById("textbox").onkeypress=function(e){
        if(e.keyCode==13){
            e.preventDefault;
            document.getElementById("submit").click();
        }
    }
}


