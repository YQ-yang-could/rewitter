<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width,initial-scale=1.0">
        <title>rewitter</title>
        <link rel="stylesheet" href="/public/css/screen.css">
        <link rel="stylesheet" href="/public/css/custom.css">
    </head>
<body>
    <div class="container">
        <div id="header" class="span-24">
            <div class="span-12">
                <br>
                <h1>Rewitter</h1>
            </div>
            % if defined('username'):
            <div class="span-12 last right-align">
                <br>
                <br>
                <a href="/">首页</a>|
                <a href="/mentions/{{username}}">与我相关</a>|
                <a href="/{{username}}">{{username}}</a>|
                <a href="/timeline">社交圈</a> |
                <a href="/logout">退出</a>
            </div>
            % end
            <hr>
        </div>