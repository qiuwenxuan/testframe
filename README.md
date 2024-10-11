# 自动化测试框架

#### 介绍
本自动化测试框架采用python + unittest 的基础来搭建，采用PO模式、数据驱动的思想，通过selenium来实现WEB UI自动化，通过request来实现接口自动化。移动终端的自动化也可在该框架基础上去构建补充。



本框架主要用于大家练手，熟悉企业真实测试框架中的自动化思想、技术点。



目前本工程，是**可以直接运行**的，运行main.py即可，前提是各种库已经安装好。



本工程调试通过的**python版本为3.10**。



具体请参考：

 [从零搭建完整python自动化测试框架（UI自动化和接口自动化 ）——持续更新_霸蛮哥的博客-CSDN博客](https://blog.csdn.net/sunjice/article/details/114790746) 



#### 注意事项

1. 本目录下的requerments.txt，里面收录了 需要安装的依赖库，请提前安装；
2. 注意更换配置文件[**conf/config.ini**]中的邮箱相关配置；
3. 更换[**testcase/API/Case/baidu.py**]中的 **app_id、app_key**。

