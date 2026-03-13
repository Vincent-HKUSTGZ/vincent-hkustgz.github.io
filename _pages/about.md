---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class="anchor" id="about-me"></span>

<div class="intro-block">
  <p class="intro-block__eyebrow">Research Theme</p>
  <h1 class="intro-block__title">Trustworthy AI</h1>
  <ul class="intro-block__facts">
    <li>PhD Student in Data Science and Analytics at <a href="https://www.hkust-gz.edu.cn/">The Hong Kong University of Science and Technology (Guangzhou)</a>.</li>
    <li>Advised by Prof. <a href="https://xinleihe.github.io/">Xinlei He</a> (Wuhan University, Overseas High-Level Young Talent Program), with primary supervision from Prof. Weijia Heng and co-supervision from Prof. Yutao Yue in HKUST(GZ).</li>
  </ul>
  <div class="inline-link-list">
    <a class="inline-link-list__item" href="https://scholar.google.com/citations?user=7ir2zYsAAAAJ&hl=en">Google Scholar</a>
    <a class="inline-link-list__item" href="mailto:zsun344@connect.hkust-gz.edu.cn">Email</a>
    <a class="inline-link-list__item" href="https://github.com/Vincent-HKUSTGZ">GitHub</a>
  </div>
  <div class="intro-block__scholar">
    <a href="https://scholar.google.com/citations?user=7ir2zYsAAAAJ&hl=en">
      <img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations" alt="Google Scholar citations">
    </a>
  </div>
</div>

<span class="anchor" id="research"></span>
## Research Interests

<div class="interest-grid">
  <span class="interest-chip">Trustworthy AI</span>
  <span class="interest-chip">AI Security &amp; Privacy</span>
  <span class="interest-chip">AI-Generated Content Detection</span>
  <span class="interest-chip">AI For Safety</span>
</div>

<span class="anchor" id="news"></span>
## News

<div class="content-panel">
  <div class="news-group">
    <h3 class="news-group__title">Paper Updates</h3>
    <ul class="news-clean-list">
      <li><span class="news-clean-list__icon">🎉</span><span class="news-clean-list__date">2026.01</span><span><a href="https://openreview.net/forum?id=DJkQ236C8B">JALMBench</a> was accepted at ICLR 2026.</span></li>
      <li><span class="news-clean-list__icon">🎉</span><span class="news-clean-list__date">2025.12</span><span><a href="https://arxiv.org/abs/2512.19058">6DAttack</a> was accepted at AAAI 2026 as an Oral presentation.</span></li>
      <li><span class="news-clean-list__icon">🎉</span><span class="news-clean-list__date">2025.09</span><span><a href="https://arxiv.org/abs/2502.21059">FC-Attack</a> was accepted at EMNLP 2025 Findings.</span></li>
      <li><span class="news-clean-list__icon">🎉</span><span class="news-clean-list__date">2025.09</span><span><a href="https://arxiv.org/abs/2509.18874">CHASM</a> was accepted at NeurIPS 2025.</span></li>
      <li><span class="news-clean-list__icon">🎉</span><span class="news-clean-list__date">2025.06</span><span><a href="https://arxiv.org/abs/2502.04951">Unsafe LLM-Based Search</a> was accepted at USENIX Security 2025.</span></li>
      <li><span class="news-clean-list__icon">🎉</span><span class="news-clean-list__date">2025.05</span><span><a href="https://aclanthology.org/2025.acl-long.1120/">AIGT on Social Media</a> was accepted at ACL 2025, and <a href="https://arxiv.org/abs/2412.17242">MGT Generalization</a> plus <a href="https://arxiv.org/abs/2503.08708">TH-Bench</a> were accepted at KDD 2025.</span></li>
      <li><span class="news-clean-list__icon">🎉</span><span class="news-clean-list__date">2025.03</span><span><a href="https://arxiv.org/abs/2411.17453">PEFTGuard</a> was accepted at IEEE S&amp;P 2025.</span></li>
    </ul>
  </div>
  <div class="news-group">
    <h3 class="news-group__title">Awards and Milestones</h3>
    <ul class="news-clean-list">
      <li><span class="news-clean-list__icon">🏆</span><span class="news-clean-list__date">2025.12</span><span>I received the 2025 DSA Excellent Research Award.</span></li>
      <li><span class="news-clean-list__icon">🏆</span><span class="news-clean-list__date">2024.11</span><span>AdSpectorX received the Best Paper Award at SENSYS-SocialMeta 2024.</span></li>
      <li><span class="news-clean-list__icon">🏆</span><span class="news-clean-list__date">2024.06</span><span>I received my firm PhD offer from HKUST(GZ).</span></li>
    </ul>
  </div>
