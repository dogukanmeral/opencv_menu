import cv2

def capture_frame_to_file(camera_port, file_name_to_write, capture_key):
	camera = cv2.VideoCapture(camera_port)

	while True:
		result, frame = camera.read()
		cv2.imshow('frame', frame)

		if cv2.waitKey(1) & 0xFF == ord(capture_key):
			cv2.imwrite(file_name_to_write, frame)

			camera.release()
			cv2.destroyAllWindows()
			break