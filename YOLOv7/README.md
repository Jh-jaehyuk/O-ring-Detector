# Machine Learning - (Model : YOLOv7)

### 주의 사항 ‼️
* 여기서는 [링크](https://github.com/WongKinYiu/yolov7) 의 파일들을 "C:/Users/{Username}"에 넣고 진행함
* 파일들을 다운받은 후에 필수 라이브러리 설치 필요   
    ```
    pip install -r requirements.txt
    ```

</br>

### 진행 과정 📆
1. YOLO Custom Model 작성
   * custom_data.yaml
   * yolov7-custom.yaml   
2. Train 데이터 만들기
   * data.zip/train/images
   * data.zip/train/labels   
     - labelImg 를 이용한 라벨링
       ```
       pip install labelImg # 설치
       labelmg # 실행
       ```
       + 이미지 파일을 지정하고 레이블 포맷을 yolo로 설정
       + 사각형으로 이미지 파일에서 필요한 부분을 지정
       + 필요한 이미지만큼 반복 작업   
3. Machine Learning
   * cmd에서 train.py 실행
     ```
     python train.py --workers 1 --device 0 --batch-size 4 --epochs 100 --img 640 640 --data data/custom_data.yaml --hyp data/hyp.scratch.custom.yaml --cfg cfg/training/yolov7-custom.yaml --name yolov7-custom --weight yolov7-tiny.pt
     ```
     - 코드 설명   
       --workers 1 : 컴퓨터 한 대   
       --device 0 : 그래픽 카드 번호   
       --batch-size 4 : 한번에 연산하는 데이터의 크기   
       --epochs 10 : epoch의 횟수   
       --img 640 640 : 각 pt 마다 고정된 값   
       --data data/custom_data.yaml : 데이터 정보가 있는 yaml 위치   
       --hyp data/hyp.scratch.custom.yaml : 하이퍼파라미터 정보가 있는 yaml 위치   
       --cfg cfg/training/yolov7-custom.yaml : cfg 정보가 있는 yaml 위치   
       --name yolov7-custom : 저장 위치   
       --weights yolo7-tiny.pt : 가중치의 위치
   * 여기서는 노트북 성능이 좋지 않아 **batch-size, epoch, model, weights 전부 기본보다 낮추어 사용**   
4. YOLO 구동 및 Model 신뢰도 평가
   * YOLOv7_test.jpg   
     - 사진에서 사각형 위쪽의 왼쪽이 레이블, 오른쪽이 신뢰도
     - 레이블은 정상적으로 O-ring이라고 표시
     - 그러나, 신뢰도가 0.3 후반에서 0.7까지 들쑥날쑥함

</br>

### image 를 통한 YOLOv7 작동 방법 🖼️
1. image_object_detection.py 를 실행
2. 파이썬 파일 내부의 이미지 파일 경로를 지정(이 코드에서는 사진을 인터넷에 올려둔 후, url 을 통해 이미지 가져오는 방법을 사용)
3. cmd 실행 후 py 파일 경로로 이동 후 py 실행   
   ```
   cd {directory}/ # 경로 이동
   python image_object_detection.py # 실행
   ```

</br>

### 문제점 :x:
1. 학습시킨 모델의 성능이 낮아서 인식은 되지만 낮은 신뢰도를 보여줌.
   * 이는 컴퓨터의 성능을 개선하여 높은 성능의 모델과 가중치를 이용하면 개선될 것으로 생각됨
2. 신뢰도를 수정한 이후에 어느정도 작은 불량까지 검출할 수 있는지 확인되지 않음.
   * O-ring 특정 상 매우 작은 불량이 많아서 **YOLO 모델로는 더 이상의 진행을 보류함**
