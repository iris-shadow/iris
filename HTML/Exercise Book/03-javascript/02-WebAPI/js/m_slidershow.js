window.addEventListener("load", function () {
    // foucs 元素
    var focus = this.document.querySelector(".focus");
    // ul 元素
    var slider = focus.children[0];
    // ol 元素
    var dots = focus.children[1];

    //
    // 根据 slider 中的元素个数来创建小圆点
    for (var i = 0; i < slider.children.length; i++) {
        var dot = this.document.createElement("li");
        dots.appendChild(dot);
    }
    // 给第一个小圆点加上 current 类
    dots.children[0].classList.add("current");

    //
    // 克隆第一张排到最后，克隆最后一张排到最前
    var cloneFirst = slider.children[0].cloneNode(true);
    var cloneLast = slider.children[slider.children.length - 1].cloneNode(true);
    slider.appendChild(cloneFirst);
    slider.insertBefore(cloneLast, slider.children[0]);
    // 更改 slider 宽度
    slider.style.width = slider.children.length * 100 + "%";
    // 更改 slider 内每个轮播图的宽度
    for (var i = 0; i < slider.children.length; i++) {
        slider.children[i].style.width = (100 / slider.children.length).toFixed(4) + "%";
    }

    //
    // 声明记录 focus 宽度的 focusWidth
    var focusWidth = focus.offsetWidth;
    // 声明记录 slider 当前位置的 index
    var index = 0;

    //
    // 封装一个计算轮播图位移的函数
    function calcInterval(transitStatus, duration) {
        // 是否需要过渡
        if (transitStatus) {
            slider.style.transition = "all " + duration + "s";
        } else {
            slider.style.transition = "none";
        }
        // 求取 slider 的位移
        var displacement = -index * focusWidth;
        slider.style.transform = "translateX(" + displacement + "px)";
    }

    //
    // 封装一个开启定时器实现轮播图的自动播放的函数
    var timer = null;
    function setTimer() {
        timer = this.setInterval(function () {
            // slider 位置 + 1
            index++;
            // 调用 calcInterval 进行轮播
            calcInterval(true, 0.6);
        }, 2000);
    }
    // 开启定时器
    setTimer();

    //
    // 在使用 transitioned 事件，在动画结束后判断 slider 当前位置以及调整对应小圆点的样式
    slider.addEventListener("transitionend", function () {
        // 是否到达最后一张
        // 使用 == 操作，在离开页面时会出现无限移动的情况
        if (index >= slider.children.length - 2) {
            index = 0;
        }
        // 是否到达第一张
        else if (index < 0) {
            index = slider.children.length - 3;
        }

        // 调用 calcInterval 进行轮播
        calcInterval(false);

        // 调整对应小圆点的样式
        // 使用 element.classList.remove(className) 移除前一个的 .current 类名
        dots.querySelector(".current").classList.remove("current");
        // 使用 element.classList.add(className) 在对应的小圆点加上 .current 类名
        dots.children[index].classList.add("current");
    });

    //
    // 手指拖动时滑动轮播图
    // 声明记录手指按下时的 originX 和移动距离 distanceX
    var originX = 0;
    var distanceX = 0;

    // 使用 touchstart 事件记录手指按下的 originX
    slider.addEventListener("touchstart", function (event) {
        // 获取手指按下时的 originX
        originX = event.targetTouches[0].pageX;
        // 按下时清除定时器
        clearInterval(timer);
    });

    // 使用 touchmove 事件使 slider 跟随手指移动
    slider.addEventListener("touchmove", function (event) {
        // 获取移动后的 distinationX
        var distinationX = event.targetTouches[0].pageX;
        // 获取移动的距离
        distanceX = distinationX - originX;
        // 清除动画过渡
        slider.style.transition = "none";
        // slider 的移动距离 = dsitanceX + slider 当前位置
        var displacement = -index * focusWidth + distanceX;
        slider.style.transform = "translateX(" + displacement + "px)";
        // 阻止滚动屏幕的行为
        event.preventDefault();
    });

    // 使用 touchend 事件判断手指移动的距离进而决定播放哪张轮播图
    slider.addEventListener("touchend", function () {
        // 判断手指移动距离是否大于  50px
        if (Math.abs(distanceX) > 50) {
            if (distanceX > 0) {
                index--;
            } else {
                index++;
            }
            // 调用 calcInterval 进行轮播
            calcInterval(true, 0.6);
        } else {
            // 调用 calcInterval 进行轮播
            calcInterval(true, 0.3);
        }

        // 开启定时器
        // 预先清除定时器，防止添加多个
        clearInterval(timer);
        setTimer();
    });
});
