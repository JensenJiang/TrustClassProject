#占坑
普天同庆，第一个api写好了！
##User App
###/user/api/profile/*
要求登录
####*为空
返回当前用户profile
####*为ID
返回用户ID为*的profile
~~~
GET /user/api/profile/
~~~
~~~
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "nickname": "hrsonion",
    "school": 2
}
~~~
