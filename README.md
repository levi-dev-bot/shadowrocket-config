# Shadowrocket 分流配置

基于 [johnshall/Shadowrocket-ADBlock-Rules-Forever](https://github.com/johnshall/Shadowrocket-ADBlock-Rules-Forever) 的 `lazy_group.conf`（2026-11-03 版），叠加个人自定义规则层。

## 配置文件地址（在 Shadowrocket「配置」里添加这个）

```
https://cdn.jsdelivr.net/gh/levi-dev-bot/shadowrocket-config@main/lazy_group.conf
```

这个地址是**规则配置文件**，不是节点订阅。节点订阅仍用你自己的机场那条，两者分开互不影响。

## 文件说明

- `lazy_group.conf` —— 主配置（General / Proxy Group / Rule / Host / Rewrite / MITM），一般不动
- `custom.list` —— 个人自定义规则集，**日常只改这个**

`custom.list` 在 `[Rule]` 里通过 `RULE-SET` 排在第一位匹配，优先级高于所有内置规则集。所以同一个域名内置列表判 DIRECT，你在 `custom.list` 里写 PROXY 就能覆盖，反过来也一样。

## 规则写法

```
DOMAIN-SUFFIX,example.com,PROXY        # 整站及子域走代理
DOMAIN,www.example.com,DIRECT          # 仅这一个域名直连
DOMAIN-KEYWORD,abc,REJECT              # 关键词拦截
```

策略除了 `PROXY` / `DIRECT` / `REJECT`，也可以直接写分组名：`香港节点` `台湾节点` `日本节点` `新加坡节点` `韩国节点` `美国节点` `AI` `YouTube` `Netflix` `TikTok` 等。

## 更新

Shadowrocket：`配置` → 选中该配置 → 右上角「更新」（或下拉刷新）。

主配置内 `update-url` 已指向本仓库，自动更新拉的就是这里。

## CDN 缓存说明

jsDelivr 有缓存。改完若拉到旧版本，等 1-2 分钟；或临时换成 GitHub 直连：

```
https://raw.githubusercontent.com/levi-dev-bot/shadowrocket-config/main/custom.list
```

注意反过来：GitHub raw 自己有约 5 分钟缓存，jsDelivr 可以用 purge 接口强制刷新，所以日常推荐用 jsDelivr 那条。
