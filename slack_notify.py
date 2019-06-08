# ライブラリインポート
import requests

# 設定
TOKEN='https://hooks.slack.com/services/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'
CHANNEL='smartse_k9'
TEXT='slack_test'
USERNAME='da-okazaki@outlook.com'
URL='https://slack.com/api/chat.postMessage'

# post
post_json = {
    'token': TOKEN,
    'text': TEXT,
    'channel': CHANNEL,
    'username': USERNAME,
    'link_names': 1
}
requests.post(URL, data = post_json)