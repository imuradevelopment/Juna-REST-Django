# 登録

```ps1
curl.exe -X POST http://127.0.0.1:8000/api/v1/auth/users/ --data 'email=curl3@example.com&username=curlUsesr3&password=password0618&re_password=password0618'
# {"email":"curl3@example.com","username":"curlUsesr3","id":"184b3ec0-954f-4398-a0a9-27049faa9945"}
# http://127.0.0.1:8000/#/activate/MTg0YjNlYzAtOTU0Zi00Mzk4LWEwYTktMjcwNDlmYWE5OTQ1/aogosn-0478aac8cd7655c405ea305d29a93a57
```

## ユーザー詳細

```ps1
# JWT取得後の場合
curl.exe -LX GET http://127.0.0.1:8000/api/v1/auth/users/me/ -H 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI0MDI5NjgzLCJqdGkiOiJlZjY1MWE4ZTQxZTY0MDIyYmNkMDQ4NjIyMTQ4NDRjOSIsInVzZXJfaWQiOiIxODRiM2VjMC05NTRmLTQzOTgtYTBhOS0yNzA0OWZhYTk5NDUifQ.b2Ryp5Yrr2XKcq-GIfd2diuMNxGUM9U30oi3_KybRfI'
# {"email":"curl3@example.com","id":"184b3ec0-954f-4398-a0a9-27049faa9945","username":"curlUsesr3"}
curl.exe -LX GET http://127.0.0.1:8000/api/v1/auth/users/me/ -H 'Authorization: JSON eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI0MTE5NDExLCJqdGkiOiI2OTVhNzc3NTE4MTY0ZjY5YmY2OWIwMzdmMWUyYzc2NCIsInVzZXJfaWQiOiIzZTgxMjM4ZS1kNThjLTQ4N2ItODBkMy1jZjYyODk2NDhmYTAifQ.VHqj1IkWcKbBMuEPuG5T1u4dhtHKdpJPwNZWaqHqhJg'
```

## JWTトークンの発行

```ps1
# アクティベート後
curl.exe -X POST http://127.0.0.1:8000/api/v1/auth/jwt/create/ --data 'username=curlUsesr3&password=password0618'
# {"refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyNDExMjQ4MywianRpIjoiYWZjOGRkYmVjNWIwNDUxY2E0MTEwOWVlOThlYzg2YTkiLCJ1c2VyX2lkIjoiMTg0YjNlYzAtOTU0Zi00Mzk4LWEwYTktMjcwNDlmYWE5OTQ1In0.wBBMCYbSLGMhA84ofzSvulMOQmpS0hXbS88C739EJc0","access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI0MDI5NjgzLCJqdGkiOiJlZjY1MWE4ZTQxZTY0MDIyYmNkMDQ4NjIyMTQ4NDRjOSIsInVzZXJfaWQiOiIxODRiM2VjMC05NTRmLTQzOTgtYTBhOS0yNzA0OWZhYTk5NDUifQ.b2Ryp5Yrr2XKcq-GIfd2diuMNxGUM9U30oi3_KybRfI"}
```

## アカウントのアクティベート

```ps1
curl.exe -X POST http://127.0.0.1:8000/api/v1/auth/users/activation/ --data 'uid=MTg0YjNlYzAtOTU0Zi00Mzk4LWEwYTktMjcwNDlmYWE5OTQ1&token=aogosn-0478aac8cd7655c405ea305d29a93a57'
# メール
```