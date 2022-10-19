# encoding: utf-8
# auto clash config file renew prog
import os
import requests
import yaml
import time
import pathlib

# config?
Config = ".Clash.yaml"
# data save to...
Folder = "Clash"
ConfigPath = f"{os.getcwd()}/{Config}"
print(f"> Use Config: {ConfigPath}")


class Tool(object):
    @staticmethod
    def sendNotify(text: str, inform=True) -> None:
        if inform:
            import notify2
            notify2.init('ClashRenew')
            ns = notify2.Notification('ClashRenew', text)
            ns.show()

    @staticmethod
    def overWrite(origin: dict, newer: dict) -> dict:
        origin.update(newer)
        return origin


class App(object):
    def __init__(self, cake) -> None:
        """
        初始化所有信息
        :param cake: 配置文件数据
        """
        self.c = False
        if cake:
            self.c = yaml.load(cake, Loader=yaml.CFullLoader)
            self.count = []
            self.changeConfig = self.c.get('RenewConfig')
            self.willUse = self.c.get('RenewTargetKey')
            self.proxyList = self.c.get("content")
            self.notifySwitch = self.c.get("RenewNotify")
            self.Overlaycontent = self.c.get("Overlaycontent")
        # 父文件夹
        self.Cpath = f"{os.getcwd()}/{Folder}"
        self.clashConfig = f"{os.getcwd()}/.config/clash/config.yaml"
        self.templateConfig = f"{self.Cpath}/.template.yaml"
        pathlib.Path(self.Cpath).mkdir(exist_ok=True)
        pathlib.Path(self.templateConfig).touch(exist_ok=True)

    def Worker(self, name, urlList):
        time.sleep(1)
        try:
            config_get = requests.get(url=urlList[0], headers=headers)
            config_get.raise_for_status()  # 如果不是200，产生异常requests.HTTPError
            config_get.encoding = 'utf-8'
            # 子文件夹
            rpath = f"{self.Cpath}/{name}"
            pathlib.Path(rpath).mkdir(exist_ok=True)
            if len(config_get.text) > 500:
                with open(rpath + "/" + time.strftime("%Y%m%d%H%M%S") + '.yaml', 'w+', encoding='utf-8') as fs:
                    fs.write(config_get.text)
                    fs.flush()
                    os.fsync(fs.fileno())
            else:
                raise ValueError("Content less than 500 words, skip for safety")
        except Exception as e:
            if "Connection reset by peer" in str(e):
                e = "请求频繁被拒:" + str(e)
            Tool.sendNotify(f"> Error occur\n{e}", inform=self.notifySwitch)
        else:
            self.count.append(name)
            if name == self.willUse:
                _nowConfig = yaml.load(config_get.text, Loader=yaml.CFullLoader)
                _tempConfig = yaml.load(open(self.templateConfig, 'r', encoding='utf-8'), Loader=yaml.FullLoader)
                if all([self.Overlaycontent, _nowConfig, _tempConfig]):
                    _nowConfig = Tool.overWrite(_nowConfig, _tempConfig)
                with open(self.clashConfig, 'w+', encoding='utf-8') as fs:
                    yaml.dump(_nowConfig, fs, sort_keys=False, allow_unicode=True)

    def Finally(self):
        _timeNow = time.strftime("%Y-%m-%d %H:%M:%S")
        _log_base = f"Update completed- + {_timeNow}\nTotal:{len(self.proxyList)}\nSuccess Renew:{len(self.count)}"
        # self.sendNotify(info,prt=True)
        _log = f"Use config:{ConfigPath}\n{_log_base}"
        if self.changeConfig:
            _log_change = ("The running configuration file has been replaced ,use:" + self.willUse)
            _log = f"{_log}\n{_log_change}"
        Tool.sendNotify(_log, inform=self.notifySwitch)

    def Run(self):
        if all([self.c, self.changeConfig, self.willUse, self.proxyList]):
            for k, v in self.proxyList.items():
                self.Worker(k, v)
            self.Finally()
        else:
            print("> ClashRenewError: Argument missing...")


headers = {'Accept': '*/*',
           'Accept-Language': 'en-US,en;q=0.8',
           'Cache-Control': 'max-age=0',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 '
                         'Safari/537.36',
           'Connection': 'keep-alive'
           }
# main
try:
    f = open(ConfigPath, 'r')
except FileNotFoundError:
    Tool.sendNotify(text="打开配置文件失败了", inform=True)
else:
    fileC = f.read()
    f.close()
    time.sleep(15)
    App(cake=fileC).Run()
