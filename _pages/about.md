---
permalink: /
title: ""
excerpt: ""
author_profile: false
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

<div class="profile-header">
  <div class="profile-header__image">
    <img src="{{ '/images/me.png' | relative_url }}" alt="Zhen Sun">
  </div>
  <div class="profile-header__info">
    <h1>Zhen Sun</h1>
    <p class="profile-header__role">PhD Student in Data Science and Analytics</p>
    <p class="profile-header__aff"><a href="https://www.hkust-gz.edu.cn/" class="text-plain">The Hong Kong University of Science and Technology (Guangzhou)</a></p>
    <p class="profile-header__links">
      <a href="mailto:zsun344@connect.hkust-gz.edu.cn">Email</a>
      &nbsp;/&nbsp;
      <a href="https://scholar.google.com/citations?user=7ir2zYsAAAAJ&hl=en">Scholar</a>
      &nbsp;/&nbsp;
      <a href="https://github.com/Vincent-HKUSTGZ">GitHub</a>
    </p>
    <p class="profile-header__badge">
      <a href="https://scholar.google.com/citations?user=7ir2zYsAAAAJ&hl=en">
        <img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations" alt="Google Scholar citations">
      </a>
    </p>
  </div>
</div>

<span class="anchor" id="research"></span>
<section class="page-section">
  <p>
    Hello! I'm a PhD student in Data Science and Analytics at
    <a href="https://www.hkust-gz.edu.cn/">The Hong Kong University of Science and Technology (Guangzhou)</a>.
    I am advised by Prof. <a href="https://xinleihe.github.io/">Xinlei He</a>,
    with primary supervision from Prof. <a href="https://sites.google.com/ucsc.edu/jiahengwei">Jiaheng Wei</a>
    and co-supervision from Prof. Yutao Yue at HKUST(GZ).
  </p>
  <p>
    My research interests lie in <strong>Trustworthy AI</strong>, specifically focusing on the following directions:
  </p>

  <div class="research-pillars">
    <div class="pillar pillar--trust">
      <div class="pillar-title">Trustworthy AI</div>
      <div class="pillar-sub">Building reliable and responsible AI systems across the model lifecycle.</div>
    </div>
    <div class="pillar pillar--security">
      <div class="pillar-title">AI Security &amp; Privacy</div>
      <div class="pillar-sub">Studying backdoors, jailbreaks, and privacy risks in modern AI models.</div>
    </div>
    <div class="pillar pillar--aigt">
      <div class="pillar-title">AI-Generated Content Detection</div>
      <div class="pillar-sub">Detecting and monitoring machine-generated text and multimodal content in the wild.</div>
    </div>
    <div class="pillar pillar--safety">
      <div class="pillar-title">AI For Safety</div>
      <div class="pillar-sub">Mitigating AI-driven harms and improving the safety of deployed systems.</div>
    </div>
  </div>
</section>

<span class="anchor" id="news"></span>
<section class="page-section">
  <h2>News</h2>
  <ul class="list-compact">
    <li><span class="news-date">[2026.01]</span> <a href="https://openreview.net/forum?id=DJkQ236C8B">JALMBench</a> was accepted at <strong>ICLR 2026</strong>.</li>
    <li><span class="news-date">[2025.12]</span> <a href="https://arxiv.org/abs/2512.19058">6DAttack</a> was accepted at <strong>AAAI 2026</strong> as an Oral presentation.</li>
    <li><span class="news-date">[2025.12]</span> I received the <strong>2025 DSA Excellent Research Award</strong>.</li>
    <li><span class="news-date">[2025.09]</span> <a href="https://arxiv.org/abs/2502.21059">FC-Attack</a> was accepted at <strong>EMNLP 2025 Findings</strong>.</li>
    <li><span class="news-date">[2025.09]</span> <a href="https://arxiv.org/abs/2509.18874">CHASM</a> was accepted at <strong>NeurIPS 2025</strong>.</li>
    <li><span class="news-date">[2025.06]</span> <a href="https://arxiv.org/abs/2502.04951">Unsafe LLM-Based Search</a> was accepted at <strong>USENIX Security 2025</strong>.</li>
    <li><span class="news-date">[2025.05]</span> <a href="https://aclanthology.org/2025.acl-long.1120/">AIGT on Social Media</a> was accepted at <strong>ACL 2025</strong>, and <a href="https://arxiv.org/abs/2412.17242">MGT Generalization</a> plus <a href="https://arxiv.org/abs/2503.08708">TH-Bench</a> were accepted at <strong>KDD 2025</strong>.</li>
    <li><span class="news-date">[2025.03]</span> <a href="https://arxiv.org/abs/2411.17453">PEFTGuard</a> was accepted at <strong>IEEE S&amp;P 2025</strong>.</li>
  </ul>
  <div id="hidden-news" class="is-hidden">
    <ul class="list-compact">
      <li><span class="news-date">[2024.11]</span> AdSpectorX received the <strong>Best Paper Award</strong> at SENSYS-SocialMeta 2024.</li>
      <li><span class="news-date">[2024.06]</span> I received my firm PhD offer from HKUST(GZ).</li>
    </ul>
  </div>
  <p><span class="news-toggle" onclick="toggleNews()">Show more news</span></p>
