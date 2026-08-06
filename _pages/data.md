---
permalink: /data/
title: "Data"
excerpt: "Open datasets for trustworthy AI, content detection, and AI safety research."
author_profile: false
---

<div class="data-page">
  <header class="data-hero">
    <div class="data-hero__mark" aria-hidden="true">🤗</div>
    <div class="data-hero__content">
      <div class="data-kicker">Open datasets on Hugging Face</div>
      <h1>Data</h1>
      <p>I champion open-source ethos. Below are datasets my collaborators and I have built together. Feel free to explore and use them in your work.</p>
    </div>
  </header>

  <section class="dataset-grid" aria-label="Research datasets">
    <article class="dataset-card dataset-card--pad">
      <div class="dataset-card__top">
        <span class="dataset-card__icon" aria-hidden="true">🧩</span>
        <div class="dataset-card__heading">
          <h2><a href="https://huggingface.co/datasets/Vincent-HKUSTGZ/PADBench">PADBench</a></h2>
          <div class="dataset-tags"><span>PEFT</span><span>Backdoor Detection</span><span>LLMs</span></div>
        </div>
      </div>
      <p>A benchmark of 13,300 benign and backdoored parameter-efficient adapters spanning multiple LLMs, PEFT methods, datasets, and attack strategies.</p>
      <div class="dataset-card__footer">
        <span class="dataset-download" title="Total downloads on Hugging Face"><span aria-hidden="true">↓</span> <strong data-hf-downloads="Vincent-HKUSTGZ/PADBench">291,327</strong> downloads</span>
        <div class="dataset-actions">
          <a href="https://arxiv.org/abs/2411.17453">Paper ↗</a>
          <a class="dataset-hf-link" href="https://huggingface.co/datasets/Vincent-HKUSTGZ/PADBench"><span aria-hidden="true">🤗</span> Dataset ↗</a>
        </div>
      </div>
    </article>

    <article class="dataset-card dataset-card--aigt">
      <div class="dataset-card__top">
        <span class="dataset-card__icon" aria-hidden="true">✍️</span>
        <div class="dataset-card__heading">
          <h2><a href="https://huggingface.co/datasets/tarryzhang/AIGTBench">AIGTBench</a></h2>
          <div class="dataset-tags"><span>AI-Generated Text</span><span>Social Media</span></div>
        </div>
      </div>
      <p>845,497 human- and AI-generated social media posts from Medium, Quora, and Reddit, covering several widely used language models.</p>
      <div class="dataset-card__footer">
        <span class="dataset-download" title="Total downloads on Hugging Face"><span aria-hidden="true">↓</span> <strong data-hf-downloads="tarryzhang/AIGTBench">1,500+</strong> downloads</span>
        <div class="dataset-actions">
          <a href="https://aclanthology.org/2025.acl-long.1120/">Paper ↗</a>
          <a class="dataset-hf-link" href="https://huggingface.co/datasets/tarryzhang/AIGTBench"><span aria-hidden="true">🤗</span> Dataset ↗</a>
        </div>
      </div>
    </article>

    <article class="dataset-card dataset-card--fragfake">
      <div class="dataset-card__top">
        <span class="dataset-card__icon" aria-hidden="true">🖼️</span>
        <div class="dataset-card__heading">
          <h2><a href="https://huggingface.co/datasets/Vincent-HKUSTGZ/FragFake">FragFake</a></h2>
          <div class="dataset-tags"><span>Edited Images</span><span>VLMs</span><span>Localization</span></div>
        </div>
      </div>
      <p>A fine-grained benchmark for detecting and localizing edits from modern image-editing models, organized across easy and hard settings.</p>
      <div class="dataset-card__footer">
        <span class="dataset-download" title="Total downloads on Hugging Face"><span aria-hidden="true">↓</span> <strong data-hf-downloads="Vincent-HKUSTGZ/FragFake">15,643</strong> downloads</span>
        <div class="dataset-actions">
          <a href="https://arxiv.org/abs/2505.15644">Paper ↗</a>
          <a class="dataset-hf-link" href="https://huggingface.co/datasets/Vincent-HKUSTGZ/FragFake"><span aria-hidden="true">🤗</span> Dataset ↗</a>
        </div>
      </div>
    </article>

    <article class="dataset-card dataset-card--mgt">
      <div class="dataset-card__top">
        <span class="dataset-card__icon" aria-hidden="true">🎓</span>
        <div class="dataset-card__heading">
          <h2><a href="https://huggingface.co/datasets/AITextDetect/AI_Polish_clean">MGT-Academic</a></h2>
          <div class="dataset-tags"><span>Academic Writing</span><span>Text Detection</span></div>
        </div>
      </div>
      <p>A large-scale collection of human- and machine-generated academic text, with 749K samples across STEM, social sciences, and humanities.</p>
      <div class="dataset-card__footer">
        <span class="dataset-download" title="Total downloads on Hugging Face"><span aria-hidden="true">↓</span> <strong data-hf-downloads="AITextDetect/AI_Polish_clean">526+</strong> downloads</span>
        <div class="dataset-actions">
          <a href="https://arxiv.org/abs/2412.17242">Paper ↗</a>
          <a class="dataset-hf-link" href="https://huggingface.co/datasets/AITextDetect/AI_Polish_clean"><span aria-hidden="true">🤗</span> Dataset ↗</a>
        </div>
      </div>
    </article>
  </section>

  <p class="data-footnote">Download counts are refreshed from Hugging Face when the page loads.</p>
</div>

<script>
  (function () {
    var counters = document.querySelectorAll('[data-hf-downloads]');
    Array.prototype.forEach.call(counters, function (counter) {
      var datasetId = counter.getAttribute('data-hf-downloads');
      var endpoint = 'https://huggingface.co/api/datasets/' + datasetId + '?expand=downloadsAllTime';

      fetch(endpoint)
        .then(function (response) {
          if (!response.ok) throw new Error('Hugging Face API request failed');
          return response.json();
        })
        .then(function (data) {
          if (typeof data.downloadsAllTime === 'number') {
            counter.textContent = data.downloadsAllTime.toLocaleString('en-US');
          }
        })
        .catch(function () {
          // Keep the fallback value already rendered in the page.
        });
    });
  })();
</script>
