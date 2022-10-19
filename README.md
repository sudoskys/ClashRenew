# ClashRenew

自动备份配置列表中网址的数据并写入特定文件。

在 **不采用proxy provider的情况下** 实现 Linux clash或clash-meta 配置-config.yaml 的自动更新。

使用前请先看一下代码。


Ps: 你也可以使用 Clash proxy-provider




## 安装

克隆本项目后请移动文件到 ```～/``` （HOME）目录

#### 依赖

```bash
pip install requirements.txt
```



>因为 yaml 库的兼容问题，配置写了需要使用 5.4.1 以上的库

### 覆写

在脚本数据目录（默认为 `Clash`） 下有一个 `.template.yaml` ，里面写东西就能合并进去

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

`clash.service` 举例 （适用于启动成功但io超时）

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

这里可以换成 `clash-meta`

**注意： ```After=network-online.target``` 有适配问题，请注意！**

Ps:至于 network ，见https://access.redhat.com/documentation/zh-cn/red_hat_enterprise_linux/8/html/configuring_and_managing_networking/systemd-network-targets-and-services_configuring-and-managing-networking

*部分参考此教程*
https://blog.linioi.com/posts/clash-on-arch/


重载配置 ```systemctl --user daemon-reload```


### 程序配置文件示例

注意空格
```
RenewConfig: True  # 自动更新运行中的配置
RenewNotify: True  # 桌面通知
Overlaycontent: ""  # 追加内容，比如 `external-ui`
# 如果不想被桌面通知，上面这行请填 False
RenewTargetKey: cloud22
content:
   cloud1:
       - https://
   cloud22:
       - https://

```

```RenewConfig``` 指是否替换运行依赖的config,```RenewTargetKey```指替换的目标（必须在列表里）




编辑 python 脚本，按照注释配置 配置文件名称 和 数据目录。

#### 无障碍投喂

[![s](https://img.shields.io/badge/Become-sponsor-DB94A2)](https://dun.mianbaoduo.com/@Sky0717)

**使用本项目造成的一切后果需使用者负责。**