</section>

<span class="anchor" id="publications"></span>
<section class="page-section">
  <h2>Selected Papers</h2>
  <p class="section-note"><sup>*</sup> denotes equal contribution. <sup>&dagger;</sup> denotes corresponding author. The complete list can be found at <a href="https://scholar.google.com/citations?user=7ir2zYsAAAAJ&hl=en">Google Scholar</a>.</p>

  <div class="pub-list">
    <div class="pub-entry">
      <div class="pub-meta"><span class="pub-year">2026</span><span class="pub-venue">ICLR</span><span class="pub-tag">CCF-A</span></div>
      <div class="pub-content">
        <div class="pub-title"><a href="https://openreview.net/forum?id=DJkQ236C8B">JALMBench: Benchmarking Jailbreak Vulnerabilities in Audio Language Models</a></div>
        <div class="pub-authors">Zifan Peng, Yule Liu, <strong>Zhen Sun</strong>, Mingchen Li, Zeren Luo, Jingyi Zheng, Wenhan Dong, Xinlei He, Xuechao Wang, Yingjie Xue, Shengmin Xu, Xinyi Huang.</div>
        <div class="pub-links"><a href="https://openreview.net/forum?id=DJkQ236C8B">PDF</a></div>
      </div>
    </div>

    <div class="pub-entry">
      <div class="pub-meta"><span class="pub-year">2026</span><span class="pub-venue">AAAI</span><span class="pub-tag">CCF-A · Oral</span></div>
      <div class="pub-content">
        <div class="pub-title"><a href="https://arxiv.org/abs/2512.19058">6DAttack: Backdoor Attacks in the 6DoF Pose Estimation</a></div>
        <div class="pub-authors">Jihui Guo, Zongmin Zhang, <strong>Zhen Sun</strong>, Yuhao Yang, Jinlin Wu, Fu Zhang, Xinlei He.</div>
        <div class="pub-links"><a href="https://arxiv.org/abs/2512.19058">PDF</a></div>
      </div>
    </div>

    <div class="pub-entry">
      <div class="pub-meta"><span class="pub-year">2025</span><span class="pub-venue">IEEE S&amp;P</span><span class="pub-tag">CCF-A</span></div>
      <div class="pub-content">
        <div class="pub-title"><a href="https://arxiv.org/abs/2411.17453">PEFTGuard: Detecting Backdoor Attacks Against Parameter-Efficient Fine-Tuning</a></div>
        <div class="pub-authors"><strong>Zhen Sun</strong>, Tianshuo Cong, Yule Liu, Chenhao Lin, Xinlei He, Rongmao Chen, Xingshuo Han, Xinyi Huang.</div>
        <div class="pub-links"><a href="https://arxiv.org/abs/2411.17453">PDF</a></div>
      </div>
    </div>

    <div class="pub-entry">
      <div class="pub-meta"><span class="pub-year">2025</span><span class="pub-venue">ACL</span><span class="pub-tag">CCF-A</span></div>
      <div class="pub-content">
        <div class="pub-title"><a href="https://aclanthology.org/2025.acl-long.1120/">Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media</a></div>
        <div class="pub-authors"><strong>Zhen Sun<sup>*</sup></strong>, Zongmin Zhang<sup>*</sup>, Xinyue Shen, Ziyi Zhang, Yule Liu, Michael Backes, Yang Zhang, Xinlei He.</div>
        <div class="pub-links"><a href="https://aclanthology.org/2025.acl-long.1120/">PDF</a></div>
      </div>
    </div>

    <div class="pub-entry">
      <div class="pub-meta"><span class="pub-year">2025</span><span class="pub-venue">USENIX Security</span><span class="pub-tag">CCF-A</span></div>
      <div class="pub-content">
        <div class="pub-title"><a href="https://arxiv.org/abs/2502.04951">Unsafe LLM-Based Search: Quantitative Analysis and Mitigation of Safety Risks in AI Web Search</a></div>
        <div class="pub-authors">Zeren Luo, Zifan Peng, Yule Liu, <strong>Zhen Sun</strong>, Mingchen Li, Jingyi Zheng, Xinlei He.</div>
        <div class="pub-links"><a href="https://arxiv.org/abs/2502.04951">PDF</a></div>
      </div>
    </div>

    <div class="pub-entry">
      <div class="pub-meta"><span class="pub-year">2025</span><span class="pub-venue">NeurIPS</span><span class="pub-tag">CCF-A</span></div>
      <div class="pub-content">
        <div class="pub-title"><a href="https://arxiv.org/abs/2509.18874">CHASM: Unveiling Covert Advertisements on Chinese Social Media</a></div>
        <div class="pub-authors">Jingyi Zheng, Tianyi Hu, Yule Liu, <strong>Zhen Sun</strong>, Zongmin Zhang, Zifan Peng, Wenhan Dong, Xinlei He.</div>
        <div class="pub-links"><a href="https://arxiv.org/abs/2509.18874">PDF</a></div>
      </div>
    </div>

    <div class="pub-entry">
      <div class="pub-meta"><span class="pub-year">2025</span><span class="pub-venue">KDD</span><span class="pub-tag">CCF-A</span></div>
      <div class="pub-content">
        <div class="pub-title"><a href="https://arxiv.org/abs/2503.08708">TH-Bench: Evaluating Evading Attacks via Humanizing AI Text on Machine-Generated Text Detectors</a></div>
        <div class="pub-authors">Jingyi Zheng, Junfeng Wang, <strong>Zhen Sun</strong>, Wenhan Dong, Yule Liu, Xinlei He.</div>
        <div class="pub-links"><a href="https://arxiv.org/abs/2503.08708">PDF</a></div>
      </div>
    </div>

    <div class="pub-entry">
      <div class="pub-meta"><span class="pub-year">2025</span><span class="pub-venue">KDD</span><span class="pub-tag">CCF-A</span></div>
      <div class="pub-content">
        <div class="pub-title"><a href="https://arxiv.org/abs/2412.17242">On the Generalization and Adaptation Ability of Machine-Generated Text Detectors in Academic Writing</a></div>
        <div class="pub-authors">Yule Liu, Zhiyuan Zhong, Yifan Liao, <strong>Zhen Sun</strong>, Jingyi Zheng, Jiaheng Wei, Qingyuan Gong, Fenghua Tong, Yang Chen, Yang Zhang, Xinlei He.</div>
        <div class="pub-links"><a href="https://arxiv.org/abs/2412.17242">PDF</a></div>
      </div>
    </div>

    <div class="pub-entry">
      <div class="pub-meta"><span class="pub-year">2025</span><span class="pub-venue">EMNLP Findings</span><span class="pub-tag">CCF-B</span></div>
      <div class="pub-content">
        <div class="pub-title"><a href="https://arxiv.org/abs/2502.21059">FC-Attack: Jailbreaking Large Vision-Language Models via Auto-Generated Flowcharts</a></div>
        <div class="pub-authors">Ziyi Zhang<sup>*</sup>, <strong>Zhen Sun</strong><sup>*</sup>, Zongmin Zhang, Jihui Guo, Xinlei He.</div>
        <div class="pub-links"><a href="https://arxiv.org/abs/2502.21059">PDF</a></div>
      </div>
    </div>

    <div class="pub-entry">
      <div class="pub-meta"><span class="pub-year">2024</span><span class="pub-venue">SENSYS-SocialMeta</span><span class="pub-tag">Best Paper</span></div>
      <div class="pub-content">
        <div class="pub-title">AdSpectorX: A Multimodal Expert Spector for Covert Advertising Detection on Chinese Social Media</div>
        <div class="pub-authors">Zongmin Zhang, Yujie Han, Zhou Zhang, Yule Liu, Jingyi Zheng, <strong>Zhen Sun</strong><sup>&dagger;</sup>.</div>
        <div class="pub-award">Best Paper Award</div>
      </div>
    </div>
  </div>
