# AI Code Review Tutorial

GitHub Pull Request가 생성/수정되면 GitHub Actions가 변경된 Python 파일의 diff를 OpenAI API로 검토하고 PR 대화에 댓글을 남깁니다.

## 준비
1. 이 폴더를 새 GitHub 저장소의 **기본 브랜치(main)** 에 push합니다.
2. GitHub 저장소 → Settings → Secrets and variables → Actions → New repository secret → 이름 `OPENAI_API_KEY`, 값은 본인의 API 키를 입력합니다. (API 사용 비용이 발생할 수 있습니다.)
3. Settings → Actions → General → Workflow permissions에서 기본 `GITHUB_TOKEN`이 댓글 작성에 필요한 권한을 사용할 수 있는지 확인합니다. 워크플로에 `issues: write`를 명시했습니다.
4. Actions 탭에서 워크플로가 허용되어 있는지 확인합니다.

## 시연
1. `git checkout -b demo/buggy-average`
2. `src/calculator.py`에서 `if not numbers:`와 그 아래 `raise ValueError(...)` 줄을 삭제합니다.
3. `git add . && git commit -m "Demo: remove empty-input guard" && git push -u origin demo/buggy-average`
4. GitHub에서 `demo/buggy-average` → `main` PR을 만듭니다.
5. Actions 탭의 **AI Code Review** 실행 결과를 보고, PR **Conversation** 탭에서 봇 댓글을 확인합니다.
6. 오류를 고쳐 다시 push하면 댓글이 갱신됩니다.

## 로컬 테스트
`python -m pip install -r requirements.txt`
`python -m pytest -q`

## 주의
- `pull_request_target`은 높은 권한으로 실행될 수 있으므로 PR의 head 브랜치를 checkout하거나 PR 코드를 실행하면 안 됩니다. 이 예제는 신뢰된 기본 브랜치의 스크립트만 실행하고 PR의 diff 텍스트만 가져옵니다.
- PR diff에는 공격적인 지시문이 포함될 수 있습니다. 프롬프트에서 이를 데이터로 취급하도록 지시했지만 프롬프트 인젝션을 완전히 막는 것은 아닙니다.
- 외부 LLM으로 코드 diff가 전송되므로 민감한 저장소에서는 정책을 검토하세요.
- `.py` 파일 변경만 검토하며 최대 18,000자만 입력합니다. 대형 PR에서는 일부 파일이 제외될 수 있습니다.
- 이는 LLM 기반 자동 리뷰 워크플로로, 자율적인 다단계 도구 사용 Agent와는 구별됩니다.
