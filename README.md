# Tic Tac Toe game
    *This is a tic tac toe game created for educational purposes.
    Code Institute portpholio project 3 

    <img src="assets/images/amiresponsive-tictactoe.png"/>

    Tic Tac Toe is an age old game that is played around the world. it can be playen on a game board, a paper and pen board, in a sand and rocks board and online in the computer. It is played by two people at a time. One player takes O and another X. The players take turn by turn to mark the space in the 3×3 grid. If the current player marks three of their marks diagonally, horizontally and vertically in a row or a column that player is declared the winner.
    <br>
    The deployed website can be viewed here. [Tic Tac Toe](https://tictactoepp3.herokuapp.com/).

# Table of contents
    - [Tic Tac Toe game](#Tic-Tac-Toe-game)
    - [Table of contents](#Table-of-contents)
    - [Project Goals](#Project-Goals)
    - [Flowchart](#Flowchart)
    - [Technologies](#Technologies)
    - [Existing features](#Existing-Features)
    - [future features](#Future-Features)
    - [Testing](#Testing)
    - [Bugs and solutions](#Project-Bugs-and-Solutions)
    - [deployment](#Deployment)
    - [credits](#Credits)

## Project Goals

 ### User Goals
    - user wants to Know the rules of the game before they start playing
    - user wants to Play the traditional classic tic tac toe online at ease
    - user wants to be able to play reapetdily if they wanted to and to restart the game.
    - user wants to get notified if they won.
    - user wants to play a logical game that is error free.
    - user wants to know the various ways in which they can win the game.

 ### Owner Goals
    - owner wants to create a game that is fun and and engaging to play
    - owner wants a lot of users to visit page
    - owner wants users to understand the rules of tic tac toe before users play
    - owner wants users to be aware of the diffrent ways they can win.
    - owner wants users to know the diffrent spots/marks and the numbers that conside with them
    - owner wants users to know when they entered an invalid input 
    - owner wants users to know that game cant continue unless correct input is entered
    - owner wants users to play the game, have fun and share the game with family and friends

## Flowchart
  <img src="assets/images/tictactoe-flowchart.jpg"/>
 
## Technologies

 ### Programing languages
 * Python

 ### The technologies and tools
 * Heroku for deploying and hosting. [see here](https://heroku.com/)
 * GitHub and gitpod for Cl and storage. [see here](https://github.com/)
 * App.diagrams for creating the flowchart. [see here](https://app.diagrams.net/)
 * Am i responsive to check responsivity across platforms. [see here](https://amiresponsive.co.uk/).
 * pep8 linter to check code for errors. [see here](https://pep8ci.herokuapp.com/) 

 ### Libraries
 * Random was used so that the computer can generate a random number.

## Existing Features 

 #### Introduction to game
  - As soon as the game is loaded or refreshed, the introduction to the game is shown. A welcome   message is shown as well as rules to the game. 
  <img src="assets/images/game-welcome.png"/>

 #### Game begins
  - After the welcome introduction a prompt message is shown for user to enter name. The game cannot begin whithout entering the name. Thereafter the Tic Tac Toe game board is displayed for the player to see the positions and places. after which another prompt message apears for player input. player has to enter an imput coressponding to the position they want from 1 to 9. If anything other than 1 to 9 is selcted or if spot is taken than game wont continue. 
 <img src="assets/images/game-begins.png"/>

 #### Game ends in tie
  - game ends in a tie if none of the 8 winning arangments are alighned or match. In such occation the player recieves a notification that game is over and endded on tie. Player is then given 2 options; to play the game again or to end the game. 
  <img src="assets/images/game-tie.png"/>

 #### Game ends in either player winning 
  - The game will continue with the 2 players taking turns untill any of the 8 winning arragments are matched horizentally, vertically or diagnaly. In such occation the player recieves a notification that game is over and they won or player "o" won. Player is then given 2 options; to play the game again or to end the game. 
  <img src="assets/images/game-winner.png"/>
 
 #### Play again or end the game
  - In the end the player is given two options to end the game or to keep playing. if they choose to play again, the game loads again from the begining. If they however choose to quit then player gets a good by massege. 
  <img src="assets/images/play-again.png"/>


## Testing

 ### Manual Testing


 



## Future Features


## Project Bugs and Solutions:
 
*  terminal wasnt working when used the command line.
* tried to display/print game board with a for loop. 
* number input wassnt catching invalid entries. 
* tried using player input outside varible. but coudnt
* when game checked for tie or winner, game wasnt ending. 
* found solution from stackoverflow to redefine the varible using global.
* userinput needs fursther verifications for non integer.
* when played, game was not folllowing through logic. like announced if player o won. or anounces if tie and end game. tried several solutions. fixed with help from tutors
* when press 2 to quit game, game was not quiting, tried making a function called quit all that sets gameplaying to false. unfortunaly that didnt help at all. i tried so many solutions and playd arround with code stubburly for hours. In the end i googled and found the solution was so simple all along. a build in function called quit() can be used or another called exit() amongst other solutions. i was gobsmacked but super happy

* check tie wasnt working. fixed it by removing additional winner arguent.
* persistant error of when player chooses to play gaian, current player becomes "o". when it shoud've been "x". fixxed this persistant error by re defining current player on both main function and play again or not function and setting current player to "x".


## Deployment

 
## Credits 

 ### winning arrangments and cheching for winnning

 ### handling input errors

 ### ending the game
 
 ### printing board and checking for tie

 
 ### Acknowledgements

 -	To the Code Institute for the course material, lectures and their grounded guidlines for the project.  

 -	To the Slack community for being so helpful, informative and inspiring

 - To [W3schools](https://www.w3schools.com/) and [Stack overflow ](https://stackoverflow.com/) for general reference regarding sytax, tags, elements and everything in between.
 - To my mentor Brian Bohare for supporting me, and encouraging me not to give up when everyhing got too hectic and overloaded with pressure at home and with studies. 

