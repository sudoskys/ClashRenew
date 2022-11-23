# ClashRenew

自动备份配置列表中网址的数据并写入特定文件。

在 **不采用proxy provider的情况下** 实现 Linux clash 或clash-meta 配置 config.yaml 的自动更新。

Ps: 你也可以使用 Clash proxy-provider 实现自动更新。

## 安装

克隆本项目后请移动 `clash.py` 和 `cron.sh` 到 ```～/``` （HOME）目录。

#### 依赖

```bash
pip install requirements.txt
```

### 覆写

在脚本数据目录（默认为 `Clash`） 下新建一个 `.template.yaml` ，里面写东西就能自动覆写运行配置。

### 配置开机自动

不要使用```.zshrc```或者```.bashrc```，会产生打开终端就执行的问题...

**运行如下来开机自动启动clash**

```bash
systemctl --user enable clash.service
systemctl --user start clash.service
systemctl --user status clash.service
```

如果你使用 `meta`，替换 `clash.service` 为 `clash-meta.service`

**复制cron.sh**

本地账户配置开机服务

```bash
sudo cp ~/cron.sh  /usr/local/bin
```

```bash
cd /usr/lib/systemd/user/
sudo vim clashrenew.service
```

**填入**

```service
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

```bash
systemctl --user enable clashrenew.service
systemctl --user start clashrenew.service
systemctl --user status clashrenew.service
```

这样用户自定义服务就可以运行起来了

PS:ExecStartPre=/bin/sleep 20 代表延迟20秒，也可以修改clash的服务,使其延迟启动（如果你是无线链接）

`clash.service` 举例 （适用于启动成功但io超时）

```service
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

Ps:至于 network ，见 [这里](https://access.redhat.com/documentation/zh-cn/red_hat_enterprise_linux/8/html/configuring_and_managing_networking/systemd-network-targets-and-services_configuring-and-managing-networking)

*部分参考此教程*
<https://blog.linioi.com/posts/clash-on-arch/>

### 程序配置文件示例

注意空格

```yaml
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

**使用本项目造成的一切后果需使用者负责。**
