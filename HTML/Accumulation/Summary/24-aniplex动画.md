# 思路

1. 所以字母使用一个 div 盒子，动画设置为围绕 Y 轴 3D 旋转，opacity 右 0 渐变为 1
2. 外边框另用一个 div 盒子制作，用定位全部叠加到一起，然后移到最左边。使用动画设置为沿着 X 到字母的相应位置，移动过程中加上围绕 Y 轴旋转

# 注意点

-   在沿 Y 轴旋转 90deg 时，只有旋转的元素在原地（没有位移）时，才能隐藏，若发生移动则能看到元素。此案例的中间字母用到该注意点
