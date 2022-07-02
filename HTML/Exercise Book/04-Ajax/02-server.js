// 引入 express
const { response } = require('express');
const express = require('express');

// 实例化对象
const app = express();

// 设置路由
app.get('/server', (request, response) => {
    // 设置响应头 允许跨域
    response.setHeader('Access-Control-Allow-Origin', '*');

    // 设置响应体
    response.send('Hello Ajax!(GET)');
});

app.post('/server', (request, response) => {
    // 设置响应头 允许跨域
    response.setHeader('Access-Control-Allow-Origin', '*');
    // 允许设置非预定义（自定义）的请求头
    response.setHeader('Access-Control-Allow-Headers', '*');

    // 设置响应体
    const data = {
        name: 'iris',
    };

    let str = JSON.stringify(data);
    response.send(str);
});

// 允许所有请求方式
app.all('/server', (request, response) => {
    // 设置响应头 允许跨域
    response.setHeader('Access-Control-Allow-Origin', '*');
    response.setHeader('Access-Control-Allow-Headers', '*');

    // 设置响应体
    response.send('Hello Ajax!(POST)');
});

// 延时模拟
app.get('/delay', (request, response) => {
    // 设置响应头 允许跨域
    response.setHeader('Access-Control-Allow-Origin', '*');
    // 设置响应体
    // 延时 3s 发送
    setTimeout(() => {
        response.send('您的浏览器太垃圾，不配访问我！');
    }, 3000);
});

// 取消模拟
app.get('/cancel', (request, response) => {
    // 设置响应头 允许跨域
    response.setHeader('Access-Control-Allow-Origin', '*');

    // 设置响应体
    setTimeout(() => {
        response.send('你这网络不保熟呀 。。。');
    }, 5000);
});

// jQuery Ajax
app.all('/jQuery-server', (request, response) => {
    // 设置响应头 允许跨域
    response.setHeader('Access-Control-Allow-Origin', '*');
    response.setHeader('Access-Control-Allow-Headers', '*');

    let data = { name: '一叶秋' };
    // 设置响应体
    setTimeout(() => {
        response.send(JSON.stringify(data));
    }, 900);
});

app.all('/jQuery-jsonp', (request, response) => {
    const data = {
        exist: true,
        msg: '用户名已经存在。',
    };

    let callback = request.query.callback;

    let str = JSON.stringify(data);

    response.end(`${callback}(${str})`);
});

// 启动监听服务
app.listen(8000, () => {
    console.log('服务已启动，8000 端口监听中 。。。');
});
