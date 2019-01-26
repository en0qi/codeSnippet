# Code Snippet
レポジトリにするほどでもないコードの切れ端集

## threholding.py
白黒画像から2値画像を生成
Excecute by entering the command below.
`python3 threholding.py ***[.jpg,.png]`

## gentask.py
たまに難しい問題を含む足し算掛け算の問題とその答えをCSV出力する

## labin.py
研究室に設置されているRaspberryPiに接続されたボタンを押すと、Slackにラボに来たことを通知し、同時にGoogleSpreadSheetに入室時間を記録。もう一度押すと退室を通知し時間を記録します。

## change_status.py
実行すると、Slackのステータスを変更します。ただAPIにリクエスト投げるだけ。

## labinout.py
RaspberryPiに接続された超音波距離センサーで、自分の机の前に人が座っているかいないかを検知。座っている場合は、Slackにラボにいることを通知、帰宅した場合はその旨を通知する。

## facedetect.py
OpenCVで顔検出をする

