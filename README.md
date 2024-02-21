# Road Damage Detection Using YOLO

The present research examines the development of a road damage detection model and its potential implications on the economy and society. The timely and accurate identification of deteriorated road conditions has the potential to significantly reduce vehicular accidents, improve traffic flow, and ultimately save lives. The adoption of this technology can also yield substantial financial benefits for governmental entities and road management associations by enhancing the prioritization and scheduling of maintenance and repair tasks. Notably, deep learning techniques, particularly the YOLOv7 model, have contributed to notable improvements in detection accuracy, reduced computational complexity, and overall effectiveness. This study involved conducting several experiments comparing the performance of YOLOv5 and YOLOv7 models. The results highlight the superior performance of the YOLOv7 architecture in accurately identifying damaged areas and predicting object categories. The utilisation of the YOLOv7 model in deep learning and computer vision has led to significant advancements in the precision and efficiency of road damage detection models. The findings from a series of experiments comparing YOLOv5 and YOLOv7 models demonstrate the enhanced effectiveness of the YOLOv7 architecture in accurately detecting damaged regions and predicting object categories. Various methodologies, including hyperparameter optimization and image augmentation techniques, were employed to improve precision. The initial experiment incorporated rotation, hue saturation value configuration, image scaling, and flipping techniques resulting in an average accuracy of 79.75% across all test image categories using YOLOv7. However, Experiment 2 revealed limitations in the implementation of the Gaussian Blur method on YOLOv7, leading to a bias toward blurred images and a consequent compromise in overall precision, resulting in an accuracy of 19.75%. In Experiment 3, the YOLOv5 algorithm was used with a refined dataset, yielding an average accuracy of 55.75% across all categories, which was lower than the accuracy achieved in the first experiment using YOLOv7. This study suggests employing the YOLOv7-trained model as a means of detecting road damage, in conjunction with various image augmentation techniques. According to the findings, the model attained an F1 score of 75%. The adoption of this technology in practical applications is justified by its exceptional performance, which provides significant insights into the state of road conditions and enables timely maintenance and repair interventions. It is also recommended to utilise the designated software in this study to facilitate the convenient implementation of the proposed model by end-users. Further research and improvement of the model may reveal its complete capabilities in augmenting road infrastructure administration and guaranteeing more secure and effective transportation systems.

## **Experiment 1 (YOLOv7)**
| **Labelled** | **Predicted** |
| ----- | -----|
|![test_batch2_labels](https://github.com/MizanMustakim/thesis_work/assets/56040932/ddab5a20-4c75-43e1-b0c7-2f1a9d157bd3)|![test_batch2_pred](https://github.com/MizanMustakim/thesis_work/assets/56040932/d31427d1-a531-49a6-9221-c6d5fa30a654)|

## **Experiment 2 (YOLOv7 Augmented)**
| **Labelled** | **Predicted** |
| ----- | -----|
||On Testing||


## **Experiment 3 (YOLOv5)**
| **Labelled** | **Predicted** |
| ----- | -----|
|![val_batch2_labels](https://github.com/MizanMustakim/thesis_work/assets/56040932/898e129f-dee3-4fa3-8ee8-74a152a83e67)|![val_batch2_pred](https://github.com/MizanMustakim/thesis_work/assets/56040932/8172c56d-199c-4df4-b9e1-340908c5a27d)|


## **Real Time Testing**
![real_time_Model_Experiment](https://github.com/MizanMustakim/thesis_work/assets/56040932/a03d2b65-8568-458b-8f81-612b9c99785d)

## **Designed Computer Software Interface**
### *Pipeline*
![image](https://github.com/MizanMustakim/thesis_work/assets/56040932/0b23d8a8-fe41-41d5-a2a8-8ccd17f2355e)

## **Paper Link**
[Road Damage Detection Based on Deep Learning](https://www.researchgate.net/publication/372769154_Road_Damage_Detection_Based_on_Deep_Learning)
