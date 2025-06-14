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

I'm **Youngwan**, a _senior researcher_ at [ETRI](https://www.etri.re.kr/eng/main/main.etri) and _Ph.D student_ in Graduate school of [AI](https://gsai.kaist.ac.kr/) at [KAIST](https://www.kaist.ac.kr/en/), where I'm advised by Prof. [Sung Ju Hwang](http://www.sungjuhwang.com/) in the [Machine Learning and Artificial Intelligence (MLAI)](https://www.mlai-kaist.com/) lab. I received my B.S and M.S. degrees at Inha University in 2015 and 2017, respectively, advised by [Hakil Kim](https://vision.inha.ac.kr/).
My research interest is how computers understand the world, including efficient 2D/3D neural network design, object detection, instance segmentation, semantic segmentation, and video classification 🖥️🌏. Besides, I have explored Vision Transformer architecture and self-supervised learning.
Recently, I have focused on multimodal learning, including text-image generation and safety for vision-language models.

I aspire to practice [Slow Science](http://slow-science.org/).



# 🎉 News
- *2025.02*: &nbsp;🎉🎉 VideICL has been accepted at CVPR 2025. 
- *2025.01*: &nbsp;🎉🎉 Two papers have been accepted at ICLR 2025. 
- *2024.09*: &nbsp;🎉🎉 KOALA has been accepted at NeurIPS 2024. 
- *2024.08*: &nbsp;🎉🎉 DiT-Pruner has been accepted at ECCVW 2024. 
- *2024.05*: &nbsp;🎉🎉 EVEREST has been accepted at ICML 2024. 
- *2023.12*: &nbsp;🎉🎉 KOALA, a fast Text-to-Image sythesis model, has been released. 
- *2023.02*: &nbsp;🎉🎉 Two papers have been accepted at ICLR 2023. 
- *2022.02*: &nbsp;🎉🎉 One paper has been accepted at CVPR 2022. 

# 📚 Publications 
[Google Scholar full list](https://scholar.google.com/citations?user=EqemKYsAAAAJ&hl) <a href='https://scholar.google.com/citations?user=EqemKYsAAAAJ&hl'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>)

* ## HoliSafe: Holistic Safety Benchmarking and Modeling with Safety Meta Token for Vision-Language Model <br>
    **Youngwan Lee**, Kangsan Kim, Kwanyong Park, Ilchae Jung, Sujin Jang, Seanie Lee, Yong-Ju Lee, Sung Ju Hwang <br>
    <span style="color:darkred">**Arxiv**</span> 2025 <br>
   [[Project page]](https://youngwanlee.github.io/holisafe/) / [[paper]](https://www.arxiv.org/pdf/2506.04704) / [[code]](https://github.com/youngwanLEE/holisafe)


 * ## VideoICL: Confidence-based Iterative In-context Learning for Out-of-Distribution Video Understanding <br>
    Kangsan Kim, Geon Park, **Youngwan Lee**, Woongyeong Yeo, Sung Ju Hwang <br>
    Computer Vision and Pattern Recognition (<span style="color:darkred">**CVPR**</span>) 2025  <br>
    [[paper]](https://arxiv.org/abs/2412.02186) / [[poster]](https://www.dropbox.com/scl/fi/y8k2ibj7gptq1cnrmyc67/videoicl_cvpr25_poster.pdf?rlkey=gh8h20f9xgjhh24wqqijiwc8l&st=2eajus6r&dl=0) / [[code]](https://github.com/KangsanKim07/VideoICL) <br>

* ## A Training-Free Sub-quadratic Cost Transformer Model Serving Framework with Hierarchically Pruned Attention <br>
   Heejun Lee\*, Geon Park\*, __Youngwan Lee\*__, Jaduk Suh\*, Jina Kim, Wonyong Jeong, Bumsik Kim, Hyemin Lee, Myeongjae Jeon, Sung Ju Hwang <br>
   *:equal contribtion <br>
   Internation Conference on Learning Representation (<span style="color:darkred">**ICLR**</span>) 2025  <br>
   [[paper]](https://openreview.net/forum?id=PTcMzQgKmn) / [[code]](https://github.com/DeepAuto-AI/hip-attention)

* ## Training Free Exponential Context Extension via Cascading KV Cache <br>
   Jeffrey Willette, Heejun Lee, **Youngwan Lee**, Myeongjae Jeon, Sung Ju Hwang <br>
   Internation Conference on Learning Representation (<span style="color:darkred">**ICLR**</span>) 2025  <br>
   [[paper]](https://openreview.net/forum?id=dSneEp59yX&noteId=cXYZDTrz2p)

* ## KOALA: Empirical Lessons Toward Memory-Efficient and Fast Diffusion Models for Text-to-Image Synthesis <br>
    **Youngwan Lee**, Kwanyong Park, Yoorhim Cho, Yong-Ju Lee, Sung Ju Hwang <br>
   Advances in Neural Information Processing Systems (<span style="color:darkred">**NeurIPS**</span>) 2024 <br>
   CVPR 2024  Workshop on [Generative Models for Computer Vision](https://generative-vision.github.io/workshop-CVPR-24/) <br>
    [[Project page]](https://youngwanlee.github.io/KOALA/) / [[paper]](https://arxiv.org/abs/2312.04005) / [[OpenReview]](https://openreview.net/forum?id=KNDUBpWV9b&referrer=%5Bthe%20profile%20of%20Youngwan%20Lee%5D(%2Fprofile%3Fid%3D~Youngwan_Lee1)) / [[poster]](https://www.dropbox.com/scl/fi/pg5364swonj14h3yzdlce/poster_koala_final_2.pdf?rlkey=q15vao7myr1l8sgv2292ip5m2&st=hcqwggpb&dl=0) / [[code]](https://github.com/youngwanLEE/sdxl-koala) <br>

* ## DiT-Pruner: Pruning Diffusion Transformer Models for Text-to-Image Synthesis Using Human Preference Scores <br>
    **Youngwan Lee**, Yong-Ju Lee, Sung Ju Hwang <br>
    European Conference on Computer Vision (<span style="color:darkred">**ECCV**</span>) 2024  Workshop on [Green Foundation Models](https://green-fomo.github.io/ECCV2024/)   <br>
    [[paper]](https://green-fomo.github.io/ECCV2024/static/papers/14.pdf)<br>

* ## PC-LoRA: Low-Rank Adaptation for Progressive Model Compression with Knowledge Distillation <br>
    Injoon Hwang\*, Haewon Park\*, **Youngwan Lee\***, Jooyoung Yang, SunJae Maeng <br>
   *:equal contribtion <br>
   Computer Vision and Pattern Recognition (<span style="color:darkred">**CVPR**</span>) 2024  Workshop on [Transformers for Vision (T4V)](https://sites.google.com/view/t4v-cvpr24), <span style="color:purple">**Spotlight**</span> <br>
    [[paper]](https://arxiv.org/abs/2406.09117)<br>

* ## EVEREST: Efficient Masked Video Autoencoder by Removing Redundant Spatiotemporal Tokens <br>
    Sunil Hwang\*, Jaehong Yoon\* **Youngwan Lee\***, Sung Ju Hwang <br>
    *:equal contribtion <br>
   Internation Conference on Machine Learning (<span style="color:darkred">**ICML**</span>) 2024 <br>
   CVPR 2024  Workshop on [Transformers for Vision (T4V)](https://sites.google.com/view/t4v-cvpr24), <span style="color:purple">**Spotlight**</span> <br>
   [[paper]](https://arxiv.org/abs/2211.10636)

* ## Dynamic and Super-Personalized Media Ecosystem Driven by Generative AI: Unpredictable Plays Never Repeating the Same <br>
    Sungjun Ahn, Hyun-Jeong Yim, **Youngwan Lee**, Sung-Ik Park <br>
   IEEE Transactions on Broadcasting 2024 <br>
   [[paper]](https://ieeexplore.ieee.org/abstract/document/10506327)


* ## Visualizing the loss landscape of Self-supervised Vision Transformer  <br>
    **Youngwan Lee**, Jeffrey Ryan Willette, Jonghee Kim, Sung Ju Hwang <br>
   Conference on Neural Information Processing Systems (<span style="color:darkred">**NeurIPS**</span>) 2023  Workshop on [Self-Supervised Learning - Theory and Practice](https://sslneurips23.github.io/index.html)   <br>
    [[paper]](https://arxiv.org/abs/2405.18042)<br>

* ## Exploring the Role of Mean Teachers in Self-supervised Masked Auto-Encoders <br>
    **Youngwan Lee**\*, Jeffrey Ryan Willette\*, Jonghee Kim, Juho Lee, Sung Ju Hwang <br>
    *:equal contribtion <br>
    Internation Conference on Learning Representation (<span style="color:darkred">**ICLR**</span>) 2023  <br>
    [[paper]](https://openreview.net/forum?id=7sn6Vxp92xV) / [[poster]](https://www.dropbox.com/s/mqwdgckil89qh8e/rcmae_poster_final.pdf) / [[slide]](https://docs.google.com/presentation/d/1OoN67hRpyQybe2QcwBX0h1Urq4g40zVrD9lX3AlQgPs/edit?usp=sharing) / [![](https://img.shields.io/github/stars/youngwanLEE/rc-mae?style=social&label=Code+Stars)](https://github.com/youngwanLEE/rc-mae) <br>

 * ## Sparse Token Transformer with Attention Back Tracking <br>
    Heejun Lee, Minki Kang, **Youngwan Lee**, Sung Ju Hwang <br>
    Internation Conference on Learning Representation (<span style="color:darkred">**ICLR**</span>) 2023  <br>
    [[paper]](https://openreview.net/forum?id=VV0hSE8AxCw&referrer=%5BAuthor%20Console%5D(%2Fgroup%3Fid%3DICLR.cc%2F2023%2FConference%2FAuthors%23your-submissions)) / [[poster]](https://www.dropbox.com/s/v15asq628iyt0x9/sparse_token_poster.pdf) / [[slide]](https://docs.google.com/presentation/d/1BPplZugqLyhp2Posig0K62CeTn6DaiALx4D2g0PIt8U/edit#slide=id.p) <br>
 
 
 * ## MPViT: Multi-Path Vision Transformer for Dense Prediction <br>
    **Youngwan Lee**, Jonghee Kim, Jeffrey Ryan Willette, Sung Ju Hwang <br>
    Computer Vision and Pattern Recognition (<span style="color:darkred">**CVPR**</span>) 2022  <br>
    [[paper]](https://arxiv.org/abs/2112.11010) / [[poster]](https://www.dropbox.com/s/56tdh4fmxkm04u9/%5Bfinal%5D%5Bmpvit_poster%5D.pdf) / [[slide]](https://www.dropbox.com/s/1jclnrdlex07yn6/mpvit_presentation.pdf) / [![](https://img.shields.io/github/stars/youngwanLEE/MPViT?style=social&label=Code+Stars)](https://github.com/youngwanLEE/MPViT) <br>

 * ## Localization Uncertainty Estimation for Anchor-Free Object Detection <br>
    **Youngwan Lee**, Joong-Won Hwang, Hyung-Il Kim, Kimin Yun, YongJin Kwon, Yuseok Bae, Sung Ju Hwang <br>
    European Conference on Computer Vision Workshop on [Uncertainty Quantification for Computer Vision](https://uncv2022.github.io/) (<span style="color:darkred">**ECCVW**</span>) 2022  <br>
    [[paper]](https://arxiv.org/abs/2006.15607) / [[poster]](https://www.dropbox.com/s/rxwgveiy7l0isnh/poster.pdf) / [[slide]](https://www.dropbox.com/s/ijp3nofi57jbhbr/uad_presentation.pdf) / [![](https://img.shields.io/github/stars/youngwanLEE/UAD?style=social&label=Code+Stars)](https://github.com/youngwanLEE/UAD) <br>
    
 * ## Diverse Temporal Aggregation and Depthwise Spatiotemporal Factorization for Efficient Video Classification <br>
    **Youngwan Lee**, Hyung-Il Kim, Kimin Yun, Jinyoung Moon <br>
    IEEE Access 2021  <br>
    [[paper]](https://arxiv.org/abs/2012.00317) / [![](https://img.shields.io/github/stars/youngwanLEE/VoV3D?style=social&label=Code+Stars)](https://github.com/youngwanLEE/VoV3D) <br>

 * ## Adversarial training with stochastic weight average <br>
    Joong-Won Hwang, **Youngwan Lee**, Seongchan Oh, Yuseok Bae<br>
    International Conference on Image Processing (<span style="color:darkred">**ICIP**</span>) 2021<br>
    [[paper]](https://ieeexplore.ieee.org/abstract/document/9506548) <br>

 * ## Anti-Litter Surveillance based on Person Understanding via Multi-Task Learning <br>
    Kangmin Bae, Kimin Yun, Hyung-Il Kim, **Youngwan Lee**, Jongyoul Park <br>
    The British Machine Vision Conference (<span style="color:darkred">**BMVC**</span>) 2020<br>
    [[paper]](https://www.bmvc2020-conference.com/assets/papers/0279.pdf) <br>

 * ## CenterMask: Real-Time Anchor-Free Instance Segmentation <br>
    **Youngwan Lee**, Jongyoul Park <br>
    Computer Vision and Pattern Recognition (<span style="color:darkred">**CVPR**</span>) 2020 <br>
    [[paper]](https://arxiv.org/abs/1911.06667) / [![](https://img.shields.io/github/stars/youngwanLEE/CenterMask?style=social&label=Code1+Stars)](https://github.com/youngwanLEE/CenterMask)[![](https://img.shields.io/github/stars/youngwanLEE/centermask2?style=social&label=detectron2+Stars)](https://github.com/youngwanLEE/centermask2) <br>

 * ## An Energy and GPU-Computation Efficient Backbone Network for Real-Time Object Detection <br>
    **Youngwan Lee**\*, Joong-Won Hwang\*, Sangrok Lee, Yuseok Bae, Jongyoul Park <br>
    *:equal contribtion <br>
    Computer Vision and Pattern Recognition Workshop on Compact and Efficient Feature Representation and Learning in Computer Vision (<span style="color:darkred">**CVPRW**</span>) 2019  <br>
    [[paper]](https://arxiv.org/abs/1904.09730) / [[timm]](https://huggingface.co/docs/timm/models/ese-vovnet) / [![](https://img.shields.io/github/stars/youngwanLEE/vovnet-detectron2?style=social&label=Code+Stars)](https://github.com/youngwanLEE/vovnet-detectron2) <br>


# 🎖 Honors and Awards
- *2025.04* Best Researcher Award, ETRI
- *2025.04* Best Lecturer Award, ETRI
- *2024.04* Best Paper Award, ETRI 
<!-- - *2022.12* Ministerial Citation (장관표창)<sub>[[certificate](https://www.dropbox.com/scl/fi/2xtwnb1d3x4xz9arbak0p/_.png?rlkey=xlhcjsqsbnl06r7mtj0b19r36&dl=0)]</sub>, Minister of Science and ICT, South Korea -->
- *2022.12* Ministerial Citation ([장관표창](https://www.dropbox.com/scl/fi/2xtwnb1d3x4xz9arbak0p/_.png?rlkey=xlhcjsqsbnl06r7mtj0b19r36&dl=0)), Minister of Science and ICT, South Korea
- *2022.04* Best Lecturer Award, ETRI 
- *2022.04* Best Paper Award, ETRI 
- *2017.06* 2nd rank in ImageNet Challenge (Detection task, Team [DeepView](https://image-net.org/challenges/LSVRC/2017/results)) 

<!-- # 📖 Educations
- *2019.06 - 2022.04 (now)*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2015.09 - 2019.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  -->

<!-- # 💬 Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/) -->

# 💻 Academic Services
- Lecturer
   - 2020-present, AI Academy at ETRI
   - 2022-2023, Hallym University Medical Center
   - 2022, Korea Atomic Energy Research Institute

- Reviewer
   - Journal
      - IEEE Transactions on Pattern Analysis and Machine Intelligence (T-PAMI)
      - IEEE Transactions on Image Processing (T-IP)
      - IEEE Transactions on Intelligent Transportation Systems (T-ITS)
      - IEEE Transactions on Vehicular Technology (T-VT)
      - IEEE Transactions on Circuits and Systems for Video Technology (T-CSVT)
      - International Journal on Computer Vision (IJCV)

   - Conference
      - IEEE/CVF Computer Vision and Pattern Recognition Conference (CVPR) 2023 2024 2025
      - Neural Information Processing Systems (NeurIPS) 2023 2024 2025
      - International Conference on Learning Representations (ICLR) 2024 2025
      - International Conference on Machine Learning (ICML) 2023 2024 2025
      - International Conference on Computer Vision (ICCV) 2023 2025
      - European Conference on Computer Vision (ECCV) 2024
      - Association for the Advancement of Artificial Intelligence (AAAI) 2025
      <!-- - ICIP 2023 -->
      <!-- - WACV 2021 2024 -->
