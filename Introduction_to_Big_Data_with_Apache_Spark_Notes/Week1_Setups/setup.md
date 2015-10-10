##安装环境
这门课程使用Vagrant搭建了一个虚拟开发环境,首先要装Vagrant.

由于网络环境问题,使用课程提供的Vagrantfile和vagrant up命令这个方法行不通,要手动下载package.box
```
axel https://atlas.hashicorp.com/sparkmooc/boxes/base2/versions/0.0.7.1/providers/virtualbox.box
```
然后
```
mkdir spark_vagrant && cd spark_vagrant
vagrant box add sparkmooc ../package.box
vagrant init sparkmooc
vagrant up
```