</div>

<span class="anchor" id="selected-works"></span>
## Selected Papers

<p class="section-sub"><sup>*</sup> denotes equal contribution. <sup>&dagger;</sup> denotes corresponding author.</p>

<div class="card-grid">
  <a class="paper-card paper-card--ccf-a" href="https://arxiv.org/abs/2411.17453">
    <span class="paper-card__venue">IEEE S&amp;P 2025 <span class="paper-card__tag">CCF-A</span></span>
    <strong class="paper-card__title">PEFTGuard: Detecting Backdoor Attacks Against Parameter-Efficient Fine-Tuning</strong>
    <span class="paper-card__authors"><strong>Zhen Sun</strong>, Tianshuo Cong, Yule Liu, Chenhao Lin, Xinlei He, Rongmao Chen, Xingshuo Han, Xinyi Huang.</span>
  </a>
  <a class="paper-card paper-card--ccf-a" href="https://aclanthology.org/2025.acl-long.1120/">
    <span class="paper-card__venue">ACL 2025 <span class="paper-card__tag">CCF-A</span></span>
    <strong class="paper-card__title">Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media</strong>
    <span class="paper-card__authors"><strong>Zhen Sun<sup>*</sup></strong>, Zongmin Zhang<sup>*</sup>, Xinyue Shen, Ziyi Zhang, Yule Liu, Michael Backes, Yang Zhang, Xinlei He.</span>
  </a>
  <a class="paper-card paper-card--ccf-b" href="https://arxiv.org/abs/2502.21059">
    <span class="paper-card__venue">EMNLP 2025 Findings <span class="paper-card__tag">CCF-B</span></span>
    <strong class="paper-card__title">FC-Attack: Jailbreaking Large Vision-Language Models via Auto-Generated Flowcharts</strong>
    <span class="paper-card__authors">Ziyi Zhang<sup>*</sup>, <strong>Zhen Sun</strong><sup>*</sup>, Zongmin Zhang, Jihui Guo, Xinlei He.</span>
  </a>
  <a class="paper-card paper-card--ccf-a" href="https://arxiv.org/abs/2503.08708">
    <span class="paper-card__venue">KDD 2025 <span class="paper-card__tag">CCF-A</span></span>
    <strong class="paper-card__title">TH-Bench: Evaluating Evading Attacks via Humanizing AI Text on Machine-Generated Text Detectors</strong>
    <span class="paper-card__authors">Jingyi Zheng, Junfeng Wang, <strong>Zhen Sun</strong>, Wenhan Dong, Yule Liu, Xinlei He.</span>
  </a>
  <a class="paper-card paper-card--ccf-a" href="https://arxiv.org/abs/2512.19058">
    <span class="paper-card__venue">AAAI 2026 <span class="paper-card__tag">CCF-A · Oral</span></span>
    <strong class="paper-card__title">6DAttack: Backdoor Attacks in the 6DoF Pose Estimation</strong>
    <span class="paper-card__authors">Jihui Guo, Zongmin Zhang, <strong>Zhen Sun</strong>, Yuhao Yang, Jinlin Wu, Fu Zhang, Xinlei He.</span>
  </a>
  <a class="paper-card paper-card--ccf-a" href="https://openreview.net/forum?id=DJkQ236C8B">
    <span class="paper-card__venue">ICLR 2026<span class="paper-card__tag">CCF-A</span></span>
    <strong class="paper-card__title">JALMBench: Benchmarking Jailbreak Vulnerabilities in Audio Language Models</strong>
    <span class="paper-card__authors">Zifan Peng, Yule Liu, <strong>Zhen Sun</strong>, Mingchen Li, Zeren Luo, Jingyi Zheng, Wenhan Dong, Xinlei He, Xuechao Wang, Yingjie Xue, Shengmin Xu, Xinyi Huang.</span>
  </a>
  <a class="paper-card paper-card--ccf-a" href="https://arxiv.org/abs/2412.17242">
    <span class="paper-card__venue">KDD 2025 <span class="paper-card__tag">CCF-A</span></span>
    <strong class="paper-card__title">On the Generalization and Adaptation Ability of Machine-Generated Text Detectors in Academic Writing</strong>
    <span class="paper-card__authors">Yule Liu, Zhiyuan Zhong, Yifan Liao, <strong>Zhen Sun</strong>, Jingyi Zheng, Jiaheng Wei, Qingyuan Gong, Fenghua Tong, Yang Chen, Yang Zhang, Xinlei He.</span>
  </a>
  <a class="paper-card paper-card--ccf-a" href="https://arxiv.org/abs/2502.04951">
    <span class="paper-card__venue">USENIX Security 2025 <span class="paper-card__tag">CCF-A</span></span>
    <strong class="paper-card__title">Unsafe LLM-Based Search: Quantitative Analysis and Mitigation of Safety Risks in AI Web Search</strong>
    <span class="paper-card__authors">Zeren Luo, Zifan Peng, Yule Liu, <strong>Zhen Sun</strong>, Mingchen Li, Jingyi Zheng, Xinlei He.</span>
  </a>
  <a class="paper-card paper-card--ccf-a" href="https://arxiv.org/abs/2509.18874">
    <span class="paper-card__venue">NeurIPS 2025 <span class="paper-card__tag">CCF-A</span></span>
    <strong class="paper-card__title">CHASM: Unveiling Covert Advertisements on Chinese Social Media</strong>
    <span class="paper-card__authors">Jingyi Zheng, Tianyi Hu, Yule Liu, <strong>Zhen Sun</strong>, Zongmin Zhang, Zifan Peng, Wenhan Dong, Xinlei He.</span>
  </a>
  <a class="paper-card paper-card--award" href="#">
    <span class="paper-card__venue">SENSYS-SocialMeta 2024 <span class="paper-card__tag">Best Paper</span></span>
    <strong class="paper-card__title">AdSpectorX: A Multimodal Expert Spector for Covert Advertising Detection on Chinese Social Media</strong>
    <span class="paper-card__authors">Zongmin Zhang, Yujie Han, Zhou Zhang, Yule Liu, Jingyi Zheng, <strong>Zhen Sun</strong><sup>&dagger;</sup>.</span>
  </a>
