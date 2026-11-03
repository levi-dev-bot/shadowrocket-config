# Shadowrocket 分流配置

基于 [johnshall/Shadowrocket-ADBlock-Rules-Forever](https://github.com/johnshall/Shadowrocket-ADBlock-Rules-Forever) 的 `lazy_group.conf`，叠加个人自定义规则层。

## 订阅地址

```
https://cdn.jsdelivr.net/gh/levi-dev-bot/shadowrocket-config@main/lazy_group.conf
```

## 文件说明

| 文件 | 作用 | 什么时候改 |
|---|---|---|
| `lazy_group.conf` | 主配置（General / Proxy Group / Rule / Host / Rewrite / MITM） | 几乎不动 |
| `custom.list` | 个人自定义规则集，插在规则链最前面 | **日常只改这个** |

`custom.list` 通过 `RULE-SET` 在主配置中排第一位匹配，优先级高于所有内置规则集，所以同一条域名在内置列表里被判为 DIRECT 时，写在 `custom.list` 里可以覆盖成 PROXY，反过来也一样。

## 更新方式

Shadowrocket 里：`配置` → 当前配置 → 右上角更新（或下拉刷新）。

主配置里的 `update-url` 已指向本仓库，Shadowrocket 自动更新时拉的也是这里。

## 改完没生效？

jsDelivr 是 CDN，有缓存。提交后如果拉到的还是旧版本，等 1-2 分钟，或在 Shadowrocket 里换成下面这个 GitHub 直连地址临时用：

```
https://raw.githubusercontent.com/levi-dev-bot/shadowrocket-config/main/custom.list
```
