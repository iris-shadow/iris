$(function () {
    // 克隆监控记录重复添加，实现无缝滚动的效果
    // 使用循环是因为存在两个 .marquee 元素
    $('.marquee').each(function () {
        var children = $(this).children().clone();
        $(this).append(children);
    });

    // 为 .monitor .tabs a 注册点击事件
    $('.monitor .tabs').on('click', 'a', function () {
        $(this).addClass('active').siblings().removeClass('active');
        $('.monitor .content').eq($(this).index()).css('display', 'block').siblings('.content').css('display', 'none');
    });

    // 使用立即函数制作每个图表，避免变量名的污染

    // 定义一个让图标大小跟随浏览器大小变化的函数
    function resize(chart) {
        window.addEventListener('resize', function () {
            chart.resize();
        });
    }

    //
    // 饼图（点位分布统计）
    //

    (function () {
        // 初始化 echarts
        var pie = echarts.init(document.querySelector('.pie'));

        // 配置选项和数据
        var option = {
            tooltip: {
                trigger: 'item',
                backgroundColor: 'rgba(0, 0, 0, 0.5)',
                formatter: '{a} <br/>{b} : {c} ({d}%)',
                borderWidth: 0,
                textStyle: {
                    color: '#fff',
                },
            },
            color: ['#006cff', '#60cda0', '#ed8884', '#ff9f7f', '#0096ff', '#9fe6b8', '#32c5e9', '#1d9dff'],
            series: [
                {
                    name: '点位统计',
                    type: 'pie',
                    radius: ['10%', '70%'],
                    center: ['50%', '50%'],
                    roseType: 'radius',
                    data: [
                        { value: 20, name: '云南' },
                        { value: 26, name: '北京' },
                        { value: 24, name: '山东' },
                        { value: 25, name: '河北' },
                        { value: 20, name: '江苏' },
                        { value: 25, name: '浙江' },
                        { value: 30, name: '四川' },
                        { value: 42, name: '湖北' },
                    ],
                    // 文字
                    label: {
                        fontSize: 10,
                        color: 'inherit',
                        overflow: 'none',
                    },
                    // 引线
                    labelLine: {
                        length: 6,
                        length2: 4,
                    },
                },
            ],
        };
        // 将选项和数据传给 pie
        pie.setOption(option);

        // 跟随浏览器大小变化
        resize(pie);
    })();

    //
    // 条形图（全国用户总量）
    //

    (function () {
        var bar = echarts.init(document.querySelector('.bar'));

        // series.data 省略项
        var elliptical = {
            name: '',
            value: 1200,
            itemStyle: {
                color: '#254065',
            },
            emphasis: {
                itemStyle: {
                    color: '#254065',
                },
            },
            tooltip: {
                extraCssText: 'opacity: 0',
            },
        };

        var option = {
            // 图表大小
            grid: {
                show: true,
                top: '3%',
                right: '3%',
                bottom: '3%',
                left: '0%',
                containLabel: true,
                borderColor: 'rgba(0, 240, 255, 0.3)',
            },
            // 提示框
            tooltip: {
                trigger: 'item',
                backgroundColor: 'rgba(0, 0, 0, 0.5)',
                axisPointer: {
                    type: '',
                },
                borderWidth: 0,
                textStyle: {
                    color: '#fff',
                },
            },
            // 图表颜色
            color: {
                type: 'linear',
                x: 0,
                y: 0,
                x2: 0,
                y2: 1,
                colorStops: [
                    {
                        offset: 0,
                        color: '#00fffb',
                    },
                    {
                        offset: 1,
                        color: '#0061ce',
                    },
                ],
                globalCoord: false,
            },
            xAxis: {
                type: 'category',
                // 标签刻度
                axisTick: {
                    show: false,
                    alignWithLabel: false,
                },
                // 标签文字
                axisLabel: {
                    color: '#4c9bfd',
                },
                // x 轴
                axisLine: {
                    lineStyle: {
                        color: 'rgba(0, 240, 255, 0.3)',
                    },
                },
                data: ['上海', '广州', '北京', '深圳', '合肥', '', '......', '', '杭州', '厦门', '济南', '成都', '重庆'],
            },
            yAxis: {
                type: 'value',
                // 标签刻度
                axisTick: {
                    show: false,
                },
                // 标签文字
                axisLabel: {
                    color: '#4c9bfd',
                },
                // y 轴
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: 'rgba(0, 240, 255, 0.3)',
                    },
                },
                // 分割线
                splitLine: {
                    lineStyle: {
                        color: 'rgba(0, 240, 255, 0.3)',
                    },
                },
            },
            series: [
                {
                    type: 'bar',
                    barWidth: '60%',
                    data: [2100, 1900, 1700, 1560, 1400, elliptical, elliptical, elliptical, 900, 750, 600, 480, 240],
                },
            ],
        };

        bar.setOption(option);

        window.addEventListener('resize', bar.resize);
    })();

    //
    // order
    //

    // 注册点击事件
    $('.order .tabs').on('click', 'a', function () {
        // 准备数据
        var data = [
            {
                orderQuantity: '20,301,987',
                sale: '99843',
            },
            {
                orderQuantity: '21,987',
                sale: '9843',
            },
            {
                orderQuantity: '1,987',
                sale: '843',
            },
            {
                orderQuantity: '987',
                sale: '33',
            },
        ];
        // 更改点击元素样式
        $(this).addClass('active').siblings('a').removeClass('active');
        // 更换销售量
        $('.order .data .item').eq(0).children('h4').html(data[$(this).index()].orderQuantity);
        // 更换销售额
        $('.order .data .item').eq(1).children('h4').html(data[$(this).index()].sale);
    });

    //
    // 折线图（销售额统计）
    //

    (function () {
        // 准备数据
        var data = {
            year: [
                [24, 40, 101, 134, 90, 230, 210, 230, 120, 230, 210, 120],
                [40, 64, 191, 324, 290, 330, 310, 213, 180, 200, 180, 79],
            ],
            season: [
                [23, 75, 12, 97, 21, 67, 98, 21, 43, 64, 76, 38],
                [43, 31, 65, 23, 78, 21, 82, 64, 43, 60, 19, 34],
            ],
            month: [
                [34, 87, 32, 76, 98, 12, 32, 87, 39, 36, 29, 36],
                [56, 43, 98, 21, 56, 87, 43, 12, 43, 54, 12, 98],
            ],
            week: [
                [43, 73, 62, 54, 91, 54, 84, 43, 86, 43, 54, 53],
                [32, 54, 34, 87, 32, 45, 62, 68, 93, 54, 54, 24],
            ],
        };

        var line = echarts.init(document.querySelector('.line'));

        var option = {
            tooltip: {
                trigger: 'axis',
            },
            legend: {
                textStyle: {
                    color: '#4c9bfd',
                },
                right: '10%',
            },
            grid: {
                top: '20%',
                right: '4%',
                left: '3%',
                bottom: '3%',
                show: true,
                borderColor: '#012f4a',
                containLabel: true,
            },
            color: ['#00f2f1', '#ed3f35'],
            xAxis: {
                type: 'category',
                boundaryGap: false,
                data: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
                axisTick: {
                    show: false,
                },
                axisLabel: {
                    color: '#4c9bfd',
                },
                axisLine: {
                    show: false,
                },
            },
            yAxis: {
                type: 'value',
                axisTick: {
                    show: false,
                },
                axisLabel: {
                    color: '#4c9bfd',
                },
                splitLine: {
                    lineStyle: {
                        color: '#012f4a',
                    },
                },
            },
            series: [
                {
                    name: '预期销售额',
                    type: 'line',
                    stack: '总量',
                    smooth: true,
                    data: data.year[0],
                },
                {
                    name: '实际销售额',
                    type: 'line',
                    stack: '总量',
                    smooth: true,
                    data: data.year[1],
                },
            ],
        };

        line.setOption(option);

        // 注册点击事件
        $('.statistic .tabs').on('click', 'a', function () {
            index = $(this).index();
            $(this).addClass('active').siblings('a').removeClass('active');

            // 获取自定义属性 data-type 来决定显示哪个数据
            var type = $(this).attr('data-type');
            option.series[0].data = data[type][0];
            option.series[1].data = data[type][1];
            // 重新设置 line 的数据
            line.setOption(option);
        });

        // 自动播放 tabs 栏
        var index = 0;
        var timer = setInterval(function () {
            $('.statistic .tabs a').eq(index).click();
            index++;
            index %= $('.statistic .tabs a').length;
        }, 1000);

        // 鼠标进入和离开
        $('.statistic .tabs').hover(
            function () {
                clearInterval(timer);
            },
            function () {
                timer = setInterval(function () {
                    $('.statistic .tabs a').eq(index).click();
                    index++;
                    index %= $('.statistic .tabs a').length;
                }, 1000);
            }
        );

        resize(line);
    })();

    //
    // 雷达图（渠道分布）
    //

    (function () {
        var radar = echarts.init(document.querySelector('.radar'));

        var option = {
            radar: {
                shape: 'circle',
                center: ['50%', '50%'],
                radius: '65%',
                splitNumber: 4,
                splitLine: {
                    lineStyle: {
                        color: 'rgba(255,255,255, 0.5)',
                    },
                },
                splitArea: {
                    show: false,
                },
                axisLine: {
                    lineStyle: {
                        color: 'rgba(255,255,255, 0.5)',
                    },
                },
                name: {
                    textStyle: {
                        color: '#4c9bfd',
                    },
                },
                indicator: [
                    { name: '机场', max: 100 },
                    { name: '商场', max: 100 },
                    { name: '火车站', max: 100 },
                    { name: '汽车站', max: 100 },
                    { name: '地铁', max: 100 },
                ],
            },
            tooltip: {
                show: true,
                position: ['60%', '10%'],
                borderWidth: 0,
                backgroundColor: 'rgba(0,0,0, 0.5)',
                textStyle: {
                    color: '#fff',
                },
            },
            series: [
                {
                    name: '北京',
                    type: 'radar',
                    areaStyle: {
                        color: 'rgba(238, 197, 102, 0.6)',
                    },
                    lineStyle: {
                        color: '#fff',
                        width: 1,
                    },
                    symbol: 'circle',
                    symbolSize: 5,
                    itemStyle: {
                        color: '#fff',
                    },
                    label: {
                        show: true,
                        color: '#fff',
                        fontSize: 10,
                    },
                    data: [[90, 19, 56, 11, 34]],
                },
            ],
        };

        radar.setOption(option);

        resize(radar);
    })();

    //
    // 饼图（一季度销售进度）
    //

    (function () {
        var gauge = echarts.init(document.querySelector('.gauge'));

        var option = {
            series: [
                {
                    name: '销售进度',
                    type: 'pie',
                    radius: ['130%', '150%'],
                    center: ['48%', '80%'],
                    label: {
                        show: false,
                    },
                    emphasis: {
                        label: {
                            show: false,
                        },
                    },
                    startAngle: 180,
                    hoverOffset: 0,
                    labelLine: {
                        show: false,
                    },
                    data: [
                        {
                            value: 1,
                            itemStyle: {
                                //     color: {
                                //         type: 'linear',
                                //         x: 0,
                                //         y: 0,
                                //         x1: 0,
                                //         y2: 1,
                                //         colorStops: [
                                //             {
                                //                 offset: 0,
                                //                 color: '#00c9e0',
                                //             },
                                //             {
                                //                 offset: 1,
                                //                 color: '#005fc1',
                                //             },
                                //         ],
                                //         global: false,
                                //     },
                                color: new echarts.graphic.LinearGradient(
                                    // (x1,y2) 点到点 (x2,y2) 之间进行渐变
                                    0,
                                    0,
                                    0,
                                    1,
                                    [
                                        { offset: 0, color: '#00c9e0' }, // 0 起始颜色
                                        { offset: 1, color: '#005fc1' }, // 1 结束颜色
                                    ]
                                ),
                            },
                        },
                        {
                            value: 1,
                            itemStyle: {
                                color: '#12274d',
                            },
                        },
                        { value: 2, itemStyle: { color: 'transparent' } },
                    ],
                },
            ],
        };

        gauge.setOption(option);

        resize(gauge);
    })();

    //
    // 排行榜
    //

    (function () {
        // 准备数据
        var data = [
            {
                city: '北京',
                sales: '25, 179',
                flag: true,
                brands: [
                    //  品牌种类数据
                    { name: '可爱多', num: '9,086', flag: true },
                    { name: '娃哈哈', num: '8,341', flag: true },
                    { name: '喜之郎', num: '7,407', flag: false },
                    { name: '八喜', num: '6,080', flag: false },
                    { name: '小洋人', num: '6,724', flag: false },
                    { name: '好多鱼', num: '2,170', flag: true },
                ],
            },
            {
                city: '河北',
                sales: '23,252',
                flag: false,
                brands: [
                    { name: '可爱多', num: '3,457', flag: false },
                    { name: '娃哈哈', num: '2,124', flag: true },
                    { name: '喜之郎', num: '8,907', flag: false },
                    { name: '八喜', num: '6,080', flag: true },
                    { name: '小洋人', num: '1,724', flag: false },
                    { name: '好多鱼', num: '1,170', flag: false },
                ],
            },
            {
                city: '上海',
                sales: '20,760',
                flag: true,
                brands: [
                    { name: '可爱多', num: '2,345', flag: true },
                    { name: '娃哈哈', num: '7,109', flag: true },
                    { name: '喜之郎', num: '3,701', flag: false },
                    { name: '八喜', num: '6,080', flag: false },
                    { name: '小洋人', num: '2,724', flag: false },
                    { name: '好多鱼', num: '2,998', flag: true },
                ],
            },
            {
                city: '江苏',
                sales: '23,252',
                flag: false,
                brands: [
                    { name: '可爱多', num: '2,156', flag: false },
                    { name: '娃哈哈', num: '2,456', flag: true },
                    { name: '喜之郎', num: '9,737', flag: true },
                    { name: '八喜', num: '2,080', flag: true },
                    { name: '小洋人', num: '8,724', flag: true },
                    { name: '好多鱼', num: '1,770', flag: false },
                ],
            },
            {
                city: '山东',
                sales: '20,760',
                flag: true,
                brands: [
                    { name: '可爱多', num: '9,567', flag: true },
                    { name: '娃哈哈', num: '2,345', flag: false },
                    { name: '喜之郎', num: '9,037', flag: false },
                    { name: '八喜', num: '1,080', flag: true },
                    { name: '小洋人', num: '4,724', flag: false },
                    { name: '好多鱼', num: '9,999', flag: true },
                ],
            },
        ];

        // 填充 .province 中的数据
        $.each(data, function (index, elem) {
            var flag = elem.flag == true ? 'icon-up' : 'icon-down';
            var li = $(`<li><span>${elem.city}</span><span>${elem.sales} <i class="${flag}"></i></span></li>`);
            $('.hot-cakes .province').append(li);
        });

        // 填充 .detail 中的数据
        function fill(index) {
            $('.hot-cakes .province li').eq(index).addClass('active').siblings('li').removeClass('active');

            $('.hot-cakes .detail').empty();
            $.each(data[index].brands, function (index, elem) {
                var flag = elem.flag == true ? 'icon-up' : 'icon-down';
                var li = $(`<li><span>${elem.name}</span><span>${elem.num}<i class="${flag}"></i></span></li>`);
                $('.hot-cakes .detail').append(li);
            });
        }

        // 注册鼠标经过事件
        $('.hot-cakes .province').on('mouseenter', 'li', function () {
            // 更改自动轮播的序号
            index = $(this).index();
            // 更换 .detail 中的数据
            fill(index);
        });

        // 刷新时显示数据
        $('.hot-cakes .province li').eq(0).mouseenter();

        // 自动播放销售热榜的数据
        var index = 0;
        var timer = setInterval(function () {
            fill(index);
            index++;
            index %= $('.hot-cakes .province li').length;
        }, 2000);

        $('.hot-cakes .province').hover(
            function () {
                clearInterval(timer);
            },
            function () {
                timer = setInterval(function () {
                    fill(index);
                    index++;
                    index %= $('.hot-cakes .province li').length;
                }, 2000);
            }
        );
    })();
});
