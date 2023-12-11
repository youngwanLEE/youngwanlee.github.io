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

I'm **Youngwan**, a _senior researcher_ at [ETRI](https://www.etri.re.kr/eng/main/main.etri) and _Ph.D student_ in Graduate school of [AI](https://gsai.kaist.ac.kr/) at [KAIST](https://www.kaist.ac.kr/en/), where I'm advised by Prof. [Sung Ju Hwang](http://www.sungjuhwang.com/) in the [Machine Learning and Artificial Intelligence (MLAI)](https://www.mlai-kaist.com/) lab.
My research interest is how computers understand the world, including efficient 2D/3D neural network design, object detection, instance segmentation, semantic segmentation, and video classification 🖥️🌏. Recently, I have focused on Vision Transformer architecture and self-supervised learning. 



# 🎉 News
- *2023.12*: &nbsp;🎉🎉 KOALA, a fast Text-to-Image sythesis model, has been released. 
- *2023.02*: &nbsp;🎉🎉 Two papers have been accepted at ICLR 2023. 
- *2022.02*: &nbsp;🎉🎉 One paper has been accepted at CVPR 2022. 

# 📚 Publications 
[Google Scholar full list](https://scholar.google.com/citations?user=EqemKYsAAAAJ&hl)


* ## KOALA:Self-Attention Matters in Knowledge Distillation of Latent Diffusion Models for Memory-Efficient and Fast Image Synthesis  <br>
    **Youngwan Lee**, Kwangyong Park, Yoorhim Cho, Yong-Ju Lee, Sung Ju Hwang <br>
   <span style="color:darkred">**Arxiv**</span> 2023 <br>
    [Project page](https://youngwanlee.github.io/KOALA/)[[paper]](https://arxiv.org/abs/2312.04005)[code](https://github.com/youngwanLEE/sdxl-koala)<br>


* ## Visualizing the loss landscape of Self-supervised Vision Transformer  <br>
    **Youngwan Lee**, Jeffrey Ryan Willette, Jonghee Kim, Sung Ju Hwang <br>
   Conference on Neural Information Processing Systems (<span style="color:darkred">**NeurIPS**</span>) 2023  Workshop on [Self-Supervised Learning - Theory and Practice](https://sslneurips23.github.io/index.html)   <br>
    [[paper]](https://sslneurips23.github.io/paper_pdfs/paper_23.pdf)<br>

* ## Exploring the Role of Mean Teachers in Self-supervised Masked Auto-Encoders <br>
    **Youngwan Lee**\*, Jeffrey Ryan Willette\*, Jonghee Kim, Juho Lee, Sung Ju Hwang <br>
    *:equal contribtion <br>
    Internation Conference on Learning Representation (<span style="color:darkred">**ICLR**</span>) 2023  <br>
    [[paper]](https://openreview.net/forum?id=7sn6Vxp92xV)[[poster]](https://www.dropbox.com/s/mqwdgckil89qh8e/rcmae_poster_final.pdf)[[slide]](https://docs.google.com/presentation/d/1OoN67hRpyQybe2QcwBX0h1Urq4g40zVrD9lX3AlQgPs/edit?usp=sharing)|[![](https://img.shields.io/github/stars/youngwanLEE/rc-mae?style=social&label=Code+Stars)](https://github.com/youngwanLEE/rc-mae) <br>

 * ## Sparse Token Transformer with Attention Back Tracking <br>
    Heejun Lee, Minki Kang, **Youngwan Lee**, Sung Ju Hwang <br>
    Internation Conference on Learning Representation (<span style="color:darkred">**ICLR**</span>) 2023  <br>
    [[paper]](https://openreview.net/forum?id=VV0hSE8AxCw&referrer=%5BAuthor%20Console%5D(%2Fgroup%3Fid%3DICLR.cc%2F2023%2FConference%2FAuthors%23your-submissions))[[poster]](https://www.dropbox.com/s/v15asq628iyt0x9/sparse_token_poster.pdf)[[slide]](https://docs.google.com/presentation/d/1BPplZugqLyhp2Posig0K62CeTn6DaiALx4D2g0PIt8U/edit#slide=id.p) <br>
 
 
 * ## MPViT: Multi-Path Vision Transformer for Dense Prediction <br>
    **Youngwan Lee**, Jonghee Kim, Jeffrey Ryan Willette, Sung Ju Hwang <br>
    Computer Vision and Pattern Recognition (<span style="color:darkred">**CVPR**</span>) 2022  <br>
    [[paper]](https://arxiv.org/abs/2112.11010)[[poster]](https://www.dropbox.com/s/56tdh4fmxkm04u9/%5Bfinal%5D%5Bmpvit_poster%5D.pdf) [[slide]](https://www.dropbox.com/s/1jclnrdlex07yn6/mpvit_presentation.pdf)| [![](https://img.shields.io/github/stars/youngwanLEE/MPViT?style=social&label=Code+Stars)](https://github.com/youngwanLEE/MPViT) <br>

 * ## Localization Uncertainty Estimation for Anchor-Free Object Detection <br>
    **Youngwan Lee**, Joong-Won Hwang, Hyung-Il Kim, Kimin Yun, YongJin Kwon, Yuseok Bae, Sung Ju Hwang <br>
    European Conference on Computer Vision Workshop on [Uncertainty Quantification for Computer Vision](https://uncv2022.github.io/) (<span style="color:darkred">**ECCVW**</span>) 2022  <br>
    [[paper]](https://arxiv.org/abs/2006.15607)[[poster]](https://www.dropbox.com/s/rxwgveiy7l0isnh/poster.pdf)[[slide]](https://www.dropbox.com/s/ijp3nofi57jbhbr/uad_presentation.pdf)[![](https://img.shields.io/github/stars/youngwanLEE/UAD?style=social&label=Code+Stars)](https://github.com/youngwanLEE/UAD) <br>
    
 * ## Diverse Temporal Aggregation and Depthwise Spatiotemporal Factorization for Efficient Video Classification <br>
    **Youngwan Lee**, Hyung-Il Kim, Kimin Yun, Jinyoung Moon <br>
    IEEE Access 2021  <br>
    [[paper]](https://arxiv.org/abs/2012.00317) | [![](https://img.shields.io/github/stars/youngwanLEE/VoV3D?style=social&label=Code+Stars)](https://github.com/youngwanLEE/VoV3D) <br>

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
    [[paper]](https://arxiv.org/abs/1911.06667) | [![](https://img.shields.io/github/stars/youngwanLEE/CenterMask?style=social&label=Code1+Stars)](https://github.com/youngwanLEE/CenterMask)[![](https://img.shields.io/github/stars/youngwanLEE/centermask2?style=social&label=detectron2+Stars)](https://github.com/youngwanLEE/centermask2) <br>

 * ## An Energy and GPU-Computation Efficient Backbone Network for Real-Time Object Detection <br>
    **Youngwan Lee**\*, Joong-Won Hwang\*, Sangrok Lee, Yuseok Bae, Jongyoul Park <br>
    *:equal contribtion <br>
    Computer Vision and Pattern Recognition Workshop on Compact and Efficient Feature Representation and Learning in Computer Vision (<span style="color:darkred">**CVPRW**</span>) 2019  <br>
    [[paper]](https://arxiv.org/abs/1904.09730)[[timm]](https://huggingface.co/docs/timm/models/ese-vovnet)| [![](https://img.shields.io/github/stars/youngwanLEE/vovnet-detectron2?style=social&label=Code+Stars)](https://github.com/youngwanLEE/vovnet-detectron2) <br>


# 🎖 Honors and Awards
- *2022.12* Ministerial Citation (장관표창), Minister of Science and ICT, South Korea  
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
      - CVPR 2023 2024
      - ICCV 2023
      - ICLR 2024
      - ICML 2023
      - NeurIPS 2023
      - ICIP 2023
      - WACV 2021 2024
