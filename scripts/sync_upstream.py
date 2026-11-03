#!/usr/bin/env python3
"""拉取 johnshall 上游 lazy_group.conf，重新注入个人自定义规则块。"""
import sys, pathlib, urllib.request

UP = "https://raw.githubusercontent.com/johnshall/Shadowrocket-ADBlock-Rules-Forever/master/lazy_group.conf"
RAW = "https://cdn.jsdelivr.net/gh/levi-dev-bot/shadowrocket-config@main"
ANCHOR = "RULE-SET,https://raw.githubusercontent.com/iab0x00/ProxyRules/main/Rule/AI.txt,AI"
OLD_URL = "https://johnshall.github.io/Shadowrocket-ADBlock-Rules-Forever/lazy_group.conf"
BLOCK = (
    "# ==================== 个人自定义规则（Hermes 维护）====================\n"
    "# 日常新增/修改网站只改 custom.list，不要动本文件其余部分。\n"
    "# 该列表排在最前，优先于下方所有内置规则匹配。\n"
    "# 语法示例： DOMAIN-SUFFIX,example.com,PROXY   /   DOMAIN,www.a.com,DIRECT\n"
    f"RULE-SET,{RAW}/custom.list,PROXY\n\n"
)

def main():
    try:
        up = urllib.request.urlopen(UP, timeout=30).read().decode("utf-8")
    except Exception as e:
        print(f"上游拉取失败，跳过：{e}")
        return 0
    up = up.replace(OLD_URL, f"{RAW}/lazy_group.conf")
    if ANCHOR not in up:
        print("锚点缺失，上游结构变了，需人工检查")
        return 1
    if "个人自定义规则" in up:
        print("上游已含自定义块，跳过注入")
        return 0
    up = up.replace(ANCHOR, BLOCK + ANCHOR, 1)
    pathlib.Path("lazy_group.conf").write_text(up, encoding="utf-8")
    print("已重新注入自定义块")
    return 0

if __name__ == "__main__":
    sys.exit(main())
