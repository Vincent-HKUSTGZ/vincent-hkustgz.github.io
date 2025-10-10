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

<span class='anchor' id='about-me'></span>

I am a PhD student in DSA Thrust of the Information Hub at [Hong Kong University of Science and Technology (Guangzhou)](https://www.hkust-gz.edu.cn/) advised by Prof. [Xinlei He](https://xinleihe.github.io/). My research interest includes AI Security and Privacy.  (<a href='https://scholar.google.com/citations?user=7ir2zYsAAAAJ&hl=en'></a><a href='https://scholar.google.com/citations?user=7ir2zYsAAAAJ&hl=en'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>).


# 🔥 News
- *2025.06*:&nbsp;🎉🎉Our paper on the [security of LLM-based search](https://arxiv.org/abs/2502.04951) has been accepted to USENIX Security 2025.
- *2025.05*:&nbsp;🎉🎉(AIGT detection) One paper got accepted in ACL 2025; Two paper got accepted in KDD  D&B track 2025
- *2025.3*:&nbsp;🎉🎉 PEFTGuard got accepted in [IEEE S$\&$P 2025](https://sp2025.ieee-security.org/)
- *2024.11*: &nbsp;🎉🎉 Our paper won the **<span style="color: red;">Best Paper Award</span>** of  [SENSYS-SocialMeta'24](https://dl.acm.org/doi/proceedings/10.1145/3698387).
- *2024.06*: &nbsp;🎉🎉 I receive my firm PhD offer from HKUST(GZ).

# 📝 Publications

$^\star$: Equal contribution; $^\dagger$: Corresponding author

### Conference

- <span style="color: orange;">**[USENIX Security'25]**</span> Unsafe LLM-Based Search: Quantitative Analysis and Mitigation of Safety Risks in AI Web Search

  Zeren Luo, Zifan Peng, Yule Liu, Zhen Sun, Mingchen Li, Jingyi Zheng, Xinlei He

  <code class="language-plaintext highlighter-rouge">CCF-A</code> [[arxiv](https://arxiv.org/abs/2502.04951)]

- <span style="color: orange;">**[ACL Main'25]**</span> **Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media**

  **Zhen Sun$^\star$**, Zongmin Zhang$^\star$, Xinyue Shen, Ziyi Zhang, Yule Liu, Michael Backes, Yang Zhang, Xinlei He

  <code class="language-plaintext highlighter-rouge">CCF-A</code> [[arxiv](https://arxiv.org/abs/2412.18148)]

- <span style="color: orange;">**[IEEE S$\&$P'25]**</span> **PEFTGuard: Detecting Backdoor Attacks Against Parameter-Efficient Fine-Tuning** 

  **Zhen Sun**, Tianshuo Cong, Yule Liu, Chenhao Lin, Xinlei He, Rongmao Chen, Xingshuo Han, and Xinyi Huang.

  <code class="language-plaintext highlighter-rouge">CCF-A</code> [[arxiv](https://arxiv.org/abs/2411.17453)] (AR: 257/1740=14.8%, Cycle 2 AR: 151/1001=15.1%)

- <span style="color: orange;">**[KDD D&B'25]** </span> **On the Generalization Ability of Machine-Generated Text Detectors**

  Yule Liu$^\star$, Zhiyuan Zhong$^\star$, Yifan Liao, **Zhen Sun**, Jingyi Zheng, Jiaheng Wei, Qingyuan Gong, Fenghua Tong, Yang Chen, Yang Zhang, Xinlei He

  <code class="language-plaintext highlighter-rouge">CCF-A</code> [[arxiv](https://arxiv.org/abs/2412.17242)]

- <span style="color: orange;">**[KDD D&B'25]** </span> **TH-Bench: Evaluating Evading Attacks via Humanizing AI Text on Machine-Generated Text Detectors**

  Jingyi Zheng$^\star$, Junfeng Wang$^\star$, **Zhen Sun**, Wenhan Dong, Yule Liu, Xinlei He

  <code class="language-plaintext highlighter-rouge">CCF-A</code> [[arxiv](https://arxiv.org/abs/2503.08708)]

- <span style="color: orange;">**[SENSYS-SocialMeta'24]**</span> **AdSpectorX: A Multimodal Expert Spector for Covert Advertising Detection on Chinese Social Media**

  Zongmin Zhang, Yujie Han, Zhou Zhang, Yule Liu, Jingyi Zheng, and **Zhen Sun$^\dagger$**.

  In Proceedings of the Third International Workshop on Social and Metaverse Computing, Sensing and Networking, pp. 50-56. 2024.

  <code class="language-plaintext highlighter-rouge">CCF-B</code> [[code](https://github.com/Zonmgin-Zhang/AdSpectorX)] 🏆 Best Paper Award

### Under Review $\&$ Manuscript

- **Jailbreak Attacks and Defenses Against Large Language Models: A Survey** [[arxiv](https://arxiv.org/abs/2407.04295)]
  
  Sibo Yi$^\star$, Yule Liu$^\star$, **Zhen Sun$^\star$**, Tianshuo Cong, Xinlei He, Jiaxing Song, Ke Xu, and Qi Li.
  
- **Quantized Delta Weight Is Safety Keeper** [[arxiv](https://arxiv.org/abs/2411.19530)]

  Yule Liu, **Zhen Sun,** Xinlei He, and Xinyi Huang

- **FC-Attack: Jailbreaking Large Vision-Language Models via Auto-Generated Flowcharts**[[arxiv](https://arxiv.org/abs/2502.21059)]

  Ziyi Zhang$^\star$, **Zhen Sun$^\star$**, Zongmin Zhang, Jihui Guo, Xinlei He

- **The Rising Threat to Emerging AI-Powered Search Engines**[[arxiv](https://arxiv.org/abs/2502.04951)]

  Zeren Luo, Zifan Peng, Yule Liu, **Zhen Sun**, Mingchen Li, Jingyi Zheng, Xinlei He

# 👨‍🎓Services

### Reviewer of Conference

- ICML
- CVPR
- SaTML 
- EuroS$\&$P
- AsiaCCS
- AAAI
- MM

### Reviewer of Journals

- IEEE Transactions on Dependable and Secure Computing (TDSC)
- ACM Transactions on Privacy and Security (TOPS)

# 🥇 Honors and Awards

- 🥈**Kaggle Competitions Expert** ([Vincent Sirius](https://www.kaggle.com/rdxsun))
- *2020.04*, MCM/ICM Meritorious Winner
- *2019 / 2020 / 2021*, Third-class Scholarship of BUPT
- *2019 / 2020 / 2021*, Excellent Student Leader of BUPT

# 🎓 Educations

- *2024.08-now*, PhD in Data Science Analysis, Hong Kong University of Science and Technology (Guangzhou)
- *2022.08-2023.10*, MSc in Computer Science, City University of Hong Kong
- *2018.09-2022.07*, BSc in Computer Science and Technology, Beijing University of Posts and Telecommunications

# 💻 Experiences
-  **[Research Assistant]** *2023.06 - 2024.05*, Centre for Artificial Intelligence and Robotics (CAIR) Hong Kong Institute of Science $\&$ Innovation, Chinese Academy of Sciences (HKISI-CAS) - Surgical LLM and Image Segmentation, Supervisor: [Dr. Jinlin Wu](https://scholar.google.com.hk/citations?user=XujjZmUAAAAJ&hl=zh-CN) and [Dr. Zhen Chen](https://scholar.google.com/citations?user=oVG2zEkAAAAJ&hl=zh-CN)

-  **[Project Participant]** *2022.09-2023.08*, City University of Hong Kong - Financial Machine Translation, Supervisor: [Prof. Linqi Song](https://scholar.google.com/citations?user=UcGN3MoAAAAJ&hl=en)