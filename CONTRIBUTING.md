# 贡献指南 (Contributing Guide)

感谢对本项目的关注与支持！我们欢迎社区提交客观、可复现的服务商信息纠错、节点测速报告以及失效链接反馈。

## 提交规范
1. **服务商信息变更**：请直接修改 `data/providers.yml` 文件，切勿直接手动编辑 `README.md`。
2. **数据完整性**：所有新增或修改的条目必须包含完整的 Schema 字段（包含协议、线路类型、价格区间、客观优缺点与状态）。
3. **CI 校验**：提交 PR 前请在本地运行 `python scripts/validate_data.py` 和 `python scripts/evaluate_quality.py`，确保质量评分保持在 95 分以上。
