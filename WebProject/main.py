from flask import Flask, request, redirect, render_template, url_for
from sql import Add_User, Is_Existed, Edit_User, Find_Data
from visualization1 import Visualization

# 创建 Flask 应用实例
app = Flask(__name__)
username = {}
datas = []

# app.route是创建路由，主要是为了提示浏览器如何访问之后的函数部分
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('log.html')
    else:
        # 处理表单提交
        global username
        username = request.form.get('username')
        password = request.form.get('password')
        # 这里应该添加验证用户名和密码的逻辑
        if Is_Existed(username, password):
            #session['user_info'] = username
            return redirect('/intro')
        else:
            return render_template('log.html', msg='用户名或密码错误')

@app.route('/intro')
def intro():
    return render_template('intro.html', user=username)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        # 处理表单提交
        global username
        username = request.form.get('username')
        password = request.form.get('password')
        Add_User(username, password)
        # 将新用户信息存入数据库
        return redirect('/log')

@app.route('/modify', methods=['GET', 'POST'])
def modify():
    if request.method == 'GET':
        return render_template('modify.html')
    else:
        # 处理表单提交
        global username
        pre_username = username
        username = request.form.get('username')
        password = request.form.get('password')
        Edit_User(username, password, pre_username)
        # 将新用户信息存入数据库
        return redirect('/intro')

@app.route('/tables')
def tables():
    global datas
    datas = Find_Data('小张')
    plot_url = Visualization()
    return render_template('tables.html', user=username, datas = datas, plot_url=plot_url)
    
    

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html', user=username)

# 运行应用
if __name__ == '__main__':
    app.run(debug=True,port=8080)