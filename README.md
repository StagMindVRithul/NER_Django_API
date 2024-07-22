# Medical Entity Recognition App

This repository contains a Django REST application for medical entity recognition. The app allows users to input medical text data, which is then processed by a trained Named Entity Recognition (NER) model. The model identifies and categorizes relevant medical entities present in the text, such as medical names, categories, strengths, packaging information, and additional dimensions.

## Featues: 

* User-friendly UI for text input and displaying categorized entities
* User registration and authentication
* Backend implemented using Django REST Framework
* Integration with a custom-trained NER model for entity recognition
* Storage of user entries with text, results, date/time, and username
* Dockerized for easy deployment and cross-platform compatibility


## Overview of the Medical Entity Recognition App:
1. This is Login Page
   
![Screenshot 2024-06-06 at 3 58 30 PM](https://github.com/StagMindRithul/NER_Django_API/assets/171004389/47d0c370-9cc3-42ee-81f9-48fe2bca1011)

2. This is the Registeration Page

![Screenshot 2024-06-06 at 3 58 47 PM](https://github.com/StagMindRithul/NER_Django_API/assets/171004389/07806fba-a75b-41d6-ad0f-0e7e07d1eed2)

3. This is the Home Page

![Screenshot 2024-06-06 at 3 59 12 PM](https://github.com/StagMindRithul/NER_Django_API/assets/171004389/06a80825-dc51-4a27-8eff-e85e775d06ac)

On the top left corner, click on -> Medical Data, It will redirect you to the Input text page

4. This is the Medical Data Page

![Screenshot 2024-06-06 at 3 59 29 PM](https://github.com/StagMindRithul/NER_Django_API/assets/171004389/398a6c5c-9176-4205-bf0d-7c6b510ef4fa)

Enter the name of the medicine here and click on the "Know the details" Button. 

5. Back to Home Page

![Screenshot 2024-06-06 at 3 59 39 PM](https://github.com/StagMindRithul/NER_Django_API/assets/171004389/7b200050-74ac-4e76-925e-a4421b421098)

Here the input data will displayed along with labels and entities. You can keep on adding the medical data here to know the details. Once done, Please logout. 

## Usage

To ensure a seamless experience and facilitate the deployment process, I recommend leveraging the existing Docker image available on my DockerHub repository. Follow the below steps:

* Clone the repository
* Pull the Docker image: docker pull stagmindrithul/medical-ner
* Ru n the Docker container: docker run -p 8000:8000 stagmindrithul/medical-ner
* Access the application at http://localhost:8000

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any questions or inquiries, please contact the project maintainers at rithul.v@stag-ai.com

## Note

If you choose to run the application locally without using the Docker image, please unzip the NER_Model file and ensure that the path to the NER model in the code is correct.









