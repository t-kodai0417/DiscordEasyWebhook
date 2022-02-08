import requests
def normal(webhook,content):
  webhook_url = webhook

  #json?でmainContentを入れる
  main_content = {
    "content": f"{content}"
  }
  #送信
  requests.post(webhook_url, main_content)
def user(webhook,content,icon,name):
  webhook_url = webhook

  #json?でmainContentを入れる
  main_content = {
    "username": f"{name}",
    "avatar_url": f"{icon}",
    "content": f"{content}"
  }
  #送信
  requests.post(webhook_url, main_content)

#username   = name
#avatar_url = icon
#content    = content
#normal     = メッセージ送信のみ
#user       = メッセージ送信&アイコン・ユーザーネームが変更できる
