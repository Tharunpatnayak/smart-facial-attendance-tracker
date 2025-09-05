import cv2

def test_camera_indices(max_index=5):
    for index in range(max_index):
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                print(f"Camera found at index {index}")
                cv2.imshow(f"Camera {index}", frame)
                cv2.waitKey(2000)  # Display for 2 seconds
                cv2.destroyAllWindows()
            else:
                print(f"Index {index} opened but failed to capture frame")
            cap.release()
        else:
            print(f"No camera found at index {index}")

if __name__ == "__main__":
    test_camera_indices(5)  # Test indices 0 to 4