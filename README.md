# Champions League Round of 16 Draw Algorithm
A simple algorithm to select the UEFA Champions League round of 16 draw, based on the method performed in 2021/2022. 

The runners up from each group are drawn by random, then eligible clubs are drawn at random. Elgible clubs are defined (in [Article 18.01](https://documents.uefa.com/r/Regulations-of-the-UEFA-Champions-League-2021/22/Article-18-Match-system-round-of-16-quarter-finals-and-semi-finals-Online)) as follows:
- Clubs from the same association cannot be drawn against each other.
- Group winners must be drawn against runners-up from a different group.

I can't find exception handling in the rule book for when a club doesn't have any eligible opponents remaining, thus this code will raise an error. I also considered alternative methods of drawing to avoid invalid draws.

## Getting Started
All code is in the `cl_draw.py` file.

The `draw_clubs` function takes in a dataframe with 4 variables:
| Column  | Type    | Label                                       |
|---------|---------|---------------------------------------------|
| club    | string  | Name of the club                            |
| group   | string  | Group number in round of 32                 |
| finish  | integer | Winner (1) or runners up (2) in their group |
| country | string  | Country/association of club                 |

Then returns a dataframe listing the clubs in each match.

## Alternative Methods of Drawing
Using the drawing method outlined by the UFEA rule book, around 1/5 of the draws in 2021 would be invalid by the clubs in match 8 being incompatible. Thus, I considered three alternative methods of drawing the round of 16:
1. `draw_clubs_country`
2. `draw_clubs_country_alt`
3. `draw_clubs_order`

`draw_clubs_country` prioritises the countires with clubs in both the winners and runners up slots, which would reduce the likelihood of an invalid draw. However, smaller countries might view this method as unfair due to ealier draws could lead to earlier matches. But, this can be tackled by a match number randomisation at the end.

`draw_clubs_country_alt` is another method that is similar to the `draw_clubs_country` but it alternates between drawing winners and runners up, as performed in 2020 UEFA Champions League.

`draw_clubs_order` produces no invalid draws, as it updates the pool of runners up being drawn based on the number of eligible teams (winners) they have to pick from. However, this method may be the most difficult to follow for a TV audience.