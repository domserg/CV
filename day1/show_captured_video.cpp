#include <opencv2/opencv.hpp>
using namespace cv;
int main() {
	int id = 0;
	VideoCapture cap;
	cap.open(id, CAP_DSHOW);
	Mat frame;
	namedWindow("Original Video", WINDOW_AUTOSIZE);
	int key = -1;
	while (key != 27) {
		cap >> frame;
		imshow("Original Video", frame);
		key = waitKey(33);
	}
	return 0;
}
