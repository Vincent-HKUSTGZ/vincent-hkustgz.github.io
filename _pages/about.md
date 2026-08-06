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
    <p class="profile-header__aka">Vincent</p>
    <p class="profile-header__role">PhD Candidate in Data Science and Analytics</p>
    <p class="profile-header__aff"><a href="https://www.hkust-gz.edu.cn/" class="text-plain">The Hong Kong University of Science and Technology (Guangzhou)</a></p>
    <p class="profile-header__links">
      <a href="mailto:zsun344@connect.hkust-gz.edu.cn"><i class="fas fa-envelope profile-link-icon" aria-hidden="true"></i>Email</a>
      &nbsp;/&nbsp;
      <a href="https://scholar.google.com/citations?user=7ir2zYsAAAAJ&hl=en"><i class="ai ai-google-scholar profile-link-icon" aria-hidden="true"></i>Scholar</a>
      &nbsp;/&nbsp;
      <a href="https://github.com/Vincent-HKUSTGZ"><i class="fab fa-github profile-link-icon" aria-hidden="true"></i>GitHub</a>
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
    Hello! I'm a PhD candidate in Data Science and Analytics at
    <a href="https://www.hkust-gz.edu.cn/">The Hong Kong University of Science and Technology (Guangzhou)</a>.
    I am advised by Prof. <a href="https://xinleihe.github.io/">Xinlei He</a>,
    with primary supervision from Prof. <a href="https://sites.google.com/ucsc.edu/jiahengwei">Jiaheng Wei</a>
    and co-supervision from Prof. Yutao Yue at HKUST(GZ).
  </p>
  <p>
    My research interests lie in <strong>Trustworthy AI</strong>, specifically focusing on the following directions:
  </p>

  <div class="research-pillars">
    <div class="pillar pillar--security">
      <div class="pillar-icon" aria-hidden="true"><img src="{{ '/images/icons/security-privacy.png' | relative_url }}" alt=""></div>
      <div class="pillar-title">Security &amp; Privacy</div>
      <div class="pillar-sub">Studying backdoors, jailbreaks, and privacy risks in modern AI models.</div>
    </div>
    <div class="pillar pillar--aigt">
      <div class="pillar-icon" aria-hidden="true"><img src="{{ '/images/icons/content-detection.png' | relative_url }}" alt=""></div>
      <div class="pillar-title">AI-Generated Content Detection</div>
      <div class="pillar-sub">Detecting and monitoring machine-generated text and multimodal content in the wild.</div>
    </div>
    <div class="pillar pillar--safety">
      <div class="pillar-icon" aria-hidden="true"><img src="{{ '/images/icons/ai-for-safety.png' | relative_url }}" alt=""></div>
      <div class="pillar-title">AI For Safety</div>
      <div class="pillar-sub">Mitigating AI-driven harms and improving the safety of deployed systems.</div>
    </div>
  </div>
</section>

