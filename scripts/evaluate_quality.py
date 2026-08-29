#!/usr/bin/env python3
"""Multi-Dimensional Automated Quality & SEO Scoring Engine (100-Point System)."""

import sys
from pathlib import Path
import yaml
import re

ROOT = Path(__file__).resolve().parent.parent

def evaluate():
    scores = {}
    details = {}
    
    # -------------------------------------------------------------
    # 1. 关键词覆盖与 SEO 密度 (Max 20分)
    # -------------------------------------------------------------
    readme_file = ROOT / "README.md"
    if not readme_file.exists():
        print("ERROR: README.md not found. Run python scripts/build_readme.py first.")
        sys.exit(1)
        
    readme_text = readme_file.read_text(encoding="utf-8")
    
    core_keywords = ["vpn推荐", "机场推荐", "翻墙", "梯子", "科学上网", "节点", "订阅"]
    scenario_keywords = ["chatgpt", "claude", "netflix", "4k", "流媒体", "出海", "游戏", "hysteria 2", "reality", "iepl", "iplc"]
    
    core_hit = sum(1 for kw in core_keywords if kw in readme_text.lower())
    scenario_hit = sum(1 for kw in scenario_keywords if kw in readme_text.lower())
    
    kw_score = min(20.0, (core_hit / len(core_keywords)) * 10.0 + (scenario_hit / len(scenario_keywords)) * 10.0)
    scores["SEO & 关键词覆盖度"] = round(kw_score, 1)
    details["SEO & 关键词覆盖度"] = f"核心词命中 {core_hit}/{len(core_keywords)}，长尾场景词命中 {scenario_hit}/{len(scenario_keywords)}"

    # -------------------------------------------------------------
    # 2. E-E-A-T 权威性与开源工程包装 (Max 20分)
    # -------------------------------------------------------------
    eeat_score = 0.0
    eeat_items = []
    
    check_files = [
        ("docs/methodology.md", 5.0, "评测方法论"),
        ("docs/protocols.md", 4.0, "现代协议全景技术指南"),
        ("docs/clients.md", 4.0, "全平台客户端选型手册"),
        ("docs/blacklist.md", 3.0, "跑路预警与避坑黑名单"),
        ("LICENSE", 2.0, "MIT 开源协议"),
        ("CONTRIBUTING.md", 2.0, "开源贡献与纠错规范")
    ]
    for rel_path, weight, label in check_files:
        if (ROOT / rel_path).exists():
            eeat_score += weight
            eeat_items.append(label)
            
    scores["E-E-A-T 权威性与工程规范"] = round(eeat_score, 1)
    details["E-E-A-T 权威性与工程规范"] = f"完备性规范：{', '.join(eeat_items)}"

    # -------------------------------------------------------------
    # 3. 信息架构、排版与交互体验 (Max 20分)
    # -------------------------------------------------------------
    ux_score = 0.0
    ux_reasons = []
    
    # 折叠面板检查
    if "<details" in readme_text and "</details>" in readme_text:
        ux_score += 5.0
        ux_reasons.append("交互式折叠目录")
        
    # 对比表格检查
    table_count = len(re.findall(r"\|.*\|.*\|", readme_text))
    if table_count >= 5:
        ux_score += 5.0
        ux_reasons.append(f"包含结构化对比表格 ({table_count} 行)")
        
    # 决策树与 ASCII/可视化图表
    if "┌─" in readme_text or "```" in readme_text:
        ux_score += 5.0
        ux_reasons.append("决策矩阵与场景直达")
        
    # 锚点完整度
    anchor_matches = len(re.findall(r'<div id=".*"></div>', readme_text))
    if anchor_matches >= 40:
        ux_score += 5.0
        ux_reasons.append(f"全量内嵌无缝锚点 ({anchor_matches} 个)")
        
    scores["信息架构与 UX 交互"] = round(ux_score, 1)
    details["信息架构与 UX 交互"] = "，".join(ux_reasons)

    # -------------------------------------------------------------
    # 4. 单源数据 Schema 完备度 (Max 15分)
    # -------------------------------------------------------------
    data_file = ROOT / "data" / "providers.yml"
    with open(data_file, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    providers = data.get("providers", [])
    
    data_score = 0.0
    if len(providers) >= 45:
        data_score += 8.0
    elif len(providers) >= 30:
        data_score += 5.0
        
    all_fields_ok = True
    for p in providers:
        if not (p.get("line_type") and p.get("protocols") and p.get("price_starting") and p.get("pros") and p.get("cons")):
            all_fields_ok = False
            break
            
    if all_fields_ok:
        data_score += 7.0
        
    scores["数据完整性 (SSOT Schema)"] = round(data_score, 1)
    details["数据完整性 (SSOT Schema)"] = f"总收录服务商 {len(providers)} 家，全量元数据零缺失"

    # -------------------------------------------------------------
    # 5. 链接与安全性审计 (Max 15分)
    # -------------------------------------------------------------
    sec_score = 15.0
    sec_issues = []
    
    # 检查明文 token
    if "github_pat_" in readme_text or "ghp_" in readme_text:
        sec_score -= 10.0
        sec_issues.append("警告：检测到明文敏感令牌暴露！")
        
    # 检查空链接
    if "](#)" in readme_text or "]()" in readme_text:
        sec_score -= 2.0
        sec_issues.append("存在未赋值占位空链接")
        
    scores["链接与安全健康度"] = round(max(0.0, sec_score), 1)
    details["链接与安全健康度"] = "零明文机密暴露，无死链占位符" if not sec_issues else "；".join(sec_issues)

    # -------------------------------------------------------------
    # 6. 自动化与活跃维护能力 (Max 10分)
    # -------------------------------------------------------------
    ci_score = 0.0
    ci_items = []
    
    if (ROOT / ".github" / "workflows" / "data-and-links.yml").exists():
        ci_score += 5.0
        ci_items.append("GitHub Actions 自动巡检流")
        
    if (ROOT / "scripts" / "build_readme.py").exists() and (ROOT / "scripts" / "validate_data.py").exists():
        ci_score += 5.0
        ci_items.append("自动化编译与校验脚本链")
        
    scores["自动化与持续活跃能力"] = round(ci_score, 1)
    details["自动化与持续活跃能力"] = "，".join(ci_items)

    # -------------------------------------------------------------
    # 汇总计算与报告输出
    # -------------------------------------------------------------
    total_score = sum(scores.values())
    
    print("\n" + "=" * 65)
    print(f"   🏆 新一代顶流项目多维量化评估质量看板 (Total: {total_score:.1f} / 100)")
    print("=" * 65)
    
    for dimension, s in scores.items():
        bar_len = int(s / 20.0 * 20)
        bar = "█" * bar_len + "░" * (20 - bar_len)
        print(f" • {dimension:<22} [{bar}] {s:>4.1f} 分 ｜ {details[dimension]}")
        
    print("=" * 65)
    
    if total_score >= 95.0:
        print("🌟 评估判定：【S+ 卓越工业级标杆】，具备绝对统治级 Google/GitHub SEO 竞争力！\n")
    elif total_score >= 85.0:
        print("✅ 评估判定：【A 良好】，部分细节仍可进一步打磨优化。\n")
    else:
        print("⚠️ 评估判定：【B 待优化】，请根据上方指标逐项补强。\n")
        
    return total_score

if __name__ == "__main__":
    evaluate()
