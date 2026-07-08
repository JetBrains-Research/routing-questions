Mafia Game (MVP)

Overview
Single-room Mafia game. Players coordinate discussion externally; this service manages roles, phases, voting, eliminations, and win conditions. Only one game runs at a time globally.

Build this as a Python backend service with no UI; expose the functionality below through an HTTP API.

Constraints
- No timers; phases end on majority or when the Game Starter manually advances.
- No in-app chat, accounts, or mid-game joining.
- Player count: 4-16.

Lobby
- Players can join when no game is active.
- Joined players are visible to all in the lobby.
- Name requirements: 3-20 characters (letters, numbers, spaces, hyphens, underscores), unique within lobby (case-insensitive).
- Any joined player can start the game once 4+ players are present.
- While a game is in progress, new players cannot join; the lobby reports it is locked.
- When a game ends, the lobby reopens immediately for new players.

Game Start and Roles
- The player who starts the game becomes the Game Starter (controls manual phase advancement).
- Role assignment: Mafia count = max(1, floor(N/3)); remainder are Citizens.
- Each player can privately retrieve their role. Mafia also see all mafia teammates; Citizens see only their own role.
- Game begins at Day 1.

Day Phase
- Player status (Alive/Dead) is visible to all.
- All Alive players vote for one Alive player (self-votes allowed) or an explicit "No Elimination" option.
- Vote counts are public and reflect the current tally.
- Majority threshold = floor(Alive / 2) + 1.
- If any option reaches majority, Day ends immediately:
  - Player majority: that player is eliminated (Dead), role revealed.
  - No Elimination majority: no one eliminated.
- If the Game Starter ends Day without majority, resolve as No Elimination.
- After resolution, check win conditions; if game continues, transition to Night.

Night Phase
- Only Alive mafia vote; targets must be Alive Citizens (mafia cannot target mafia).
- Mafia see aggregated vote counts among themselves; non-mafia see nothing about night votes.
- Night majority threshold = floor(AliveMafia / 2) + 1. If any target reaches majority, Night ends immediately.
- If the Game Starter ends Night manually:
  - Unique highest-vote target: killed, role revealed.
  - Tie or no votes: no kill.
- After resolution, check win conditions; if game continues, transition to next Day.

Win Conditions
- Citizens win: all Mafia eliminated (Mafia count = 0).
- Mafia win: Mafia count >= Citizen count.
- Checked immediately after any Day elimination or Night resolution.
- On game end: reveal all roles, freeze voting, release lobby lock.
