<h1>5-Mini-Python-Projects</h1>

<h2>Description</h2>
This project is an attempt at creating/practicing some Python projects to get more familiar with the language.
<br><br/>
Projects in this repository follow the <a href="https://www.youtube.com/watch?v=DLn3jOsNRVE&ab_channel=TechWithTim">tutorial</a> given by Tech With Tim.


<h2>Languages and Utilities Used</h2>

- <b>Python</b> 

<h2>Environments Used </h2>

- <b>Windows 10</b> 

<h2>Projects and Descriptions:</h2>

<p align="left">
<h4>Project #1 - Quiz Game</h4>
<i>This is a simple game where a player is asked 4 questions and then is given a score based on how many they were able to answer correctly.</i>
<br /><br />
<h4>Project #2 - Number Guessing Game</h4>
<i>This is a simple number guessing game where a player selects a possible range and is then asked to guess a randomly generated number from within that range.  The player is given clues with each guess to help them know if they need to guess higher or lower.</i>
<br /><br />
<h4>Project #3 - Rock, Paper, Scissors</h4>
<i>This is a game of rock, paper, scissors which keeps track of how many times the computer vs the player wins.</i>
<br /><br />
<h4>Project #4 - Choose Your Own Adventure</h4>
<i>This is a choose your own adventure game where they player is given options in a story and is asked to decide what to do in order to advance the plot.</i>
<br /><br />
<h4>Project #5 - Password Managers (Most Advanced)</h4>
<i>This is a password manager that gives users the option to input credentials (into a text file) or display saved credentials.  While the program will display them in plain text, the password text file they are stored is is encrypted so that if opened it doesn't display the plain text passwords.</i>


<h2>What I learned:</h2>
<h3>Project #1 - Quiz Game</h3>
<li>Syntax for if statements in Python.</li>
<li>Syntax for f string formatting.</li>
<li>Adding to a variable using "+=" to create a counter.</li>
<br />
<h3>Project #2 - Number Guessing Game</h3>
<li>How to import modules into Python.  It was also interesting to learn that there are built in modules that don't need installation.</li>
<li>The syntax for a "while" loop including the use of the "continue" statement.</li>
<br />
<h3>Project #3 - Rock, Paper, Scissors</h3>
<li>How to add a list into an if statement.</li>
<li>Using the "not in" identity operator.</li>
<li>Using an index to pull a value from a pre-made list.</li>
<br />
<h3>Project #4 - Choose Your Own Adventure</h3>
<li>How nesting of if statements works.</li>
<li>Using elif statements.</li>
<br />
<h3>Project #5 - Password Managers (Most Advanced) </h3>
<li>Creation of Functions in Python</li>
<li>With statement in place of setting the contents of a file to a variable and then closing the file later (VARIABLE.close())</li>

```
with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
```
<li>Byte strings and why they're so important with <a href="https://stackoverflow.com/questions/67868931/which-are-the-advantages-of-byte-objects-over-string-objects-in-python">Cryptography</a>:".</li>
<i>"One example of when you might need to use bytes, is when working with crypto and pseudo-random sequence generation, where you will often end up with a sequence of bytes that cannot be represented 1-to-1 as a string. This is because you want to work with as large as possible an output space when generating pseudo-random numbers and sequences. See for example secrets.token_bytes from the stdlib."</i><br></br>
<li>open function with the read(r), write[will override file](w) and append(a).</li>
<li>The page break character "\n".</li>
<li>readlines function</li>
<li>rstrip()/strip() functions</li>
<li>.split() function</li>
<li>pip install cryptography</li>
<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
