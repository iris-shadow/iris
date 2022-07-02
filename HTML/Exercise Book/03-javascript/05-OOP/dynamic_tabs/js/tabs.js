window.addEventListener('DOMContentLoaded', function () {
    // 使用面向对象的思想编写标签页功能
    // 属性：1. 标签栏   （1）文本框 （2）删除按钮 （3）新增按钮   2. 内容栏（文本框）
    // 功能：1. 切换标签（内容栏跟随切换）  2. 新增标签（内容栏跟随新增）  3. 修改标签（内容栏也需要）  4. 删除标签（内容栏跟随删除）

    var instance;
    class Tab {
        constructor() {
            instance = this;
            // 添加新增按钮属性
            this.newTabBtn = document.querySelector('.header .new-tab');
            // 新增按钮绑定新增标签的事件
            this.newTabBtn.onclick = this.newTab;
            this.init();
            document.addEventListener('selectstart', function (event) {
                event.preventDefault();
            });
        }

        // 初始化 该部分用于在结构内容发生改变时实时更新，为后续添加的元素绑定事件
        init() {
            // 添加删除按钮的属性
            this.deleteBtn = document.querySelectorAll('.header .tabs li i');
            // 删除按钮绑定删除的事件
            for (var i = 0; i < this.deleteBtn.length; i++) {
                this.deleteBtn[i].onclick = this.delete;
            }
            // 添加标签对应的内容框属性
            this.content = document.querySelector('.main .content');
            // 添加标签属性
            this.tabs = document.querySelector('.header .tabs');
            // 添加标签点击和双击的事件，内容框的双击事件
            for (var i = 0; i < this.tabs.children.length; i++) {
                // 为标签编号，方便后续的操作
                this.tabs.children[i].index = i;
                this.tabs.children[i].onclick = this.switch;
                this.tabs.children[i].ondblclick = this.modifyTab;
                this.content.children[i].ondblclick = this.modifyContent;
            }
        }

        // 清除样式
        clearClass() {
            for (var i = 0; i < instance.tabs.children.length; i++) {
                // 清除标签的样式
                instance.tabs.children[i].className = '';
                // 清除内容框的样式
                instance.content.children[i].className = '';
            }
        }

        // 切换标签
        switch() {
            // 调用清除样式的方法
            instance.clearClass();
            // 点击的按钮本身添加 .active
            this.className = 'active';
            // 点击按钮对应的内容框添加 .active
            instance.content.children[this.index].className = 'active';
        }

        // 新建标签
        newTab() {
            if (instance.tabs.children.length == 1) {
                instance.tabs.children[0].children[1].style.display = 'inline-block';
            }
            // 先调用清除样式的方法
            instance.clearClass();
            // 创建新标签和新标签对应的内容框
            var addTab = '<li class="active"><span>新标签页</span><i class="iconfont icon-delete"></i></li>';
            var addContent = '<li class="active"><div>每当我错过一个女孩，我就往山上搬一块砖，于是世界上就有了长城。</div></li>';
            // 将标签及内容框添加进对应的父元素中
            instance.tabs.insertAdjacentHTML('beforeend', addTab);
            instance.content.insertAdjacentHTML('beforeend', addContent);
            // 进行初始化，获取最新的节点并绑定事件
            instance.init();
        }

        // 修改标签
        modifyTab() {
            // 获取当前标签页第一个子元素的内容
            var text = this.children[0].innerHTML || this.children[0].value;
            //  先删除当前标签页的第一子个元素
            this.removeChild(this.children[0]);
            // 添加一个文本框到被删除的第一个子元素的位置
            this.insertAdjacentHTML('afterbegin', '<input type="text" value=' + text + '>');
            // 默认选择文本框中的文字
            this.children[0].select();
            // 当输入框失去焦点时，重新加回原来第一个子元素，删除文本框并将其值赋值到原来的第一个子元素中
            this.children[0].addEventListener('blur', function () {
                this.parentNode.insertAdjacentHTML('afterbegin', '<span>' + this.value + '</span>');
                this.remove();
            });
            // 按下回车键时执行和失去焦点的同样操作
            this.children[0].addEventListener('keyup', function (event) {
                if (event.keyCode == 13) {
                    this.parentNode.insertAdjacentHTML('afterbegin', '<span>' + this.value + '</span>');
                    this.remove();
                }
            });
        }

        // 修改内容框
        modifyContent() {
            // 获取当前内容框的内容
            var text = this.children[0].innerHTML;
            //  先删除当前内容框的第一子个元素
            this.removeChild(this.children[0]);
            // 添加一个文本域到内容框
            this.insertAdjacentHTML('afterbegin', '<textarea name="" id="" maxlength="-1">' + text + '</textarea>');
            // 默认选择文本框中的文字
            this.children[0].select();
            // 当输入框失去焦点时，重新加回原来第一个元素，删除文本域并将其值赋值到第一个子元素中
            this.children[0].addEventListener('blur', function () {
                this.parentNode.insertAdjacentHTML('afterbegin', '<div>' + this.value + '</div>');
                this.remove();
            });
            // 按下回车键时执行和失去焦点的同样操作
            this.children[0].addEventListener('keyup', function (event) {
                if (event.keyCode == 13) {
                    this.parentNode.insertAdjacentHTML('afterbegin', '<div>' + this.value + '</div>');
                    this.remove();
                }
            });
        }

        // 删除标签
        delete(event) {
            // 阻止标签切换的冒泡事件
            event.stopPropagation();
            // 获取当前删除按钮对应标签页的序号
            var index = this.parentNode.index;
            // 删除当前删除按钮对应的标签页
            this.parentNode.remove();
            // 删除被删除的标签页对应的内容框
            instance.content.children[index].remove();
            // 序号 -1 ，用于选取当前标签页的前一个标签页
            index--;
            // 若只剩于一个便签页，则将其关闭按钮隐藏
            if (instance.tabs.children.length == 1) {
                instance.tabs.children[0].children[1].style.display = 'none';
            }
            // 进行初始化，重新编排标签序号，确保标签号与子元素对应
            instance.init();
            // 若删除的元素不是选中元素，则不选中删除标签页的前一个标签页
            if (document.querySelector('.tabs li.active')) {
                return;
            }
            // 选中当前标签页（被删除的标签页）的上一个标签页
            instance.tabs.children[index].onclick();
        }
    }

    new Tab();
});
