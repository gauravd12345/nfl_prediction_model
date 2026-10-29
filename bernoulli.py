import pandas as pd
import nflreadpy as nfl

# load schedule and teams
season = 2025
ld_schedule = nfl.load_schedules([season])
ld_teams = nfl.load_teams()

teams = set(ld_teams['team_abbr'])

# dictionary to maintain abbreviation to full name
atn = {}
for abbr, name in zip(ld_teams['team_abbr'], ld_teams['team_name']):
    atn[abbr] = name

# game statistics
game_type = ld_schedule['game_type']    # REG, WC, DIV, CON, SB
home_team = ld_schedule['home_team']
away_team = ld_schedule['away_team']
location = ld_schedule['location']
result = ld_schedule['result']
overtime = ld_schedule['overtime']


# calculate W/L results and # of games played
wins, losses, N = {}, {}, {}
for gt, ht, at, l, r, o in zip(game_type, home_team, away_team, location, result, overtime):
    if gt == "REG":
        if r > 0:
            wins[ht] = wins.get(ht, 0) + 1
            losses[at] = losses.get(at, 0) + 1
        else:
            wins[at] = wins.get(at, 0) + 1
            losses[ht] = losses.get(ht, 0) + 1

        N[ht] = N.get(ht, 0) + 1
        N[at] = N.get(at, 0) + 1

# calculate win/loss percentage for each team
wlp = {}
for wr, lr in zip(wins, losses):
    wlp[wr] = wlp.get(wr, 0) + wins[wr] / (wins[wr] + losses[lr])

# calculate bernoulli likelihood of each team winning every game
likelihood = {}
for p in wlp:
    print(p, N[p], wins[p], losses[p])
    likelihood[p] = likelihood.get(p, 0) + (wlp[p]**N[p])

# print top 5 ranking(#1 is predicted superbowl winner)
for team, prob in sorted(likelihood.items(), key=lambda x: x[1], reverse=True)[:5]:
    print(atn[team], prob)

