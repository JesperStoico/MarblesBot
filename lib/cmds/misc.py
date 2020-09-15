import os

from lib import db


# This is the amount of 'sub-luck' the different memberships get
# staff = follower
# subscriber = sub :)
# Broadcaster = The streamer

amount = {
    'staff': 1,
    'subscriber': 3,
    'broadcaster': 5,
}


@db.with_commit
def join(bot, user, *args):
    # Check if the person is already in the db, if the person is already in
    # dont add the person
    already_in_db = db.record(
        "SELECT UserID FROM users WHERE UserID = (?)", user['name']
    )
    if not already_in_db:
        # Person not in db add to db
        db.execute(
            "INSERT OR IGNORE INTO users (UserID, Membership) VALUES (?, ?)",
            user["name"],
            user['badges']
        )
        # Add person to csv file
        with open("./files/marbles.csv", "a+") as csv:
            for i in range(amount[user['badges']]):
                csv.writelines(f"{user['name']}\n")
        bot.send_message(f"Hey {user['name']} you are now in the game!")


@db.with_commit
def marbles(bot, user, *args):
    # runs the script that drop the DB and makes a new one
    db.build()
    try:
        os.remove("./files/marbles.csv")
    except:
        pass
    bot.send_message("Hey all, game is now started, type !play to join the game.")
