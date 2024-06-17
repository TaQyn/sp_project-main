# sp_project

Code nhận diện khuôn mặt

## Requirements
```bash
    python 3.8
```
## Installation

1. Clone the repository:
```bash
    git clone https://github.com/trucnguyen13/sp_project.git
    cd sp_project
```
2. Tạo và kích hoạt môi trường ảo:
```bash
    python3.8 -m venv venv
    venv\Scripts\activate
```

3. Cài đặt các thư viện yêu cầu:
```bash
    pip install -r requirements.txt
```
4. Cài đặt các thư viên khác: faiss, tf-keras.

## Chuẩn bị dữ liệu
1. Chuẩn bị hình ảnh trong thư mục `dataset` của thư mục `src`.
```
    Cấu trúc thư mục:

    your-repository/
    ├── src/
    │   ├── dataset/
    │   │   ├── person1/
    │   │   │   ├── image1.jpg
    │   │   │   ├── image2.jpg
    │   │   ├── person2/
    │   │   │   ├── image1.jpg
    │   │   │   └── image2.jpg
    │   │   └── ...
```

## Chạy Mã Trích Xuất Embedding

1. Đảm bảo có các tệp mô hình cần thiết ở đúng đường dẫn:

    - Tên mô hình: `OpenFace`
    - Đường dẫn chỉ mục: `path/to/faiss_index.bin`
    - Đường dẫn nhãn: `path/to/labels.txt`

2. Chạy mã để trích xuất embedding:

```bash
    python src\store_embeddings.py
```
## Chạy
1. Đảm bảo có các tệp mô hình cần thiết ở đúng đường dẫn:
    - Tên mô hình: OpenFace
    - Đường dẫn chỉ mục: path/to/faiss_index.bin
    - Đường dẫn nhãn: path/to/labels.txt

2. Chạy với camera:
```bash
    python infer_video.py
```
