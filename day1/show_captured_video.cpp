#include <opencv2/opencv.hpp>
using namespace cv;
int main() {
	VideoCapture video;
	video.open(0, CAP_DSHOW);
	Mat frame;
	namedWindow("Original Video", WINDOW_AUTOSIZE);
	for (;;) {
		video >> frame;
		imshow("Original Video", frame);
		waitKey(33);
	}
	return 0;
}
