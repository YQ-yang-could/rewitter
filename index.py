import bottle
import settings
import session
from conver import to_dict,to_list,to_set,to_string
import time
from model import User,Post

r=settings.r

def islogin():
    sess=session.Session(bottle.request,bottle.response)
    if sess.is_new():
        return False
    else:
        return User(sess['id'])

@bottle.get('/')
@bottle.view('index')
def index():
    user=islogin()
    if user:
        # username= to_string(r.hget('user:{}'.format(uid),'username'))
        # # 读取发布的留言
        # posts_id=to_list(r.lrange('user:{}:timeline'.format(uid),0,9))
        # # 发布内容
        # posts={}
        # for pid in posts_id:
        #     post=to_dict( r.hgetall('post:{}'.format(pid)))
        #     post['username']=to_string(r.hget('user:{}'.format(post['userid']),'username'))
        #     posts[pid]=post
        # # 粉丝
        # followers=to_list(r.smembers('user:{}:followers'.format(uid)))
        # followers=[to_string(r.hget('user:{}'.format(uid),'username')) for uid in followers]
        # followers_num=r.scard('user:{}:followers'.format(uid))
        # # 关注
        # following=to_list(r.smembers('user:{}:following'.format(uid)))
        # following=[to_string(r.hget('user:{}'.format(uid),'username')) for uid in following]
        # following_num=r.scard('user:{}:following'.format(uid))

        res={
            'username':user.username,
            'posts':user.posts(),
            'followers':user.followers(),
            'following':user.following(),
            'followers_num':user.followers_num(),
            'following_num':user.following_num()
        }

        return res
    else:
        bottle.redirect('/signup')

@bottle.get('/signup')
@bottle.view('signup')
def signup():
    return dict()

# 注册
@bottle.post('/signup')
@bottle.view('signup')
def resiter():
    username= bottle.request.POST['username']
    password= bottle.request.POST['password']

    user=User.create(username.password)
    # uid=r.hget('users',username)
    if user:
        sess=session.Session(bottle.request,bottle.response)
        sess['id']=user.id
        sess.save()
        bottle.redirect('/')
    return dict()
# 登录
@bottle.post('/login')
@bottle.view('signup')
def login():
    username=bottle.request.POST['username']
    password=bottle.request.POST['password']
    user=User.find_by_username(username)
    # uid=r.hget('users',username).decode('utf-8')
    if user:
    #    upassword= r.hget('user:{}'.format(uid),'password').decode('utf-8')
       if user.password==password:
           sess=session.Session(bottle.request,bottle.response)
           sess['id']=user.id
           sess.save()
           bottle.redirect('/')            
    return dict()
# 表单提交
@bottle.post('/post')
def post():
    user=islogin()
    if user:
        # 获取表单内容
        content=bottle.request.POST['content']
        Post.create(user,content)
        # pid=r.incr('post:uid')
        # pdata={
        #     'userid':uid,
        #     'content':content,
        #     'posttime':time.strftime("%Y-%M-%D %H:%M:%S",time.localtime())
        # }
        # r.hmset('post:{}'.format(pid),pdata)
        # r.lpush('user:{}:timeline'.format(uid),pid)
        # r.lpush('user:{}:posts'.format(uid),pid)
        # r.lpush('timeline',pid)
        # r.sadd('posts:id',pid)
        # 返回前端页面
        bottle.redirect('/')
    else:
        bottle.redirect('/signup')


# 加载静态资源
@bottle.route('/public/<filename:path>')
def send_static(filename):
    return bottle.static_file(filename,root='public/')

bottle.run(reloader=True)