</div>

<span class="anchor" id="services"></span>
## Services

<div class="content-panel">
  <div class="split-panel">
    <div>
      <h3>Conference PC / Reviewer</h3>
      <ul class="compact-list">
        <li>The Web Conference 2025 Workshop on Web for Good (WWW Web4Good)</li>
        <li>AAAI</li>
        <li>ACM MM</li>
        <li>ICML</li>
        <li>CVPR</li>
        <li>ACL</li>
        <li>EMNLP</li>
        <li>SaTML</li>
        <li>EuroS&amp;P</li>
        <li>AsiaCCS</li>
      </ul>
    </div>
    <div>
      <h3>Journal Reviewer</h3>
      <ul class="compact-list">
        <li>IEEE Transactions on Dependable and Secure Computing (TDSC)</li>
        <li>IEEE Transactions on Information Forensics and Security (TIFS)</li>
        <li>ACM Transactions on Privacy and Security (TOPS)</li>
        <li>International Journal of Human-Computer Interaction (IJHCI)</li>
      </ul>
    </div>
  </div>
</div>

<span class="anchor" id="honors"></span>
## Honors and Awards

<div class="content-panel">
  <ul class="compact-list">
    <li>2025, DSA Excellent Research Award</li>
    <li>Kaggle Competitions Expert (<a href="https://www.kaggle.com/rdxsun">Vincent Sirius</a>)</li>
    <li>2020.04, MCM/ICM Meritorious Winner</li>
    <li>2019 / 2020 / 2021, Third-class Scholarship of BUPT</li>
    <li>2019 / 2020 / 2021, Excellent Student Leader of BUPT</li>
  </ul>
</div>

<span class="anchor" id="education"></span>
## Education

<div class="content-panel">
  <ul class="compact-list">
    <li>2024.08-present, PhD in Data Science and Analytics, The Hong Kong University of Science and Technology (Guangzhou)</li>
    <li>2022.08-2023.10, MSc in Computer Science, City University of Hong Kong</li>
    <li>2018.09-2022.07, BSc in Computer Science and Technology, Beijing University of Posts and Telecommunications</li>
  </ul>
</div>

<span class="anchor" id="experience"></span>
## Experience

<div class="content-panel">
  <ul class="compact-list">
    <li><strong>Research Assistant</strong>, 2023.06-2024.05, Centre for Artificial Intelligence and Robotics (CAIR), Hong Kong Institute of Science &amp; Innovation, Chinese Academy of Sciences (HKISI-CAS). Worked on surgical LLMs and image segmentation. Supervisor: <a href="https://scholar.google.com.hk/citations?user=XujjZmUAAAAJ&hl=zh-CN">Dr. Jinlin Wu</a>.</li>
    <li><strong>Project Participant</strong>, 2022.09-2023.08, City University of Hong Kong. Worked on financial machine translation. Supervisor: <a href="https://scholar.google.com/citations?user=UcGN3MoAAAAJ&hl=en">Prof. Linqi Song</a>.</li>
  </ul>
</div>
