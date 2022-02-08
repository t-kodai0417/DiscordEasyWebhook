import requests
def normal(webhook,content):
  webhook_url = webhook

  #jsonでmainContentを入れる
  main_content = {
    "content": f"{content}"
  }
  #送信
  requests.post(webhook_url, main_content)
def user(webhook,content,icon,name):
  webhook_url = webhook

  #jsonでmainContentを入れる
  main_content = {
    "username": f"{name}",
    "avatar_url": f"{icon}",
    "content": f"{content}"
  }
  #送信
  requests.post(webhook_url, main_content)
