# 레시피 AI (냉부)

"레시피 AI (냉부)"는 사용자가 입력한 재료를 바탕으로 창의적인 요리 레시피를 생성하고 시각적 이미지를 함께 제공하는 AI 기반 웹 애플리케이션입니다. 사용자 친화적인 인터페이스와 최신 AI 기술을 활용하여 개인 맞춤형 요리 레시피를 제공합니다.  

## 주요 기능
- 사용자가 입력한 재료를 기반으로 한 레시피 생성
- 생성된 레시피에 대한 단계별 요리 설명 제공
- AI가 생성한 레시피 이미지를 시각적으로 제공
- 웹 애플리케이션을 통해 사용자의 입력을 받고 결과를 시각화

## 설치 및 실행 가이드

### 사전 요구 사항
- Python 3.7 이상
- Flask
- OpenAI API 키

### 설치 방법

1. 이 리포지토리를 클론합니다:
   ```bash
   git clone https://github.com/Nacho-Cola/recipes_10000.git
   cd recipes_10000
   ```

2. 가상 환경을 설정합니다 (선택 사항):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\activate   # Windows
   ```

3. 필요한 패키지를 설치합니다:
   ```bash
   pip install -r requirements.txt
   ```

4. OpenAI API 키 설정:
   - 환경 변수로 설정하거나, 스크립트 내에서 `openai.api_key = 'your_api_key_here'`로 설정합니다.

### 실행 방법

1. Flask 애플리케이션을 실행합니다:
   ```bash
   python3 app.py
   ```
2. 웹 브라우저에서 다음 URL을 엽니다:
   ```
   http://127.0.0.1:8888/
   ```

## 사용 방법
1. 재료를 입력란에 입력하고 "레시피 생성" 버튼을 클릭합니다.
2. AI가 제공하는 레시피 제목, 설명, 재료 목록 및 단계별 요리 방법을 확인합니다.
3. 생성된 요리 이미지도 함께 제공됩니다.
4. 필요시 제공된 팁을 통해 요리 과정 중 추가적인 정보를 확인할 수 있습니다.

## 주요 파일 구조
```
naengbu-recipe-ai/
│
├── app.py                   # Flask 애플리케이션
├── templates/
│   └── index.html           # 메인 HTML 파일
├── static/
│   ├── styles.css           # 스타일시트
│   └── script.js            # 클라이언트 측 스크립트
├── requirements.txt         # 필요한 패키지 목록
└── README.md                # 프로젝트 설명 파일
```

## 주요 기술
- **Flask**: 백엔드 웹 서버 프레임워크로 사용
- **OpenAI API**: 자연어 처리를 통한 레시피 생성 및 DALL-E 기반 이미지 생성
- **HTML/CSS/JavaScript**: 사용자 인터페이스 구성

## API 엔드포인트

### `/generate` (POST)
- **설명**: 입력된 재료를 기반으로 레시피를 생성합니다.
- **요청**:
  - `chat`: 사용자가 입력한 재료 문자열
- **응답**:
  - `title`: 생성된 레시피 제목
  - `summary`: 레시피 설명
  - `ingredients`: 재료 목록 (이름과 양)
  - `steps`: 요리 단계별 설명
  - `tips`: 추가 팁

### `/generate_img` (POST)
- **설명**: 레시피 제목과 설명을 바탕으로 이미지 생성
- **요청**:
  - `img`: 이미지 생성을 위한 입력 문자열
- **응답**:
  - `image`: 생성된 이미지의 URL

## 예제 사용
1. `감자, 소고기` 입력 시:
   - **생성된 레시피**: 감자 소고기 스튜
   - **재료 목록**: 감자 3개, 소고기 500g 등
   - **요리 단계**: 재료 손질 → 볶기 → 스튜 끓이기
   - **이미지**: 스튜 요리 이미지
