# 모아 — AI 북마크 지식 보관소

YouTube 링크를 저장하면 제목, 채널, 자막 또는 영상 메타데이터를 읽어 요약과 태그로 정리하는 인터랙티브 북마크 앱입니다.

## 주요 기능

- YouTube URL 분석 및 실제 제목·채널 정보 수집
- 자막 기반 요약과 자동 태그 분류
- 검색, 유형·컬렉션·즐겨찾기 필터
- 카드/목록 보기, 상세 패널, 랜덤 추천
- 반응형 라이트 모드 UI

## 로컬 실행

```bash
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
uvicorn server:app --reload --port 8937
```

브라우저에서 `http://127.0.0.1:8937`을 엽니다.

## 테스트

```bash
pip install pytest httpx
pytest -q
```

## 배포 참고

Vercel에서는 자막이 있는 영상은 자막 내용을 사용하고, 자막이 없는 영상은 제목과 채널 메타데이터를 기준으로 정리합니다. 로컬 Hermes Agent와 `ffmpeg`가 있는 환경에서는 자막 없는 영상의 프레임 비전 분석도 사용할 수 있습니다.

Google Fonts와 YouTube 공개 메타데이터/자막 엔드포인트를 런타임 외부 의존성으로 사용합니다.
