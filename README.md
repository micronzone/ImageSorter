# ImageSorter

ImageSorter는 사용자가 지정한 디렉토리 경로에 있는 이미지 파일들을 확장자별로 분류하여 해당 확장자명을 가진 디렉토리로 이동시키는 Python 스크립트입니다. 파일 이동 전에 이동 계획을 사용자에게 보여주고 선택할 수 있는 기능과 상세한 디버깅 로그 기능을 제공합니다.

> 다운로드 폴더에 계속 쌓이는 알 수 없는 이미지 파일들을 정리하고자 만들었습니다.

### 기능
- 디렉토리 경로에 있는 이미지 파일들을 확장자별로 자동 분류하여 이동
- 특정 확장자를 가진 파일만 선택 분류하여 이동
- 이동 전 파일 이동 계획을 사용자에게 보여주고 선택 가능
- 동일한 이미지 파일명이 있으면 접미사 생성
- 디버깅 로그 기능 제공

<img width="682" alt="ss" src="https://github.com/micronzone/ImageSorter/assets/47780105/e1449ad9-a454-47a4-812b-988005b93c2a">

### 설치 방법

이 리포지토리를 클론합니다:
```sh
git clone https://github.com/micronzone/ImageSorter.git
cd ImageSorter
```

(선택 사항) 가상 환경을 생성하고 활성화합니다:
```sh
python3 -m venv myenv
source myenv/bin/activate  # Linux 또는 macOS
.\myenv\Scripts\activate   # Windows
```

### 사용법
```bash
python3 ImageSorter.py [기본 옵션] [디렉토리 경로]
python3 ImageSorter.py [기본 옵션] [추가 옵션] [디렉토리 경로]
```

### 옵션
기본 옵션:
- `-a`: 지정된 디렉토리에 있는 모든 이미지 파일을 확장자별로 분류하여 이동
- `-t {이미지 확장자}`: 특정 확장자를 가진 이미지 파일만 분류하여 이동 (예: `-t jpg`)

추가 옵션:
- `-l {DEPTH}`: 하위 디렉토리의 깊이를 지정하여 적용 (예: `-l 2`)

디버깅 옵션:
- `--debug`: 디버깅 로그 출력

### 예제

모든 이미지 파일을 확장자별로 자동 분류하여 이동:

```sh
python3 ImageSorter.py -a /path/to/directory

```

특정 확장자(예: `jpg`)를 가진 파일만 이동:
```sh
python3 ImageSorter.py -t jpg /path/to/directory

```

하위 디렉토리 깊이 `3`까지 모든 이미지 파일을 확장자별로 자동 분류하여 이동: (예: `/path/to/directory/./dir1/dir2`)
```sh
python3 ImageSorter.py -a -l 3 /path/to/directory

```

하위 디렉토리 깊이 `3`까지 특정 확장자(예: `jpg`)를 가진 파일만 이동: (예: `/path/to/directory/./dir1/dir2`)
```sh
python3 ImageSorter.py -t jpg -l 3 /path/to/directory
```


디버깅 로그를 활성화하여 이동:
```sh
python3 ImageSorter.py -a --debug /path/to/directory

```

### 업데이트

ImageSorter 리포지토리 업데이트를 확인하는 것이 좋습니다!

```sh
cd ImageSorter
git status
```

변경 사항 가져오기:

```sh
git pull origin main
```

### 기여 방법

기여해주셔서 감사합니다! 이 프로젝트에 기여하시려면 아래 단계를 따라 주세요:

1. 이 리포지토리를 포크하세요
2. 기능 브랜치(micronzone 브랜치)를 생성하세요 (`git checkout -b micronzone/ImageSorter`)
3. 변경 사항을 커밋하세요 (`git commit -m 'Add some ImageSorter'`)
4. 브랜치에 푸시하세요 (`git push origin micronzone/ImageSorter`)
5. 풀 리퀘스트를 여세요

### 라이센스

이 프로젝트는 MIT 라이센스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참고하세요.
