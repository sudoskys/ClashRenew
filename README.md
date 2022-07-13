# ClashRenew

Linux clash或clash-meta 配置-config.yaml 自动更新小脚本，使用前请审计代码。


**使用本项目造成的后果需使用者负责。**


## 安装

克隆本项目后请移动文件到 ```～/``` （HOME）目录

#### 依赖

```pip install pyyaml==5.4.1```

>因为 yaml 库的兼容问题，需要使用 5.4.1，如果不是可以使用 ```pip unstall```



### 配置开机自动

-------

最好不要使用```.zshrc```或者```.bashrc```，会产生打开终端就执行的问题...

**运行如下来开机自动启动clash**
```
systemctl --user enable clash.service
systemctl --user start clash.service
systemctl --user status clash.service
```

**复制cron.sh**
```
sudo cp ~/cron.sh  /usr/local/bin
```

这里修正了教程的误导，采用**登陆账户**，而不是系统全开clash.

```
cd /usr/lib/systemd/user/
sudo vim clashrenew.service


```


**填入**
```
[Unit]
Description=clashRenew
After=network-online.target

[Service]
Type=simple
Restart=on-abort
ExecStart=sh /usr/local/bin/cron.sh
ExecStartPre=/bin/sleep 10

[Install]
WantedBy=default.target

```

**启动 clashrenew 程序**
```
systemctl --user enable clashrenew.service
systemctl --user start clashrenew.service
systemctl --user status clashrenew.service
```

这样用户自定义服务就可以运行起来了

PS:ExecStartPre=/bin/sleep 20 代表延迟20秒，也可以修改clash的服务,使其延迟启动（如果你是无线链接）

本人 clash.service 举例！（适用于启动成功但io超时）
```
[Unit]
Description=A rule based proxy in Go.
After=network-online.target

[Service]
Type=exec
Restart=on-abort
ExecStart=/usr/bin/clash
ExecStartPre=/bin/sleep 15

[Install]
WantedBy=default.target
```

Ps:至于 network ，见https://access.redhat.com/documentation/zh-cn/red_hat_enterprise_linux/8/html/configuring_and_managing_networking/systemd-network-targets-and-services_configuring-and-managing-networking

*部分参考此教程*
https://blog.linioi.com/posts/clash-on-arch/


重载配置 ```systemctl --user daemon-reload```


### 程序配置文件示例

注意空格
```
RenewConfig: True
RenewTargetKey: cloud22
content:
   cloud1:
       - https://
   cloud22:
       - https://

```

```RenewConfig``` 指是否替换运行依赖的config,```RenewTargetKey```指替换的目标（必须在列表里）




编辑 python 脚本，按照注释配置 配置文件名称 和 数据目录。
