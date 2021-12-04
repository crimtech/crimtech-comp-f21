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
document.addEventListener('DOMContentLoaded', function(){
    let talk = document.getElementById("talk");
    document.addEventListener("keydown", function (e) {
        if (e.key === "Enter") {  
            talk.innerHTML = "h" + s + "\n"+ force_quotes[Math.floor(Math.random()*5)];
        }
      }); 
let responder = document.getElementById("responder"); 
responder.onclick = ()=> { 
    respond(); 
};
let pic = document.getElementById("pic"); 
let quote = document.getElementById("textbox");
function respond() {
    // Your Code Here
    let text = quote.value;
    if (text.includes("cute") || text.includes("baby"))
    {
        pic.setAttribute("src", "./img/cute-std.jpg");
    }   
    else if (text.includes("force"))
    {
        if (text.includes("dark"))
        {
            pic.setAttribute("src", "./img/regular-dark.jpg");
        }
        else
        {
            pic.setAttribute("src", "./img/regular-force.jpg");
        }
    }
    quote.value = ""; 
    let talk = document.getElementById("talk");
    let s = "";
    for (let i = 0; i < Math.random()*15 +7; i++)
    {
        s+="m";
    }

    talk.innerHTML = "h" + s + "\n"+ force_quotes[Math.floor(Math.random()*5)];
    console.log("Hello World!");
    console.log(quote.innerHTML);
    quote.innerHTML = ""; 

}

});