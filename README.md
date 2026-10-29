# NFL Prediction Model

This repository contains a series of models for predicting NFL match results. The writeup and background for each kind of model is included below. My goal for this project was to design a series of models to gauge which statistical method is best.


### Bernoulli Modelling

This is the simplest model that we can design and hence, the one I started with. A Bernoulli distribution is a discrete probability distribution that only models two possible outcomes. In the context of predicting match results, we can use the simple WIN or LOSS categories.

The idea for creating the Bernoulli model is simple: count all the wins and losses of each team across the season to determine a team's win percentage. Then, we can find the likelihood of each team winning a bracket and select the team with the highest likelihood as the most probable Superbowl winner for that season.
