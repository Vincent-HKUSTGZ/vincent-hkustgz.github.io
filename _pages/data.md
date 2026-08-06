---
permalink: /data/
title: "Data"
excerpt: "Open datasets for trustworthy AI, content detection, and AI safety research."
author_profile: false
---

<div class="data-page">
  <header class="data-hero">
    <div class="data-kicker"><span aria-hidden="true">🤗</span> Hugging Face Collection</div>
    <h1>Data</h1>
    <p>I champion open-source ethos. Below are datasets my collaborators and I have built together. Feel free to explore and use them in your work.</p>
  </header>

  <div class="data-section-heading">
    <h2><span aria-hidden="true">🌐</span> Open Research Datasets</h2>
    <p>Resources for trustworthy AI, content detection, and AI safety.</p>
  </div>

  <section class="dataset-grid" aria-label="Research datasets">
    <article class="dataset-card dataset-card--pad">
      <div class="dataset-card__top">
        <div class="dataset-card__identity">
          <span class="dataset-card__icon" aria-hidden="true">🧩</span>
          <div class="dataset-card__heading">
            <h3><a href="https://huggingface.co/datasets/Vincent-HKUSTGZ/PADBench">PADBench</a></h3>
            <div class="dataset-tags"><span>PEFT</span><span>Backdoors</span><span>LLMs</span></div>
          </div>
        </div>
        <div class="dataset-actions">
          <span class="dataset-download" title="Total downloads on Hugging Face"><span aria-hidden="true">↓</span> <strong data-hf-downloads="Vincent-HKUSTGZ/PADBench">291,327</strong></span>
          <a href="https://arxiv.org/abs/2411.17453">Paper ↗</a>
          <a class="dataset-hf-link" href="https://huggingface.co/datasets/Vincent-HKUSTGZ/PADBench"><span aria-hidden="true">🤗</span> Dataset ↗</a>
        </div>
      </div>
      <p class="dataset-description"><span>Description</span>A benchmark of benign and backdoored parameter-efficient adapters spanning multiple LLMs, PEFT methods, datasets, and attack strategies.</p>
      <div class="dataset-meta">
        <div><span>Source</span>Multiple LLMs and PEFT configurations</div>
        <div><span>Size</span>13,300 adapters</div>
      </div>
    </article>

    <article class="dataset-card dataset-card--aigt">
      <div class="dataset-card__top">
        <div class="dataset-card__identity">
          <span class="dataset-card__icon" aria-hidden="true">✍️</span>
          <div class="dataset-card__heading">
            <h3><a href="https://huggingface.co/datasets/tarryzhang/AIGTBench">AIGTBench</a></h3>
            <div class="dataset-tags"><span>AI Text</span><span>Social Media</span><span>Detection</span></div>
          </div>
        </div>
        <div class="dataset-actions">
          <span class="dataset-download" title="Total downloads on Hugging Face"><span aria-hidden="true">↓</span> <strong data-hf-downloads="tarryzhang/AIGTBench">1,924</strong></span>
          <a href="https://aclanthology.org/2025.acl-long.1120/">Paper ↗</a>
          <a class="dataset-hf-link" href="https://huggingface.co/datasets/tarryzhang/AIGTBench"><span aria-hidden="true">🤗</span> Dataset ↗</a>
        </div>
      </div>
      <p class="dataset-description"><span>Description</span>Human- and AI-generated social media posts covering several widely used language models.</p>
      <div class="dataset-meta">
        <div><span>Source</span>Medium, Quora, Reddit</div>
        <div><span>Size</span>845,497 posts</div>
      </div>
    </article>

    <article class="dataset-card dataset-card--fragfake">
      <div class="dataset-card__top">
        <div class="dataset-card__identity">
          <span class="dataset-card__icon" aria-hidden="true">🖼️</span>
          <div class="dataset-card__heading">
            <h3><a href="https://huggingface.co/datasets/Vincent-HKUSTGZ/FragFake">FragFake</a></h3>
            <div class="dataset-tags"><span>Edited Images</span><span>VLMs</span><span>Localization</span></div>
          </div>
        </div>
        <div class="dataset-actions">
          <span class="dataset-download" title="Total downloads on Hugging Face"><span aria-hidden="true">↓</span> <strong data-hf-downloads="Vincent-HKUSTGZ/FragFake">15,643</strong></span>
          <a href="https://arxiv.org/abs/2505.15644">Paper ↗</a>
          <a class="dataset-hf-link" href="https://huggingface.co/datasets/Vincent-HKUSTGZ/FragFake"><span aria-hidden="true">🤗</span> Dataset ↗</a>
        </div>
      </div>
      <p class="dataset-description"><span>Description</span>A fine-grained benchmark for detecting and localizing edits from modern image-editing models.</p>
      <div class="dataset-meta">
        <div><span>Source</span>Gemini-IG, GoT, MagicBrush, UltraEdit</div>
        <div><span>Size</span>32,326 image-text examples</div>
      </div>
    </article>

    <article class="dataset-card dataset-card--mgt">
      <div class="dataset-card__top">
        <div class="dataset-card__identity">
          <span class="dataset-card__icon" aria-hidden="true">🎓</span>
          <div class="dataset-card__heading">
            <h3><a href="https://huggingface.co/datasets/AITextDetect/AI_Polish_clean">MGT-Academic</a></h3>
            <div class="dataset-tags"><span>Academic Writing</span><span>AI Text</span><span>Detection</span></div>
          </div>
        </div>
        <div class="dataset-actions">
          <span class="dataset-download" title="Total downloads on Hugging Face"><span aria-hidden="true">↓</span> <strong data-hf-downloads="AITextDetect/AI_Polish_clean">10,900</strong></span>
          <a href="https://arxiv.org/abs/2412.17242">Paper ↗</a>
          <a class="dataset-hf-link" href="https://huggingface.co/datasets/AITextDetect/AI_Polish_clean"><span aria-hidden="true">🤗</span> Dataset ↗</a>
        </div>
      </div>
      <p class="dataset-description"><span>Description</span>Human- and machine-generated academic text spanning STEM, social sciences, and humanities.</p>
      <div class="dataset-meta">
        <div><span>Source</span>arXiv, Wikipedia, Project Gutenberg</div>
        <div><span>Size</span>749K samples · 336M+ tokens</div>
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
