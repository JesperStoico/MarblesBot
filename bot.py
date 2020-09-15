"""
    COPYRIGHT INFORMATION

Some code in this file is licensed under the Apache License, Version 2.0.
    http://aws.amazon.com/apache2.0/

Rest of the code is made by me, Jesper Stoico 2020.

"""

from irc.bot import SingleServerIRCBot
# from requests import get

from lib import cmds
import logging

NAME = "LazyCowBot"
OWNER = "noisecow"


class Bot(SingleServerIRCBot):
    def __init__(self):
        self.HOST = "irc.chat.twitch.tv"
        self.PORT = 6667
        self.USERNAME = NAME.lower()
        self.CLIENT_ID = "i64xwipfpnwhi49sjylw41xbxy8qx7"
        self.TOKEN = "sl9rflfdc8ilye6iz1g7fkukdd19bh"
        self.CHANNEL = f"#{OWNER}"

        super().__init__([(self.HOST, self.PORT, f"oauth:{self.TOKEN}")], self.USERNAME, self.USERNAME)

    def on_welcome(self, cxn, event):
        for req in ("membership", "tags", "commands"):
            cxn.cap("REQ", f":twitch.tv/{req}")

        cxn.join(self.CHANNEL)        
        self.send_message("Marbles bot are now online!")

    def on_pubmsg(self, cxn, event):
        logging.info(event.tags)
        tags = {kvpair["key"]: kvpair["value"] for kvpair in event.tags}
        # Badge info comes like this "broadcaster/1", so cutting away the /X so just get the badge
        badge = tags['badges'].split("/")[0]
        user = {
            "name": tags["display-name"],
            "id": tags["user-id"],
            "badges": badge,
        }
        message = event.arguments[0]

        if user["name"] != NAME:
            cmds.process(bot, user, message)

    def send_message(self, message):
        self.connection.privmsg(self.CHANNEL, message)


if __name__ == "__main__":
    bot = Bot()
    bot.start()
