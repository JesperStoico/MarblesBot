/* membership is the status they have in twitch
    1 = Not following
    2 = Follower
    3 = Subtier 1
    4 = Subtier 2
    5 = Subtier 3
*/

DROP TABLE IF EXISTS users;

CREATE TABLE users (
    UserID text PRIMARY KEY,
    Membership INTEGER
);