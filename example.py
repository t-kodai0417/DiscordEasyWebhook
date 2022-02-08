import dehook as dk
webhook=r"https://discord.com/api/webhooks/010101010101010101010101/yajuu_senpai11451444444_0101010101010101-p-_010101010101"
icon=r"https://github.githubassets.com/apple-touch-icon.png"
#メッセージのみ送信
dk.normal(webhook,"hello!")
#名前とアイコンをカスタム
dk.user(webhook,"Hello!(2)",icon,"Tester")
#簡単なEmbed
dk.easy_embed(webhook,"Hi!","I am Tester.")


