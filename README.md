# blog_backend 

## 项目介绍

这是一个以 Django 为框架搭建的 web 后端，是根据本人之前的四十余篇 Django 笔记形成的一个博客系统

其中，会涉及到数据库、Redis、ES 等及其对应的使用，还会包括系统方面的中间件、日志、异常处理等系统功能

当前使用的 Python 版本是 3.8

Django 版本是 3.2

## 项目启动流程

1. git clone 下对应的代码
2. 修改 blog_backend/envs/ 文件夹下对应的环境变量
3. 安装依赖 pip3 install -r requirements.txt，如果安装太慢，可以换源安装
4. cd blog_backend 到系统的根目录下
5. 执行 python3 manage.py migrate 执行数据库迁移操作
6. 执行 python3 manage.py runserver 0.0.0.0:9898 启动系统


## 项目更新当前进度

1. 系统的创建与运行

## 关于 Django 笔记

关于之前的更新的四十余篇 Django 笔记，是本人根据 Django 的官方文档逐个翻译整理出来的笔记

如果想了解，可以搜索微信公众号: Hunter后端

欢迎交流。
