# 现代代理协议全景技术横评 (Protocol Guide)

选择合适的协议是保障翻墙体验与防封锁的关键技术支撑：

| 协议名称 | 传输层基础 | 特征混淆与防封原理 | 适用网络场景 | 推荐客户端 |
| :--- | :--- | :--- | :--- | :--- |
| **Hysteria 2** | UDP (QUIC) | 自研暴力拥塞控制 (Brutal)，多端口跳跃 (Port Hopping) | **弱网/高丢包/跨大西洋长距离** 极速拉满 | Sing-box, Clash Verge Rev, NekoBox |
| **VLESS-Reality** | TCP | 借用大型合规站点真实 TLS 证书伪装，彻底消除服务端证书特征 | **高压敏感时期/防火墙重点监控环境** | v2rayN, Sing-box, Shadowrocket |
| **Trojan-GFW** | TCP (TLS) | 将流量完美伪装为标准 HTTPS 流量，未授权流量直接重定向到正常网站 | **日常稳定中继/流媒体长期观看** | 全平台客户端均完美原生支持 |
| **Shadowsocks 2022** | TCP / UDP | 全新现代密码学架构，彻底消除重放攻击与主动探测特征 | **全内网 IEPL/IPLC 纯专线传输** | Surge, Clash Meta, Loon, Stash |
