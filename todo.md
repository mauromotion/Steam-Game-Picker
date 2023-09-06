# Steam Random Picker To Do list

## Backend
- [x] Set up routes
 - [x] Home
  - [x] Set up flashing alerts instead of apology.html
  - [x] Set up the SQLite db
  - [x] Insert data into db
 - [x] Filters
  - [x] Implement filters:
    - [x] Any game
    - [x] Any never played game
    - [x] Any already played game
    - [x] Any game in the first top 5
    - [x] Any game in the first top 10
    - [x] Any game in the first top 20
    - [ ] Nice to have: genres filters
 - [x] Results
  - [x] Implement re-roll with same settings
  - [x] Go back to filters
  - [ ] Nice To Have: click to launch game
- [x] Helpers
  - [x] Write random number in a len(list) function
  - [x] Write function to build the correct URL for banners
  - [x] Write function to pick a random game that accepts a string/query as argument.

I can try this:

  - Make a first API call for the user's library and specific data
  - Build the database with this data.
  - When a game is picked make a single API call for the game and store the data in a db table. Use the data to build the results.

Hopefully this way I'm not gonna make too many calls to the API and end up getting limited.
  It worked!

I think I need to save the json to a file so that I can build a db from it.
  I didn't had to.

To avoid repeating all the code for the various filters I could make a function that accept as an argument a string that is the actual db query, the only different part of each filter.
  I need to give two args to the function, one for the count query and one for the actual slice.

## Frontend
- [ ] Make it responsive
- [ ] Give it a bit of style
- [ ] May try out some nice fonts from Bunny Fonts


