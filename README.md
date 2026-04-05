# Sentiment Analysis API

## Thông tin sinh viên
- Họ và tên: Trần Nguyễn Quốc Khánh
- MSSV: 24120192

## Mô hình sử dụng
- Tên mô hình: cardiffnlp/twitter-roberta-base-sentiment-latest
- Link: https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest
- Chức năng: Phân tích cảm xúc văn bản, phân loại Positive / Negative / Neutral

## Chức năng hệ thống
API nhận đầu vào là một đoạn văn bản và trả về nhận cảm xúc cùng với độ tin cậy.

## Cài đặt thư viện
```
py install requirements.txt
```

## Chạy chương trình
```
py -m uvicorn main:app --host 0.0.0.0 --port 8000  
```

## Hướng dẫn gói API

### GET /
```
curl.exe https://nonclinging-gabriel-bewhiskered.ngrok-free.dev/
```

### GET /health
```
curl.exe https://nonclinging-gabriel-bewhiskered.ngrok-free.dev/health
```

### POST /predict
```
Invoke-RestMethod -Method POST -Uri "https://nonclinging-gabriel-bewhiskered.ngrok-free.dev/predict" -ContentType "application/json" -Body '{"text": "I love you"}'
```
Ket qua tra ve:
{
  "text": "I love this!",
  "label": "positive",
  "score": 0.9823
}
## Video demo  
```
https://drive.google.com/file/d/1GVTjHbQ1n738JPyCjVtq2brVGmCoTqWn/view?usp=sharing  
```