</section>

<span class="anchor" id="services"></span>
<section class="page-section">
  <h2>Services</h2>
  <ul class="list-compact">
    <li><strong>Conference PC / Reviewer</strong>: The Web Conference 2025 Web4Good Track, AAAI, ACM MM, ICML, CVPR, ACL, EMNLP, SaTML, EuroS&amp;P, AsiaCCS</li>
    <li><strong>Journal Reviewer</strong>: IEEE TDSC, IEEE TIFS, ACM TOPS, IJHCI</li>
  </ul>
</section>

<span class="anchor" id="honors"></span>
<section class="page-section">
  <h2>Selected Awards &amp; Honors</h2>
  <ul class="list-compact">
    <li><strong>DSA Excellent Research Award</strong>, 2025</li>
    <li><strong>Best Paper Award</strong>, SENSYS-SocialMeta 2024</li>
    <li>Kaggle Competitions Expert (<a href="https://www.kaggle.com/rdxsun">Vincent Sirius</a>)</li>
    <li><strong>MCM/ICM Meritorious Winner</strong>, 2020.04</li>
    <li>Third-class Scholarship of BUPT, 2019 / 2020 / 2021</li>
    <li>Excellent Student Leader of BUPT, 2019 / 2020 / 2021</li>
  </ul>
