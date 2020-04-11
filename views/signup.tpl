% include('shared/header.tpl')

<div class="span-24">
    <div class="span-11 box">
        <form action="/signup" method="POST">
            <table>
                <tr>
                    <td> 用户名:</td>
                </tr>
                <tr>
                     <td><input type="text" name="username" id="" style="width: 60%;"></td>
                </tr>
                <tr>
                    <td> 密码：</td>
                </tr>
                <tr>
                    <td> <input type="password" name="password" id="" style="width: 60%;"></td>
                </tr>
                <tr>
                    <td><button type="submit" style="width: 20%;">注册</button></td>
                </tr>
            </table>
       
        </form>
    </div>
    <div class="span-11 box last">
        <form action="/login" method="POST">
            <table>
                <tr>
                    <td> 用户名:</td>
                </tr>
                <tr>
                     <td><input type="text" name="username" id="" style="width: 60%;"></td>
                </tr>
                <tr>
                    <td> 密码：</td>
                </tr>
                <tr>
                    <td> <input type="password" name="password" id="" style="width: 60%;"></td>
                </tr>
                <tr>
                    <td><button type="submit" style="width: 20%;">登录</button></td>
                </tr>
            </table>
        </form>
    </div>
</div>
<hr>

% include('shared/footer.tpl')
