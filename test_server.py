import pytest
from fastapi.testclient import TestClient

from server import extract_video_id, analyze_youtube, analyze_video_frames, app


def test_extracts_video_id_from_short_url_with_share_query():
    assert extract_video_id("https://youtu.be/P1Ujx5EzLEo?si=3fLf2XHpwSP0oJud") == "P1Ujx5EzLEo"


def test_real_youtube_analysis_uses_source_metadata():
    result = analyze_youtube("https://youtu.be/P1Ujx5EzLEo?si=3fLf2XHpwSP0oJud", use_llm=False)
    assert result["title"] == "[호연지재] BIB socket pusher"
    assert result["author"] == "호연지재 (HOVISION)"
    assert result["video_id"] == "P1Ujx5EzLEo"
    assert result["title"] != "실전에서 바로 쓰는 AI 에이전트 설계법"
    assert result["tags"]


def test_analyzes_captionless_video_from_frames():
    result = analyze_video_frames("https://www.youtube.com/watch?v=P1Ujx5EzLEo", {"title": "[호연지재] BIB socket pusher", "author_name": "호연지재 (HOVISION)"})
    assert result["source"] == "vision"
    assert result["summary"].strip()
    assert result["tags"]


def test_banner_assets_are_served():
    client = TestClient(app)
    for asset in ("idea-banner-copy.jpg", "idea-banner-apps.jpg"):
        response = client.get(f"/assets/{asset}")
        assert response.status_code == 200
        assert response.headers["content-type"] == "image/jpeg"
        assert response.content


def test_favicon_does_not_create_browser_console_error():
    response = TestClient(app).get("/favicon.ico")
    assert response.status_code == 204


def test_rejects_non_youtube_url():
    with pytest.raises(ValueError, match="YouTube"):
        extract_video_id("https://example.com/article")
