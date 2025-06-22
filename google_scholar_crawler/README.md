# Google Scholar Citation Crawler

이 디렉토리는 Google Scholar에서 자동으로 citation 수를 가져와서 홈페이지에 업데이트하는 시스템입니다.

## 📁 파일 구조

```
google_scholar_crawler/
├── main.py                 # 자동 크롤링 스크립트
├── manual_update.py        # 수동 업데이트 스크립트
├── requirements.txt        # Python 의존성
├── README.md              # 이 파일
└── results/               # 크롤링 결과 저장 폴더
    ├── gs_data.json       # 전체 데이터
    └── gs_data_shieldsio.json  # 뱃지용 데이터
```

## 🚀 자동화 시스템

### GitHub Actions
- **자동 스케줄**: 매주 월요일 2AM, 목요일 2PM (UTC)
- **수동 트리거**: GitHub Actions 탭에서 언제든 실행 가능
- **백업 워크플로우**: 자동화 실패 시 수동 입력으로 업데이트

### 문제 상황
GitHub Actions IP가 Google Scholar에 의해 봇으로 인식되어 차단될 수 있습니다. 이런 경우 로컬에서 수동 업데이트를 사용하세요.

## 💻 로컬 백업 방법

### 방법 1: 자동 크롤링 (추천)

```bash
# 1. 크롤러 디렉토리로 이동
cd google_scholar_crawler

# 2. 의존성 설치 (처음 한 번만)
pip install -r requirements.txt

# 3. 자동 크롤링 실행
python main.py

# 4. 결과를 홈페이지에 복사
cp results/gs_data_shieldsio.json ../google-scholar-stats/

# 5. 변경사항 확인
git status
git diff

# 6. 커밋 & 푸시
git add ../google-scholar-stats/gs_data_shieldsio.json
git commit -m "Update Google Scholar citations manually [$(date +'%Y-%m-%d %H:%M:%S')]"
git push
```

### 방법 2: 수동 입력

```bash
# 1. 크롤러 디렉토리로 이동
cd google_scholar_crawler

# 2. 수동 업데이트 스크립트 실행
python manual_update.py

# 입력 프롬프트가 나타나면 Google Scholar에서 확인한 citation 수 입력
# 예: 2090

# 3. 결과를 홈페이지에 복사
cp results/gs_data_shieldsio.json ../google-scholar-stats/

# 4. 커밋 & 푸시
git add ../google-scholar-stats/gs_data_shieldsio.json
git commit -m "Manual update: Google Scholar citations [$(date +'%Y-%m-%d %H:%M:%S')]"
git push
```

### 방법 3: 직접 citation 수 지정

```bash
# citation 수를 직접 지정하여 실행
python manual_update.py 2090

# 또는 한 줄로
python manual_update.py 2090 && cp results/gs_data_shieldsio.json ../google-scholar-stats/
```

### 방법 4: 완전 수동 (스크립트 없이)

```bash
# 1. JSON 파일 직접 수정
echo '{"schemaVersion": 1, "label": "citations", "message": "2090"}' > google-scholar-stats/gs_data_shieldsio.json

# 2. 커밋 & 푸시
git add google-scholar-stats/gs_data_shieldsio.json
git commit -m "Manual citation update to 2090"
git push
```

## 🔍 Google Scholar Citation 수 확인 방법

1. [Google Scholar 프로필](https://scholar.google.com/citations?user=EqemKYsAAAAJ&hl) 방문
2. 프로필 상단의 **"Cited by"** 숫자 확인
3. 그 숫자를 위 방법들 중 하나로 업데이트

## ⚡ 빠른 원라이너

```bash
# 디렉토리 이동 + 크롤링 + 복사 + 커밋 + 푸시 (모든 과정 한 번에)
cd google_scholar_crawler && python main.py && cp results/gs_data_shieldsio.json ../google-scholar-stats/ && cd .. && git add google-scholar-stats/gs_data_shieldsio.json && git commit -m "Update citations [$(date +'%Y-%m-%d %H:%M:%S')]" && git push
```

## 📝 추천 워크플로우

1. **먼저 자동 크롤링 시도** (방법 1)
2. **실패하면 수동 입력** (방법 2) 
3. **급할 때는 직접 수정** (방법 4)

## 🛠️ GitHub Actions에서 수동 업데이트

자동 크롤링이 실패하는 경우:

1. GitHub 저장소 → **Actions** 탭
2. **"Manual Citation Update"** 워크플로우 선택
3. **"Run workflow"** 버튼 클릭
4. Google Scholar에서 확인한 citation 수 입력
5. **"Run workflow"** 실행

## 🔧 문제 해결

### 크롤링이 실패하는 경우
- Google Scholar가 IP를 차단했을 가능성
- 수동 방법(방법 2-4) 사용 권장

### 의존성 설치 오류
```bash
# 가상환경 사용 권장
python -m venv venv
source venv/bin/activate  # macOS/Linux
# 또는
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

### 권한 오류
```bash
# Git 사용자 정보 확인
git config user.name
git config user.email

# 필요시 설정
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

## 📊 현재 상태

- **최근 업데이트**: 2085 citations
- **Scholar ID**: EqemKYsAAAAJ
- **자동화 상태**: 주 2회 스케줄 (봇 차단 회피)
- **백업 방법**: 수동 업데이트 스크립트 준비됨

---

이제 GitHub Actions가 실패해도 언제든 로컬에서 쉽게 업데이트할 수 있습니다! 🎉