# 全平台客户端安全选型与避坑全指南 (Clients & Tooling)

> ⚠️ **安全警告**：严禁在第三方搜索引擎或未知非官方渠道下载任何闭源的所谓“破解版”客户端，极易植入恶意劫持脚本。请始终通过官方 GitHub Releases 下载！

## 1. 推荐客户端全景选型表

| 操作系统 | 推荐客户端 | 内核支持 | 核心优势 | 官方安全源 |
| :--- | :--- | :--- | :--- | :--- |
| **Windows** | **Clash Verge Rev** / **Sing-box** | Mihomo / Sing-box | 界面现代化、原生支持 Hy2 与 Reality、内存占用低 | [GitHub Releases](https://github.com/clash-verge-rev/clash-verge-rev) |
| **macOS** | **Clash Verge Rev** / **Surge** / **Loon** | Mihomo / Surge Core | 完美适配 Apple Silicon，原生系统代理分流 | [GitHub Releases](https://github.com/clash-verge-rev/clash-verge-rev) |
| **Android** | **Clash Meta for Android** / **Sing-box** | Mihomo / Sing-box | 分应用代理、省电优化、规则集丰富 | [GitHub Releases](https://github.com/MetaCubeX/ClashMetaForAndroid) |
| **iOS / iPadOS** | **Shadowrocket (小火箭)** / **Surge** / **Stash** | 多内核集成 | 需外区 Apple ID 购买，功能强大，支持一键扫码 | App Store (外区) |
| **软路由 (OpenWrt)** | **OpenClash** / **Niketa** | Mihomo Core | 全屋透明代理、智能 DNS 分流 | [GitHub Releases](https://github.com/vernesong/OpenClash) |