</section>

<span class="anchor" id="education"></span>
<section class="page-section">
  <h2>Education</h2>
  <ul class="list-compact">
    <li><strong>2024.08–present</strong>, PhD in Data Science and Analytics, The Hong Kong University of Science and Technology (Guangzhou)</li>
    <li><strong>2022.08–2023.10</strong>, MSc in Computer Science, City University of Hong Kong</li>
    <li><strong>2018.09–2022.07</strong>, BSc in Computer Science and Technology, Beijing University of Posts and Telecommunications</li>
  </ul>
</section>

<span class="anchor" id="experience"></span>
<section class="page-section">
  <h2>Experience</h2>
  <ul class="list-compact">
    <li><strong>Research Assistant</strong>, 2023.06–2024.05, Centre for Artificial Intelligence and Robotics (CAIR), Hong Kong Institute of Science &amp; Innovation, Chinese Academy of Sciences (HKISI-CAS). Worked on surgical LLMs and image segmentation. Supervisor: <a href="https://scholar.google.com.hk/citations?user=XujjZmUAAAAJ&hl=zh-CN">Dr. Jinlin Wu</a>.</li>
    <li><strong>Project Participant</strong>, 2022.09–2023.08, City University of Hong Kong. Worked on financial machine translation. Supervisor: <a href="https://scholar.google.com/citations?user=UcGN3MoAAAAJ&hl=en">Prof. Linqi Song</a>.</li>
  </ul>
</section>

<script type="text/javascript">
  function toggleNews() {
    var hidden = document.getElementById('hidden-news');
    var toggle = document.querySelector('.news-toggle');
    if (hidden.classList.contains('is-hidden')) {
      hidden.classList.remove('is-hidden');
      toggle.textContent = 'Show less news';
    } else {
      hidden.classList.add('is-hidden');
      toggle.textContent = 'Show more news';
    }
  }
</script>
