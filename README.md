# ImageSorter

ImageSorter는 사용자가 지정한 디렉토리 경로에 있는 이미지 파일들을 확장자별로 분류하여 해당 확장자명을 가진 디렉토리로 이동시키는 Python 스크립트입니다. 파일 이동 전에 이동 계획을 사용자에게 보여주고 선택할 수 있는 기능과 상세한 디버깅 로그 기능을 제공합니다.

## 기능
- 사용자가 지정한 디렉토리 경로에 있는 이미지 파일들을 확장자별로 분류하여 이동
- 이동 전 파일 이동 계획을 사용자에게 보여주고 선택 가능
- 디버깅 로그 기능 제공

## 설치 방법

1. 이 레포지토리를 클론합니다:
    ```sh
    git clone https://github.com/micronzone/ImageSorter.git
    cd ImageSorter
    ```

2. (선택 사항) 가상 환경을 생성하고 활성화합니다:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # Linux 또는 macOS
    .\venv\Scripts\activate   # Windows
    ```

## 사용법
```bash
python ImageSorter.py [디렉토리 경로]
python ImageSorter.py [옵션1] [디렉토리 경로]
python ImageSorter.py [옵션1] [옵션2] [디렉토리 경로]
```

## 옵션
- `-a`: 지정된 디렉토리에 있는 모든 이미지 파일을 확장자별로 분류하여 이동
- `-t {이미지 확장자}`: 특정 확장자를 가진 이미지 파일만 분류하여 이동 (예: `-t jpg`)
- `-l {DEPTH}`: 하위 디렉토리의 깊이를 지정하여 적용 (예: `-l 2`)
- `--debug`: 디버깅 로그 출력

## 예제

모든 이미지 파일을 확장자별로 분류하여 이동:

```sh
python ImageSorter.py -a /path/to/directory

```

특정 확장자(예: `jpg`)를 가진 파일만 이동:
```sh
python ImageSorter.py -t jpg /path/to/directory

```

하위 디렉토리 깊이 `3`까지 적용하여 이동:
```sh
python ImageSorter.py -a -l 3 /path/to/directory

```

디버깅 로그를 활성화하여 이동:
```sh
python ImageSorter.py -a --debug /path/to/directory

```


