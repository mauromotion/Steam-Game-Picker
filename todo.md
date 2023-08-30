# Steam Random Picker To Do list

## Backend
- [ ] Set up routes
 - [ ] Home
  - [ ] Set up flashing alerts instead of apology.html
  - [ ] Set up the SQLite db
  - [ ] Insert data into db
 - [ ] Filters
  - [ ] Implement filters:
    - [ ] Any game
    - [ ] Any never played game
    - [ ] Any already played game
    - [ ] Any game in the first top 5
    - [ ] Any game in the first top 10
    - [ ] Any game in the first top 20
    - [ ] Nice to have: genres filters
 - [ ] Results
  - [ ] Implement re-roll with same settings
  - [ ] Go back to filters
  - [ ] Nice To Have: click to launch game
- [ ] Helpers
  - [x] Write random number in a len(list) function
  - [ ] Write function to build the correct URL for banners

I can try this:

  - Make a first API call for the user's library and specific data
  - Build the database with this data.
  - When a game is picked make a single API call for the game and store the data in a db table. Use the data to build the results.

Hopefully this way I'm not gonna make too many calls to the API and end up getting limited.

I think I need to save the json to a file so that I can build a db from it.

## Frontend

