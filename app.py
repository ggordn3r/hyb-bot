import os
import csv
from tactics import Tactics
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

t = Tactics()
t.load()

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# Listens to incoming messages that contain "hello"
@app.message("Sinai")
def message_hello(say):
    # say() sends a message to the channel where the event was triggered
    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": "BOO!"}
            }
        ],
        text="BOO!"
    )

@app.action("button_click")
def action_button_click(body, ack, say):
    # Acknowledge the action
    ack()
    say(f"<@{body['user']['id']}> clicked the button")

# The /hackme command replies with a random tactic from 
@app.command("/hackme")
def generate_tactic(ack, respond):
    # Acknowledge command request
    ack()
    title, body = t.draw()
    respond(f"Try this: {title} \n{body}")
# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()