<span class="anchor" id="news"></span>
<section class="page-section">
  <h2>News</h2>
  <ul class="list-compact">
    <li><span class="news-date">[2026.06]</span> <span class="news-icon" aria-hidden="true">✅</span>I passed the <strong>PhD Qualifying Examination</strong> at HKUST(GZ).</li>
    <li><span class="news-date">[2026.01]</span> <span class="news-icon" aria-hidden="true">🔊</span><a href="https://openreview.net/forum?id=DJkQ236C8B">JALMBench</a> was accepted at <strong>ICLR 2026</strong>.</li>
    <li><span class="news-date">[2025.12]</span> <span class="news-icon" aria-hidden="true">🏆</span>I received <strong>First Prize</strong> in the <a href="https://kjj.wuhu.gov.cn/gg/gzdt/8894191.html">Offline Testing Algorithm Competition of the 2025 China Intelligent Vehicle Future Challenge</a>.</li>
    <li><span class="news-date">[2025.12]</span> <span class="news-icon" aria-hidden="true">🎙️</span><a href="https://arxiv.org/abs/2512.19058">6DAttack</a> was accepted at <strong>AAAI 2026</strong> as an Oral presentation.</li>
    <li><span class="news-date">[2025.12]</span> <span class="news-icon" aria-hidden="true">🏅</span>I received the <strong>2025 DSA Excellent Research Award</strong>.</li>
    <li><span class="news-date">[2025.09]</span> <span class="news-icon" aria-hidden="true">📊</span><a href="https://arxiv.org/abs/2502.21059">FC-Attack</a> was accepted at <strong>EMNLP 2025 Findings</strong>.</li>
    <li><span class="news-date">[2025.09]</span> <span class="news-icon" aria-hidden="true">🔍</span><a href="https://arxiv.org/abs/2509.18874">CHASM</a> was accepted at <strong>NeurIPS 2025</strong>.</li>
    <li><span class="news-date">[2025.06]</span> <span class="news-icon" aria-hidden="true">🛡️</span><a href="https://arxiv.org/abs/2502.04951">Unsafe LLM-Based Search</a> was accepted at <strong>USENIX Security 2025</strong>.</li>
    <li><span class="news-date">[2025.05]</span> <span class="news-icon" aria-hidden="true">✨</span><a href="https://aclanthology.org/2025.acl-long.1120/">AIGT on Social Media</a> was accepted at <strong>ACL 2025</strong>, and <a href="https://arxiv.org/abs/2412.17242">MGT Generalization</a> plus <a href="https://arxiv.org/abs/2503.08708">TH-Bench</a> were accepted at <strong>KDD 2025</strong>.</li>
    <li><span class="news-date">[2025.03]</span> <span class="news-icon" aria-hidden="true">🔐</span><a href="https://arxiv.org/abs/2411.17453">PEFTGuard</a> was accepted at <strong>IEEE S&amp;P 2025</strong>.</li>
  </ul>
  <div id="hidden-news" class="is-hidden">
    <ul class="list-compact">
      <li><span class="news-date">[2024.11]</span> <span class="news-icon" aria-hidden="true">🏆</span>AdSpectorX received the <strong>Best Paper Award</strong> at SENSYS-SocialMeta 2024.</li>
      <li><span class="news-date">[2024.06]</span> <span class="news-icon" aria-hidden="true">🎓</span>I received my firm PhD offer from HKUST(GZ).</li>
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
      <div class="pub-meta"><span class="pub-year">2025</span><span class="pub-venue">IEEE S&amp;P</span></div>
      <div class="pub-content">
        <div class="pub-title"><a href="https://arxiv.org/abs/2411.17453">PEFTGuard: Detecting Backdoor Attacks Against Parameter-Efficient Fine-Tuning</a></div>
        <div class="pub-authors"><strong>Zhen Sun</strong>, Tianshuo Cong, Yule Liu, Chenhao Lin, Xinlei He, Rongmao Chen, Xingshuo Han, Xinyi Huang.</div>
      </div>
    </div>

    <div class="pub-entry">
      <div class="pub-meta"><span class="pub-year">2025</span><span class="pub-venue">ACL</span></div>
      <div class="pub-content">
        <div class="pub-title"><a href="https://aclanthology.org/2025.acl-long.1120/">Are We in the AI-Generated Text World Already? Quantifying and Monitoring AIGT on Social Media</a></div>
        <div class="pub-authors"><strong>Zhen Sun<sup>*</sup></strong>, Zongmin Zhang<sup>*</sup>, Xinyue Shen, Ziyi Zhang, Yule Liu, Michael Backes, Yang Zhang, Xinlei He.</div>
      </div>
    </div>

    <div class="pub-entry">
      <div class="pub-meta"><span class="pub-year">2025</span><span class="pub-venue">EMNLP Findings</span></div>
      <div class="pub-content">
        <div class="pub-title"><a href="https://arxiv.org/abs/2502.21059">FC-Attack: Jailbreaking Large Vision-Language Models via Auto-Generated Flowcharts</a></div>
        <div class="pub-authors">Ziyi Zhang<sup>*</sup>, <strong>Zhen Sun</strong><sup>*</sup>, Zongmin Zhang, Jihui Guo, Xinlei He.</div>
      </div>
    </div>

    <div class="pub-entry">
      <div class="pub-meta"><span class="pub-year">2026</span><span class="pub-venue">ICLR</span></div>
      <div class="pub-content">
        <div class="pub-title"><a href="https://openreview.net/forum?id=DJkQ236C8B">JALMBench: Benchmarking Jailbreak Vulnerabilities in Audio Language Models</a></div>
        <div class="pub-authors">Zifan Peng, Yule Liu, <strong>Zhen Sun</strong>, Mingchen Li, Zeren Luo, Jingyi Zheng, Wenhan Dong, Xinlei He, Xuechao Wang, Yingjie Xue, Shengmin Xu, Xinyi Huang.</div>
      </div>
    </div>

    <div class="pub-entry">
      <div class="pub-meta"><span class="pub-year">2025</span><span class="pub-venue">USENIX Security</span></div>
      <div class="pub-content">
        <div class="pub-title"><a href="https://arxiv.org/abs/2502.04951">Unsafe LLM-Based Search: Quantitative Analysis and Mitigation of Safety Risks in AI Web Search</a></div>
        <div class="pub-authors">Zeren Luo, Zifan Peng, Yule Liu, <strong>Zhen Sun</strong>, Mingchen Li, Jingyi Zheng, Xinlei He.</div>
      </div>
    </div>

    <div class="pub-entry">
      <div class="pub-meta"><span class="pub-year">2025</span><span class="pub-venue">NeurIPS</span></div>
      <div class="pub-content">
        <div class="pub-title"><a href="https://arxiv.org/abs/2509.18874">CHASM: Unveiling Covert Advertisements on Chinese Social Media</a></div>
        <div class="pub-authors">Jingyi Zheng, Tianyi Hu, Yule Liu, <strong>Zhen Sun</strong>, Zongmin Zhang, Zifan Peng, Wenhan Dong, Xinlei He.</div>
      </div>
    </div>

    <div class="pub-entry">
      <div class="pub-meta"><span class="pub-year">2026</span><span class="pub-venue">AAAI · Oral</span></div>
      <div class="pub-content">
        <div class="pub-title"><a href="https://arxiv.org/abs/2512.19058">6DAttack: Backdoor Attacks in the 6DoF Pose Estimation</a></div>
        <div class="pub-authors">Jihui Guo, Zongmin Zhang, <strong>Zhen Sun</strong>, Yuhao Yang, Jinlin Wu, Fu Zhang, Xinlei He.</div>
      </div>
    </div>

    <div class="pub-entry">
      <div class="pub-meta"><span class="pub-year">2025</span><span class="pub-venue">KDD</span></div>
      <div class="pub-content">
        <div class="pub-title"><a href="https://arxiv.org/abs/2503.08708">TH-Bench: Evaluating Evading Attacks via Humanizing AI Text on Machine-Generated Text Detectors</a></div>
        <div class="pub-authors">Jingyi Zheng, Junfeng Wang, <strong>Zhen Sun</strong>, Wenhan Dong, Yule Liu, Xinlei He.</div>
      </div>
    </div>

    <div class="pub-entry">
      <div class="pub-meta"><span class="pub-year">2025</span><span class="pub-venue">KDD</span></div>
      <div class="pub-content">
        <div class="pub-title"><a href="https://arxiv.org/abs/2412.17242">On the Generalization and Adaptation Ability of Machine-Generated Text Detectors in Academic Writing</a></div>
        <div class="pub-authors">Yule Liu, Zhiyuan Zhong, Yifan Liao, <strong>Zhen Sun</strong>, Jingyi Zheng, Jiaheng Wei, Qingyuan Gong, Fenghua Tong, Yang Chen, Yang Zhang, Xinlei He.</div>
      </div>
    </div>

  </div>
