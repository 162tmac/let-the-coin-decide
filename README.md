
# CS50 Final Project

    name: Tom McEvoy
    country: Ireland
    description: A web app that helps you make decsions by asking for input for a number of outcomes and selecting a random outcome.
    app name: Let The Coin Decide

## Summary

This is a Flask web app that is built with HTML, CSS, Bootstrap and Python.
The main use is for when you have to decide on something.
For example, you have two restaurants that you want to choose between and leave it to up to chance.
You can flip a virtual coin giving
the name of the restarants to the app and it will make a choice for you.
You can also ask a magic 8 ball, roll a dice or give a number of outcomes up to 100 and it will randomly choose one of the outcomes.
The app makes use of the Python Rand function mainly to do this.

## How to use the app

On the main page you have 4 calls to action. You can:
* Flip a coin
* Roll a dice
* Give a custom number of outcomes
* Ask a magic 8 ball

On every page, except the 8 ball, you can simply enter your outcomes that you want to choose between.
On the custom page you must first imput the number of choices you have.
Then, once you have given your input, click the submit button and you will be taken to the results page where your choice will be made.
For the magic 8 ball page, you ask a yes-no question and will get a response.

## How the app works

The functionality of the app is built with Python and using flask.
The inputs that users give are stored and then a random number is generated depending on how many choices there are.

## Youtube

[Here](https://www.youtube.com/watch?v=PC84HCg_cYQ&feature=youtu.be&ab_channel=TomMcEvoy) is a link to my YouTube video showing the fuctionality of the site.


