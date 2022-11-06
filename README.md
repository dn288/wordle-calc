# CS50 Final Project 2022 - Wordle/Katapat Score Calculator

Wordle/Katapat Score Calculator(WSC) is a simple web application that calculates the scores of the word games Wordle and Katapat. Wordle is the popular New York Times word game and Katapat is a similar game based on malay words.

wordle website https://www.nytimes.com/games/wordle/index.html

katapat website https://www.projecteugene.com/katapat.html

WSC is built using Flask, Python, HTML, CSS and Javascript. The WSC experience is optimized for access by both desktop or by mobile.

# WSC overview

Currently WSC is hosted at (https://wordle-score-calc.herokuapp.com/) and consists of 4 pages;

## WebPages
### Home 
This is the landing page where the one will be asked to select the game one wishes to calculate the score for, either Wordle or Katapat.

One will also be required to paste the input copied from either Wordle's or Katapat's website respectively.

The page is designed to prompt and guide the user if they errornously enter any inputs.

### Instructions
Simple HTML page providing instructions to the user.

### Formula
Simple HTML page providing user with the score formula.

### Links
Simple HTML page with HTML links to other sites to provide a richer user experience.

### Results (Accessible only after clicking on submit button on the homepage)
Presents user with their score in a doughnut format using ChartJs.


## Usage

An example to obtain score for Wordle.

First on the homepage, select Wordle.

Second, user will paste their statistics copied from the wordle/katapat website.

As an example for Wordle, a copied sample from Wordle might look like something this;

> STATISTICS 289 Played 97 Win % 15 Current Streak 57 Max Streak GUESS DISTRIBUTION 1 0 2 12 3 79 4 118 5 55 6 17 Something doesn't look right >

User then clicks on the submit button to be taken to the results page.

## Key Challenges
### Regex
The key part of the application was that both games uses the same regex to extract all the data required to calculate the score despite minor variations in the format of the respective games answers

For example, Wordle a typical copied result would look like this

> STATISTICS 289 Played 97 Win % 15 Current Streak 57 Max Streak GUESS DISTRIBUTION 1 0 2 12 3 79 4 118 5 55 6 17 Something doesn't look right 

Whereas, Katapats copied result would look like;

> STATISTIK  77 Main 96 % Menang 8 Kombo Semasa 14 Kombo Maksima TABURAN TEKAAN  1 0 2 6 3 24 4 26 5 13 6 5 

Both have similar a pattern except for the placement of the '%'

The resulting regex is as follows
'''
"^([A-Z]+\s\s?([0-9][0-9]?[0-9]?)\s[a-zA-Z]+\s([0-9][0-9]?[0-9]?)\s%?\s?[a-zA-Z]+\s\%?\s?([0-9][0-9]?[0-9]?)\s[a-zA-Z]+\s[a-zA-Z]+\s([0-9][0-9]?[0-9]?)\s[a-zA-Z]+\s[a-zA-Z]+\s[A-Z]+\s[A-Z]+\s\s?1\s([0-9][0-9]?)\s2\s([0-9][0-9]?[0-9]?)\s3\s([0-9][0-9]?[0-9]?)\s4\s([0-9][0-9]?[0-9]?)\s5\s([0-9][0-9]?[0-9]?)\s6\s([0-9][0-9]?[0-9]?))"

'''

### Doughnut Chart
Another challenge encountered was to position the score in the middle of the doughnut chart. This was finally achieved using CSS with the help from the following; 

https://mdbootstrap.com/snippets/jquery/marcin-luczak/3015337#js-tab-view

## Summary

Once the data is extracted it is then formatted into a list.

The list then forms the basis of the score calculations and also the data for the doughnut chart using chartjs.

The results are then sent via flask and rendered on results.html template.



