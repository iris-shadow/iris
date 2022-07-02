// 封装缓动动画函数
function inching(element, endPoint, callback) {
    // 预先清除定时器的
    clearInterval(element.timer);
    // 给对象添加定时器
    element.timer = setInterval(function () {
        // 缓动公式 step = (endPoint - currentPoint) / 10 ，可以实现来回移动
        var step = (endPoint - element.offsetLeft) / 10;
        // 判断 step 正负后进行取整，使之准确达到结束点
        step = step > 0 ? Math.ceil(step) : Math.floor(step);
        // 判断是否到达结束点
        if (element.offsetLeft === endPoint) {
            // 清除定时器
            clearInterval(element.timer);
            // // 判断是否含有回调函数
            // if (callback) {
            //     callback();
            // }
            // 可利用与的短路实现
            callback && callback();
        }
        // 给对象的 left 加上 step
        element.style.left = element.offsetLeft + step + "px";
    }, 15);
}
