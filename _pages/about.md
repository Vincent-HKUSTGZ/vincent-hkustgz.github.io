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

<div class="hero-panel">
  <p class="hero-tag">Trustworthy AI</p>
  <h1 class="hero-title">Researching safe, secure, and reliable AI systems.</h1>
  <p class="hero-summary">
    I am a PhD student in Data Science and Analytics at
    <a href="https://www.hkust-gz.edu.cn/">The Hong Kong University of Science and Technology (Guangzhou)</a>.
    I am advised by Prof. <a href="https://xinleihe.github.io/">Xinlei He</a> (Wuhan University, Overseas Outstanding Young Scholar),
    with primary supervision from Prof. Weijia Heng and co-supervision from Prof. Yutao Yue.
    My work focuses on Trustworthy AI, especially AI safety, security, privacy, and robust multimodal foundation models.
  </p>
  <div class="hero-actions">
    <a class="btn btn--info btn--small" href="/publications/">Full Publications</a>
    <a class="btn btn--inverse btn--small" href="https://scholar.google.com/citations?user=7ir2zYsAAAAJ&hl=en">Google Scholar</a>
    <a class="btn btn--inverse btn--small" href="mailto:zsun344@connect.hkust-gz.edu.cn">Email</a>
  </div>
  <div class="hero-scholar">
    <a href="https://scholar.google.com/citations?user=7ir2zYsAAAAJ&hl=en">
      <img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations" alt="Google Scholar citations">
    </a>
  </div>
</div>

<span class="anchor" id="research"></span>
## Research Interests

I build and study AI systems that remain aligned, robust, and reliable in realistic deployment settings. My recent work spans jailbreak and backdoor attacks, AI-generated content detection, multimodal model safety, and trustworthy evaluation.

<div class="interest-grid">
  <span class="interest-chip">AI Safety</span>
  <span class="interest-chip">AI Security</span>
  <span class="interest-chip">AI Privacy</span>
  <span class="interest-chip">LLM and VLM Robustness</span>
  <span class="interest-chip">Trustworthy Multimodal AI</span>
  <span class="interest-chip">Machine-Generated Content Detection</span>
</div>

<span class="anchor" id="selected-works"></span>
## Selected Works

<div class="selected-grid">
  <a class="selected-card" href="/publications/#peftguard">
    <span class="selected-card__venue">IEEE S&amp;P 2025</span>
    <strong class="selected-card__title">PEFTGuard</strong>
    <span class="selected-card__text">Detecting backdoor attacks against parameter-efficient fine-tuning.</span>
  </a>
  <a class="selected-card" href="/publications/#aigt-social-media">
    <span class="selected-card__venue">ACL 2025</span>
    <strong class="selected-card__title">AIGT on Social Media</strong>
    <span class="selected-card__text">Quantifying and monitoring AI-generated text in the wild.</span>
  </a>
  <a class="selected-card" href="/publications/#unsafe-llm-search">
    <span class="selected-card__venue">USENIX Security 2025</span>
    <strong class="selected-card__title">Unsafe LLM-Based Search</strong>
    <span class="selected-card__text">Analyzing and mitigating safety risks in AI web search.</span>
  </a>
  <a class="selected-card" href="/publications/#chasm">
    <span class="selected-card__venue">NeurIPS 2025</span>
    <strong class="selected-card__title">CHASM</strong>
    <span class="selected-card__text">Unveiling covert advertisements on Chinese social media.</span>
  </a>
</div>

<p class="section-note">A complete list of papers and preprints is available on the <a href="/publications/">Publications</a> page.</p>

<span class="anchor" id="news"></span>
## News

<ul class="news-list">
  <li><span class="news-list__date">2025.12</span> <span class="news-list__emoji">🏅</span> I received the 2025 DSA Excellent Research Award.</li>
  <li><span class="news-list__date">2026.01</span> <span class="news-list__emoji">🏆</span> <a href="/publications/#jalmbench">JALMBench</a> was accepted at ICLR 2026 and received a Best Paper Award.</li>
  <li><span class="news-list__date">2025.12</span> <span class="news-list__emoji">🎯</span> <a href="/publications/#attack-6d">6DAttack</a> was accepted at AAAI 2026 as an Oral presentation.</li>
  <li><span class="news-list__date">2025.09</span> <span class="news-list__emoji">📣</span> <a href="/publications/#fc-attack">FC-Attack</a> was accepted at EMNLP 2025 Findings.</li>
  <li><span class="news-list__date">2025.09</span> <span class="news-list__emoji">🧭</span> <a href="/publications/#chasm">CHASM</a> was accepted at NeurIPS 2025.</li>
  <li><span class="news-list__date">2025.06</span> <span class="news-list__emoji">🛡️</span> <a href="/publications/#unsafe-llm-search">Unsafe LLM-Based Search</a> was accepted at USENIX Security 2025.</li>
  <li><span class="news-list__date">2025.05</span> <span class="news-list__emoji">📚</span> <a href="/publications/#aigt-social-media">AIGT on Social Media</a> was accepted at ACL 2025, and <a href="/publications/#mgt-generalization">MGT Generalization</a> plus <a href="/publications/#th-bench">TH-Bench</a> were accepted at KDD 2025.</li>
  <li><span class="news-list__date">2025.03</span> <span class="news-list__emoji">🔐</span> <a href="/publications/#peftguard">PEFTGuard</a> was accepted at IEEE S&amp;P 2025.</li>
  <li><span class="news-list__date">2024.11</span> <span class="news-list__emoji">🥇</span> <a href="/publications/#adspectorx">AdSpectorX</a> received the Best Paper Award at SENSYS-SocialMeta 2024.</li>
  <li><span class="news-list__date">2024.06</span> <span class="news-list__emoji">🎓</span> I received my firm PhD offer from HKUST(GZ).</li>
</ul>

<span class="anchor" id="services"></span>
## Services

### Conference PC / Reviewer

- The Web Conference 2025 Workshop on Web for Good (WWW Web4Good)
- AAAI
- ACM MM
- ICML
- SaTML
- EuroS&amp;P
- AsiaCCS

### Journal Reviewer

- International Journal of Human-Computer Interaction (IJHCI)

<span class="anchor" id="honors"></span>
## Honors and Awards

- **Kaggle Competitions Expert** ([Vincent Sirius](https://www.kaggle.com/rdxsun))
- 2020.04, MCM/ICM Meritorious Winner
- 2019 / 2020 / 2021, Third-class Scholarship of BUPT
- 2019 / 2020 / 2021, Excellent Student Leader of BUPT

<span class="anchor" id="education"></span>
## Education

- 2024.08-present, PhD in Data Science and Analytics, The Hong Kong University of Science and Technology (Guangzhou)
- 2022.08-2023.10, MSc in Computer Science, City University of Hong Kong
- 2018.09-2022.07, BSc in Computer Science and Technology, Beijing University of Posts and Telecommunications

<span class="anchor" id="experience"></span>
## Experience

- **Research Assistant**, 2023.06-2024.05, Centre for Artificial Intelligence and Robotics (CAIR), Hong Kong Institute of Science &amp; Innovation, Chinese Academy of Sciences (HKISI-CAS). Worked on surgical LLMs and image segmentation. Supervisor: [Dr. Jinlin Wu](https://scholar.google.com.hk/citations?user=XujjZmUAAAAJ&hl=zh-CN).
- **Project Participant**, 2022.09-2023.08, City University of Hong Kong. Worked on financial machine translation. Supervisor: [Prof. Linqi Song](https://scholar.google.com/citations?user=UcGN3MoAAAAJ&hl=en).