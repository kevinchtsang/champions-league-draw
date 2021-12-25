# -*- coding: utf-8 -*-
"""
Champions League Draw Algorithm

@author: kevinchtsang
"""

import pandas as pd
import numpy as np

## 2021 results of group stages
# variables of the dataframe:
# - club name
# - round of 32 group
# - position where the club finished in the group stages (winner = 1, runners up = 2)
# - which football association the club belongs to
group_2021_df = pd.DataFrame({
        'club': ['Manchester City', 'Paris Saint-Germain',
                 'Liverpool', 'Atletico Madrid',
                 'Ajax', 'Sporting CP Lisbon',
                 'Real Madrid', 'Internazionale',
                 'Bayern Munchen', 'Benfrica',
                 'Manchester United', 'Villarreal',
                 'Lille OSC', 'FC Salzburg',
                 'Juventus', 'Chelsea'],
        'group': ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D',
                  'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H'],
        'finish': [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
        'country': ['Eng', 'Fra',
                    'Eng', 'Esp',
                    'Ned', 'Por',
                    'Esp', 'Ita',
                    'Ger', 'Por',
                    'Eng', 'Esp',
                    'Fra', 'Aut',
                    'Ita', 'Eng']
        })

## eligibility check
# The round of 16 pairings are determined by means of a draw in accordance with the following principles:
# - Clubs from the same association cannot be drawn against each other.
# - Group winners must be drawn against runners-up from a different group.
# - The runners-up play the first leg at home.
def eligible_clubs(club_name, group_df):
    ok_clubs = []
    club_info = group_df[ group_df['club'] == club_name ]
    
    # select opposite of group winner/runner up
    # select from a different group
    # select from a different country
    group_subset = group_df.loc[(group_df['finish']  == (3 - club_info.finish.item())) & 
                                (group_df['group']   != club_info.group.item()) & 
                                (group_df['country'] != club_info.country.item())]
    
    ok_clubs = group_subset['club']
    
    return ok_clubs

## draw
# proceedure for draw:
# 1 - pick runner up at random
# 2 - select from eligible winners

def draw_clubs(last16_df):
    # initialise    
    winners = last16_df[last16_df['finish'] == 1]['club']
    runners = last16_df[last16_df['finish'] == 2]['club']
    
    unchosen_clubs = last16_df.copy()
    matches = pd.DataFrame(columns = ['match', 'winner', 'runner'])
    
    match_i = 1
    
    while not runners.empty:
        # 1 - pick runner up at random
        runner_club_idx = np.random.choice(runners.index)
        runner_club     = runners.pop(runner_club_idx)
        
        # 2 - select from eligible winner
        ok_clubs = eligible_clubs(runner_club, unchosen_clubs)
        if ok_clubs.empty:
            raise ValueError("No elgible clubs")
        else:
            winner_club_idx = np.random.choice(ok_clubs.index)
            winner_club     = winners.pop(winner_club_idx)
        
        # update unchosen clubs
        unchosen_clubs = unchosen_clubs.drop(
                labels = runner_club_idx, 
                axis = 0).drop(
                        labels = winner_club_idx,
                        axis = 0)
        
        # record drawn teams
        matches.loc[match_i] = pd.Series({
                'match':  match_i, 
                'winner': winner_club, 
                'runner': runner_club})
    
        match_i += 1

    return matches

ro16_matches_2021 = draw_clubs(group_2021_df)
