import os
from flask import Flask, request, Response
from slackclient import SlackClient

SLACK_TOKEN = os.getenv("SLACK_TOKEN")

slack_client = SlackClient(SLACK_TOKEN)


app = Flask(__name__)

def channel_info(channel_id):
  channel_info = slack_client.api_call("channels.info", channel=channel_id)
  if channel_info.get('ok'):
        return channel_info
  return None


def send_dms(user_id, message):
  slack_client.api_call(
      "chat.postMessage",
      channel=user_id,
      text=message
  )

@app.route('/tete', methods=['POST'])
def send_dm():
  text = request.form.get('text')
  if text[1] == '#':
    channel_id = text.split(' ')[0].split('|')[0][2:]
    remove_channel_name = text.split(' ')
    del remove_channel_name[0]
    text = ' '.join(remove_channel_name)
  else:  
    channel_id = request.form.get('channel_id')

  channel_information = channel_info(channel_id)
  channel_or_group_members = channel_information['channel']['members']
  for i in range(0, len(channel_or_group_members)):
      send_dms(channel_or_group_members[i], text)
  return 'Message Sent!', 200


@app.route('/', methods=['GET'])
def test():
    return Response('It works!')



if __name__ == '__main__':
  app.run(debug=True)
