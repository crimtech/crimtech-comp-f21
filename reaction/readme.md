# Project 4: Reaction
In this project, you will be building a web application with React to measure your reaction time! This will combine the skills we learned in Yoda Chat with some of the skills we learned in Snake.

## A. What is React?
React is a Javascript-based frontend framework developed and maintained by Facebook. It is a *very* popular choice for building websites and web apps. The Crimson (somewhat) recently migrated its frontend to React, in part to help speed up/improve overall the performance of the website.

Before we go any further, open up the [React documentation](https://reactjs.org). Trust us, you'll be referencing the documentation A LOT during this project. (Documentation should already be your best friend!)

## B. Installing React
0. You probably know the drill by now, but you will need to pull from upstream. This means `git pull upstream master` and resolve any merge conflicts that arise.
1. Install Node.js. This is quite simple now that we have experience with the terminal! For MacOS, type `brew install node`. For Linux/WSL, use `sudo apt install nodejs`.
2. Check your versions by typing `node -v` and `npm -v`. `npm` comes packaged with Node. To run react, you will need `npm` version 5 or above and node version 8 or above.
3. If you do not have version 5 or above, run `npm install -g npm@latest`. This should get you the latest version.
4. Put your versions of `npm` and `node` into `lab3-responses.md`.
5. Next, we are ready to use React. Run `npx create-react-app reactions`, which can take a while. `cd` into the folder and run `npm start`.

Your browser should be loading up `localhost:3000` after this, and you should see a spinning react logo. If so, your installation is complete!

Feel free to make a commit now so you don't lose your progress.

6. If you are using Chrome, consider getting the [React Developer Tools](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en) extension. The normal browser developer inspector tool is not very informative for React-based projects, so if you're looking for more help with debugging, we highly recommend checking out this extension! And if you're not using Chrome...well...seek out help please.

## C. Setting Up the Project
Run `npx create-react-app reactions` in this folder. The terminal will report any installation error. If so, you can either fix them by seraching on Google or call us over.

Next, *delete the `reactions/src` folder* and copy the `src` folder into `reactions/src`. This contains the starter code we will use to write the app.

## D. Overview of the Project
You're building a website that tests a user's reaction time. Check out [Human Benchmark](https://humanbenchmark.com/tests/reactiontime) for an example. To start the test, the user will click on a button. That click will make the button turn red, which will start a timer. At some point in the future, the button will turn green. The user should try to click on the button as soon as possible. Based on the timing of the click, you will be able to calculate and output their reaction time.

## E: Getting Acclimated to React
The style of thinking necessary for building a React app is quite different from what you may learn in CS50 or what you've done for the past comp labs, so we'll try to provide you with more guidance in this README.

First, spend some time browsing the files in the `src` folder. Pay particular attention to `App.js`, where you'll basically spend all your time for this project. Once you've spent a little time reading this file (and perhaps others) over (and you're probably very confused, which is totally normal!), you're ready to start learning a bit more about React!

If you attended the comp meeting, you may have already watched [this excellent, brief, high-level overview of React by Programming by Mosh](https://www.youtube.com/watch?v=N3AkSS5hXMA). It's worth a watch...and a re-watch!

Programming by Mosh's video is great, but you'll need a little more detail to get started developing and understanding our instructions for the lab. So, please read parts 1-6 (Hello World - Handling Events) of [this introductory React guide](https://reactjs.org/docs/hello-world.html). Feel free to read more of the guide if you're interested, but we recommend doing so at a later point. We don't want you to get too overwhelmed by all this new information! Let's focus on solidifying the basics first.

## F: Getting Acclimated to This Project's Starter Code
In `App.js`, you'll find the big boy, the root, of your React App: the `App` component (function). We set up `App` to return (render) a header ("How Fast is your Reaction Time?"), the "button" you'll be using to test your user's reaction time (`Panel`), and some instruction text ("Click as soon as the red box turns green. Click anywhere in the box to start."). Let's take a closer look at your button, the `Panel` component:

The Panel keeps track of the following states:
* `start_time`, which will store the last time when `start_count` is called.
* `ran_once, which will store whether or not the user has played the game once.
* `counting`, which will store whether or not we are currently counting (playing the game).
* `true_duration`, which will store how long it's supposed to take before the button turns green.
* `color`, which will store the color of the button.

## G: The `start_count` function
When we start the counting, we need to set the following states:
* `start_time` should be set to the current time. In React, the function `window.performance.now()` stores how many milliseconds it has been since the website was loaded. It should be helpful.
* `true_duration` should be set to some random value between 2s and 7s.
* `counting` should now be True.
* `color` should be dark red.

Note about React: instead of writing `this.state.counting = true;`, you should use `this.setState({counting:true});`. The setState function informs React that a state has been changed, correctly triggering a re-render of the component. If you change a state variable directly, you can mess up the react framework.

## H: Extra Resources
Before we go any further, if you're feeling very lost right now, we recommend spending some more time learning the basics of React. There are TONS of resources online, and you can probably guess what we'd recommend...another Programming with Mosh video: https://www.youtube.com/watch?v=Ke90Tje7VS0&t=18s

## I: Change color to red after `true_duration` seconds.
Look into a function called `setTimeout`, and make a function that will change the color of the button to be green. The button should turn green after exactly `true_duration` seconds.

Note about React: if you write `this.setState({counting:true}); console.log(this.state.counting);` you may sometimes find that `this.state.counting` is not set to True. This is because the `setState` function is not guaranteed to change the state right then and there.

## J: The `end_count` function
If at most `this.state.true_duration` seconds have passed, do nothing. Otherwise, we need to set the following states:
* `ran_once` should be set to true: we have ran once, after all.
* `counting` should be set to false: we have finished the game.
* `reaction_time` should be set to the difference between (the number of seconds that have elapsed) and `this.state.true_duration`.

## K: The `render` function
You should change the `msg` variable depending on what `this.state` is.
* If `this.state.counting` and the button is red, msg is `Wait for Green`.
* If `this.state.counting` and the button is green, msg is `Click!`.
* Otherwise, if you have ran once, msg is `Your reaction time is {this.state.reaction_time} ms`.
* Otherwise, we have never run the test. So, msg is `Click me to begin!`

## L: CSS
Right now the box is small and hard to click on. Let us make it big and nice to click on! Please also align the text in the center.

We recommend using a flex box, which you can learn more about at [w3schools](https://www.w3schools.com/css/css3_flexbox.asp). Consider using `justify-content` and `align-items`.

## M: Submit!
Submit your assignment like usual. Congrats on finishing your final lab - you're so close to completing the comp! :)
