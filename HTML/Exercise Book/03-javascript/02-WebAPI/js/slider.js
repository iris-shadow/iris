// 添加 load 事件，等待页面加载完毕才执行
window.addEventListener("load", function () {
    var focus = this.document.querySelector(".focus");
    var slider = this.document.querySelector(".slider");
    var arrowLeft = this.document.querySelector(".arrow-left");
    var arrowRight = this.document.querySelector(".arrow-right");
    var dots = this.document.querySelector(".dots");

    // 声明一个记录鼠标点击次数的 counter
    var counter = 0;
    // 声明一个记录 dot 索引号的 dotIndex
    var currentIndex = 0;

    // 定义一个选中当前 dot 后清除其它 dot 样式的函数
    function select() {
        // 预先清除所有 dot 的样式
        for (var i = 0; i < dots.children.length; i++) {
            dots.children[i].className = "";
        }
        // 根据 counter 选择 dot 并添加选中样式
        dots.children[currentIndex].className = "current-dot";
    }

    // 1. 给左右箭头添加鼠标滑入 focus 显示，离开隐藏的事件
    // 使用 mouseenter 和 mouseleave 事件更合适；使用 mouseover 和 mouseout 时，向左右滑开鼠标可能会无法隐藏按钮（有冒泡）
    focus.addEventListener("mouseenter", function () {
        arrowLeft.style.display = "block";
        arrowRight.style.display = "block";

        // 清除自动调用轮播效果的定时器
        clearInterval(timer);
        timer = null;
    });

    // 离开隐藏
    focus.addEventListener("mouseleave", function () {
        arrowLeft.style.display = "none";
        arrowRight.style.display = "none";

        //重新打开定时器
        timer = setInterval(function () {
            arrowRight.click();
        }, 2000);
    });

    // 2. 根据 slider 中的 li 元素个数给 dots 中添加相应的 li 元素
    for (var i = 0; i < slider.children.length; i++) {
        var dot = this.document.createElement("li");

        // 给 dots 中的 li 元素添加自定义属性 data-index 。以便后续获取其索引号
        dot.setAttribute("data-index", i);

        // 将 dot 添加进 dots
        dots.appendChild(dot);

        // 调用 dot 选中样式
        select();

        // 为每个 dot 注册鼠标滑入后自身被选中（排他思想），轮播图滚动的事件
        dot.addEventListener("mouseenter", function () {
            for (var i = 0; i < dots.children.length; i++) {
                dots.children[i].className = "";
            }
            // 将自身的添加选择后的类名
            this.className = "current-dot";

            // 切换轮播图，利用元素的索引号 * focus 的宽度即为要 slider 移动的距离（负值）
            currentIndex = this.getAttribute("data-index");
            // 将要移动的元素和结束位置传到缓动函数
            inching(slider, -(currentIndex * focus.offsetWidth), function () {
                // 解除按钮禁用，防止在点击按钮时，按钮调用的缓动函数还没结束就在滑入小圆点时重新调用缓动函数中断了按钮的缓动函数，导致按钮禁用没有解除
                arrowLeft.disabled = false;
                arrowRight.disabled = false;
            });

            // 将 counter 与 currentIndex同步
            counter = currentIndex;
        });
    }

    // 克隆第一张轮播图到最后，实现轮播图的无缝衔接
    // 若不克隆第一张轮播图到最后，当播放到最后一张时，连续点击按钮会出现轮播图次序对不上小圆点顺序的情况
    // 可使用点击时禁用按钮和缓动函数的回调函数的解除禁用解决
    var lastSlider = slider.children[0].cloneNode(true);
    slider.appendChild(lastSlider);
    slider.style.width = focus.offsetWidth * slider.children.length + "px";

    // 3. 给左右按钮注册点击切换轮播图的事件
    // 左侧按钮
    arrowLeft.addEventListener("click", function () {
        // 禁用按钮，防止多次点击
        arrowLeft.disabled = true;

        // 判断是否到达第一张轮播图
        // 使用 “==” 连接，因为下圆点的索引号是字符类型
        // 在赋值给 counter 后，若使用 “===” 会在点击第一个小圆点再点击左侧按钮后出现问题
        if (counter == 0) {
            // 点击次数改为轮播图个数 - 1
            counter = slider.children.length - 1;
            // 预先快速定位到克隆的第一张轮播图（最后一张），然后往下再调用缓动函数
            slider.style.left = -focus.offsetWidth * counter + "px";
        }

        // 点击次数 - 1
        counter--;
        // 将要移动的元素和结束位置传到缓动函数
        inching(slider, -(counter * focus.offsetWidth), function () {
            // 当缓动完成后再接触按钮禁用
            arrowLeft.disabled = false;
        });

        // 小圆点 -1
        currentIndex--;
        // 判断是否超出小圆点的索引号
        currentIndex = currentIndex < 0 ? dots.children.length - 1 : currentIndex;

        // 选中对应的 dot
        select();
    });

    // 右侧按钮
    arrowRight.addEventListener("click", function () {
        // 禁用按钮，防止多次点击
        arrowRight.disabled = true;

        // 判断是否到达克隆的第一张轮播图(最后一张)
        if (counter == slider.children.length - 1) {
            counter = 0;
            slider.style.left = "0";
        }

        // 点击次数 + 1
        counter++;
        // 将要移动的元素和结束位置传到缓动函数
        inching(slider, -counter * focus.offsetWidth, function () {
            // 当缓动完成后再接触按钮禁用
            arrowRight.disabled = false;
        });

        // 小圆点 + 1
        currentIndex++;
        // 判断小圆点是否到达最后一张轮播图（倒数第二张，不是克隆的第一张）
        currentIndex = counter == dots.children.length ? 0 : currentIndex;

        // 选中对应的 dot
        select();
    });

    // 自动调用轮播效果
    var timer = setInterval(function () {
        arrowRight.click();
    }, 2000);
});
