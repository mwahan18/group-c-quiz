# Group C - Online Quiz

## Team
| Name | Role | GitHub |
|Mahan |Leader |mwahan18|
| ... .| ....  | ..... |

## Description
A terminal quiz program. It reads multiple-choice and true/false questions from a JSON file
(and from the Open Trivia DB API), runs a quiz, saves scores and shows a leaderboard and charts.

## How to run
    pip install -r requirements.txt
    python main.py
Login: admin / Py@12345

## Features
- Show / add questions, load questions from the internet (fallback to local file)
- Quiz with random questions (MultipleChoice = 2 pts, TrueFalse = 1 pt)
- Leaderboard (top 10), player statistics, score histogram

## Class diagram
    Question
     |- MultipleChoice
     |- TrueFalse
    Player, Quiz (manager), Leaderboard

## Data files
- data/questions.json - question bank (12 samples)
- data/scores.json - results of all quizzes

## Credits
Questions from https://opentdb.com (CC BY-SA 4.0)
