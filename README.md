# COVID-19 Diagnosis Mobile Application

This project presents a mobile application that leverages computer vision and deep learning techniques to provide a rapid and accurate diagnosis of COVID-19 through X-ray images. The study utilizes transfer learning and fine-tuning of the pre-trained Inception-V3 model on the ImageNet dataset to achieve optimal performance. The application allows users to take X-ray images and receive clear and user-friendly COVID-19 detection results as well as COVID-19-related safety guidance reminders. Furthermore, the mobile app collects data that will be used by the scientific community to improve the accuracy and reliability of COVID-19 automatic screening. The software offers better generalization results, making it particularly useful for primary screening in areas with limited test kits and medical expertise. Ultimately, the application has the potential to improve the speed and accuracy of COVID-19 diagnosis, benefiting patients, radiologists, and the healthcare industry as a whole.

## Features

The application allows users to:

- Take X-ray images
- Receive clear and user-friendly COVID-19 detection results
- Receive COVID-19-related safety guidance reminders
- Fill out a questionnaire to aid in decision-making

The software offers better generalization results, making it particularly useful for primary screening in areas with limited test kits and medical expertise. Furthermore, the mobile app collects data that will be used by the scientific community to improve the accuracy and reliability of COVID-19 automatic screening.

## Technologies Used

- Computer vision
- Deep learning
- X-ray images
- Mobile application
- Retrofit
- Flask backend

## Installation

To use the application, clone the repository and install the necessary dependencies.

pip install Keras==2.4.3 opencv-python==4.4.0.44 scikit-learn==0.23.2 numpy==1.18.5 pandas==1.1.3 scipy==1.4.1 tensorflow==2.3.0 h5py==2.10.0


## Usage

To use the application, simply run it on your Android mobile device. The user interface allows the user to take images via their smartphone camera and fill out a questionnaire to aid in decision-making.

## Backend

The backend is built using Flask, a RESTful API for the Python web server. It receives requests from the frontend and processes them. MongoDB is used as a database to store images, classification results, and user data. All data transferred to the application is fully anonymized, including metadata. It has been hypothesized that an individual is not identifiable from anonymized data.

## DL Module

The DL module uses the TensorFlow Inception-V3 model for the analysis and classification of X-ray images. The Inception-V3 model was pre-trained on ImageNet dataset Deng et al. (2009) and fine-tuned by gradually unfreezing the top layers of the convolutional part of the model on a collection of chest X-ray images Errattahi et al. (2022). The total number of thoracic images used to fine-tune our model is 4187 thoracic images for 3883 different subjects. Where 1227 images are labeled with positive COVID-19 diagnosis. While the normal images and non-COVID pneumonia represent a total of 2910 images. The final model is loaded into the Flask backend and used to process images submitted by users.

## Web Frontend

The web frontend is built using jQuery Ajax to communicate with the Flask backend. Through the web user interface, the users can capture images using their computer's webcam and complete a questionnaire to assist decision-making.

## Credits

This project was developed by ENSAJ Team.


## License

This project is licensed under the MTI.
