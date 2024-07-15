#include <opencv2/opencv.hpp>
#include <iostream>
#include "tello.hpp"

int main()
{
    Tello tello;
    if (!tello.connect()) return 0;
    tello.enable_video_stream();

    cv::VideoCapture capture("udp://0.0.0.0:11111");
    int key = -1;
    while (key != 27) {
        cv::Mat frame, gray, bin;
        capture >> frame;
        if (!frame.empty()) {
            cv::cvtColor(frame, gray, cv::COLOR_BGR2GRAY);
            cv::inRange(frame, cv::Scalar(0, 100, 1000), cv::Scalar(20, 255, 255), bin);
            cv::imshow("Tello Stream", frame);
            cv::imshow("Gray", gray);
            cv::imshow("Bin", bin);
        }
        key = cv::waitKey(1);
    }
	return 0;
}
