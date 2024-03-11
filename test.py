import cv2

# 웹캠을 사용하기 위해 VideoCapture 객체를 생성합니다.
cap = cv2.VideoCapture(0)  # 0은 기본 웹캠을 의미합니다.

# VideoCapture 객체가 초기화되었는지 확인합니다.
if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

while True:
    # 웹캠에서 프레임을 읽어옵니다.
    ret, frame = cap.read()

    # 프레임을 정상적으로 읽었는지 확인합니다.
    if not ret:
        print("프레임을 읽을 수 없습니다.")
        break

    # 프레임을 화면에 표시합니다.
    cv2.imshow('Webcam', frame)

    # 'q' 키를 누르면 종료합니다.qwdtrtytserc
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 사용이 끝난 자원을 해제합니다.
cap.release()
cv2.destroyAllWindows()
