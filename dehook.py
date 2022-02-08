import requests
import json


def normal(webhook,content):
  webhook_url = webhook

  #json?でmainContentを入れる
  main_content = {
    "content": f"{content}"
  }
  #送信
  requests.post(webhook_url, main_content)


#--------------------------------------------


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


#------------------------------------------------

def easy_embed(webhook,title,description):
  #変数webhookを変数webhook_urlに代入。
  webhook_url = webhook
  
  #jsonでmainContentを入れる
  main_content = {
    #embed----------------------
    "embeds": [{
    "title": f"{title}!",
    "description": f"{description}"
    }]
    #--------------------------------
  }
  #送信
  requests.post(webhook_url,json.dumps(main_content),headers={'Content-Type': 'application/json'})

  
#username   = name
#avatar_url = icon
#content    = content
#normal     = メッセージ送信のみ
#user       = メッセージ送信&アイコン・ユーザーネームが変更できる