</section>

<span class="anchor" id="services"></span>
<section class="page-section">
  <h2>Services</h2>
  <ul class="service-list">
    <li>
      <strong>Program Committee</strong>
      <ul>
        <li><span class="service-year">2026</span> ACL ARR, AAAI, ACM MM</li>
        <li><span class="service-year">2025</span> AAAI, ACM MM, WWW (Web for Good)</li>
      </ul>
    </li>
    <li><strong>Journal Reviewers</strong>: IEEE TDSC, IEEE TIFS, ACM TOPS, IJHCI</li>
  </ul>
</section>

<span class="anchor" id="honors"></span>
<section class="page-section">
  <h2>Selected Awards &amp; Honors</h2>
  <ul class="list-compact">
    <li><strong>First Prize</strong>, <a href="https://kjj.wuhu.gov.cn/gg/gzdt/8894191.html">Offline Testing Algorithm Competition, 2025 China Intelligent Vehicle Future Challenge</a>, 2025</li>
    <li><strong>DSA Excellent Research Award</strong>, 2025</li>
    <li><strong>Best Paper Award</strong>, SENSYS-SocialMeta 2024</li>
    <li>Kaggle Competitions Expert (<a href="https://www.kaggle.com/rdxsun">Vincent Sirius</a>)</li>
    <li><strong>BUPT Third-class Scholarship &amp; Excellent Student Leader</strong>, 2019 / 2020 / 2021</li>
  </ul>
