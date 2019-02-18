import json
from flask import Flask, request, Response

app = Flask(__name__)
@app.route('/tete', methods=['POST'])
def send_dm():
  channel_id = request.form.get('channel_id') 
  channel_name = request.form.get('channel_name')
  user_id = request.form.get('user_id')
  text = request.form.get('text')
  print(channel_id, channel_name, user_id, text)
  return 'Success', 200


@app.route('/', methods=['GET'])
def test():
    return Response('It works!')



if __name__ == '__main__':
  app.run(debug=True)
