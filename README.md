# Champions League Round of 16 Draw Algorithm
A simple algorithm to select the UEFA Champions League round of 16 draw, based on the method performed in 2021/2022. 

The runners up from each group are drawn by random, then eligible clubs are drawn at random. Elgible clubs are defined (in [Article 18.01](https://documents.uefa.com/r/Regulations-of-the-UEFA-Champions-League-2021/22/Article-18-Match-system-round-of-16-quarter-finals-and-semi-finals-Online)) as follows:
- Clubs from the same association cannot be drawn against each other.
- Group winners must be drawn against runners-up from a different group.

I can't find exception handling in the rule book for when a club doesn't have any eligible opponents remaining, thus this code will raise an error.

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