</section>

<span class="anchor" id="education"></span>
<section class="page-section">
  <h2>Education</h2>
  <div class="timeline">
    <div class="timeline-item">
      <div class="timeline-item__logo">
        <img src="{{ '/images/logos/hkustgz.png' | relative_url }}" alt="HKUST(GZ)">
      </div>
      <div class="timeline-item__body">
        <div class="timeline-item__title">PhD in Data Science and Analytics</div>
        <div class="timeline-item__org"><a href="https://www.hkust-gz.edu.cn/">The Hong Kong University of Science and Technology (Guangzhou)</a></div>
        <div class="timeline-item__date">2024.08 – present</div>
      </div>
    </div>
    <div class="timeline-item">
      <div class="timeline-item__logo">
        <img src="{{ '/images/logos/cityu.svg' | relative_url }}" alt="City University of Hong Kong">
      </div>
      <div class="timeline-item__body">
        <div class="timeline-item__title">MSc in Computer Science</div>
        <div class="timeline-item__org"><a href="https://www.cityu.edu.hk/">City University of Hong Kong</a></div>
        <div class="timeline-item__date">2022.08 – 2023.10</div>
      </div>
    </div>
    <div class="timeline-item">
      <div class="timeline-item__logo">
        <img src="{{ '/images/logos/bupt.png' | relative_url }}" alt="BUPT">
      </div>
      <div class="timeline-item__body">
        <div class="timeline-item__title">BSc in Computer Science and Technology</div>
        <div class="timeline-item__org"><a href="https://www.bupt.edu.cn/">Beijing University of Posts and Telecommunications</a></div>
        <div class="timeline-item__date">2018.09 – 2022.07</div>
      </div>
    </div>
  </div>
</section>

<span class="anchor" id="experience"></span>
<section class="page-section">
  <h2>Experience</h2>
  <div class="timeline">
    <div class="timeline-item">
      <div class="timeline-item__logo">
        <img src="{{ '/images/logos/ant.svg' | relative_url }}" alt="Ant Group">
      </div>
      <div class="timeline-item__body">
        <div class="timeline-item__title">Research Intern</div>
        <div class="timeline-item__org">Ant Group</div>
        <div class="timeline-item__date">2026.03 – present</div>
        <div class="timeline-item__desc">Supervisor: <a href="https://zicofish.github.io/">Zhicong Huang</a>.</div>
      </div>
    </div>
    <div class="timeline-item">
      <div class="timeline-item__logo">
        <img src="{{ '/images/logos/cas.png' | relative_url }}" alt="CAS">
      </div>
      <div class="timeline-item__body">
        <div class="timeline-item__title">Research Assistant</div>
        <div class="timeline-item__org">Centre for Artificial Intelligence and Robotics (CAIR), Hong Kong Institute of Science &amp; Innovation, Chinese Academy of Sciences (HKISI-CAS)</div>
        <div class="timeline-item__date">2023.06 – 2024.05</div>
        <div class="timeline-item__desc">Worked on surgical LLMs and image segmentation. Supervisor: <a href="https://scholar.google.com.hk/citations?user=XujjZmUAAAAJ&hl=zh-CN">Dr. Jinlin Wu</a>.</div>
      </div>
    </div>
    <div class="timeline-item">
      <div class="timeline-item__logo">
        <img src="{{ '/images/logos/cityu.svg' | relative_url }}" alt="City University of Hong Kong">
      </div>
      <div class="timeline-item__body">
        <div class="timeline-item__title">Project Participant</div>
        <div class="timeline-item__org"><a href="https://www.cityu.edu.hk/">City University of Hong Kong</a></div>
        <div class="timeline-item__date">2022.09 – 2023.08</div>
        <div class="timeline-item__desc">Worked on financial machine translation. Supervisor: <a href="https://scholar.google.com/citations?user=UcGN3MoAAAAJ&hl=en">Prof. Linqi Song</a>.</div>
      </div>
    </div>
  </div>
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
