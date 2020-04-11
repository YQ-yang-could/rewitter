
% include('shared/header.tpl',username=username)
<div class="span-24">
    <div class="span-16">
        <div id="updateform" class="box">
            <form action="/post" method="POST">
                {{username}},欢迎留言...
                <textarea name="content" id="" cols="70" rows="3"></textarea>
                <br>
                <input type="submit" value="发送">
            </form>
        </div>

        <div id="posts" class="span-15">
            % for post in posts:
            <div class="post">
                <strong>{{ post.username }}</strong>
                {{ post.content }}
                <div class="date">{{post.posttime}}</div>
            </div>
            % end
        </div>
    </div>

    <div class="span-7 last">
        <div class="box">
            <h4>粉丝数：{{followers_num}}</h4>
            <ul class="user-list">
                % for user in followers :
                <li>{{user.username}}</li>
                % end
            </ul>
        </div>

        <div class="box">
            <h4>关注：{{following_num}}</h4>
            <ul class="user-list">
                % for user in following :
                <li>{{user.username}}</li>
                % end
            </ul>
        </div>
    </div>
</div>
% include('shared/footer.tpl')