# Project Proposal: Predicting NFL draft
**Luke Newman**

#### Domain
College football player stats are available for every college for the past 10 years.  This includes their height, weight, position, and also their in game stats for top players.  Also, the NFL draft posts a list of all the players who are drafted.  

My goal is to predict whether a college player will be drafted based on his career stats by combining these two data sets.  

#### Data

Variable | type | Description | Used for Model
-------- | ---- | ----------- | --------------
Player | str | player's name | Yes
Wt | int | Player's weight | Yes
Ht | int | Player's height | Yes
Pos | str | Player's position | Yes
Rushing | int | Rushing yards | Yes
Passing | int | Passing yards | Yes 
Receiving | int | Receiving yards | Yes
Punt Returns | int | Punt Returns | Yes
Field Goals | int | Number of field goals | Yes
PAT | int | Point after touchdown | Yes
Scoring | int | Total points scored | Yes
TD | int | Touchdowns | Yes
1XP | int | number of extra points | Yes
2XP | int | 2 extra point conversions | Yes
Safety | int | number of safetys | Yes
Tackles | int | number of total tackles | Yes
Solo | int | number of solo tackles | yes
Assisted | int | number of assisted tackles | yes
Sacks | int | number of sacks | Yes
Sack Yards | int | number of sack yards | Yes
TFL | int | tackles for loss | Yes
TFL yards | tackles for loss yards | yes
Int | int | interceptions | Yes
Int yards | int | interception yards | Yes
Int TD | int | interception result in TD | YEs
Passes Broken Up | int | number of passes proken | yes
Passes defended | int | number of passes defended | yes
Fumbles forced | int | number of fumbles forced | yes
Kicks/punts blocked | int | number of blocked kicks/punts | yes
Drafted/Not drafted | str | indicates whether player got drafted | yes