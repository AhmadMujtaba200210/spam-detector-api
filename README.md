# Spam Detector API

Welcome to the Spam Detector API repository! This API is built using Keras, TensorFlow, and LSTM, trained on custom data to effectively classify spam and non-spam messages.

## Overview

This Spam Detector API leverages deep learning techniques, specifically LSTM (Long Short-Term Memory) models, to analyze and classify messages as either spam or non-spam. The model is trained on a custom dataset, ensuring high accuracy and reliability in detecting spam patterns.

## Features

- **Deep Learning Model:** Utilizes LSTM neural networks for sequence modeling, capturing intricate patterns in text data.
- **Custom Dataset:** Trained on a carefully curated dataset to enhance performance and adaptability to diverse spam scenarios.
- **Scalable Dockerized API:** Deploy the model seamlessly using the Docker containerization platform for scalability and ease of use.

## Usage

### API Endpoint

- **Predict:** `GET /spam` - Make a POST request with the text data you want to classify as the request payload. The API will respond with the prediction result.

## Getting Started

Follow these steps to set up the Spam Detector API locally:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/spam-detector-api.git
    cd spam-detector-api
    ```

2. **Build and run the Docker container:**

    ```bash
    docker build -t spam-detector-api .
    docker run -p 8000:8000 spam-detector-api
    ```

3. **Access the API at `http://localhost:8000`.**
## You can also used prebuild image here:

  ```bash
    docker pull ahmadmujtaba200210/spam-classifier
    docker run -p 8000:8000 spam-detector-api
  ```

## Contributing

If you'd like to contribute to the development of the Spam Detector API, please follow our [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

We would like to express our gratitude to the open-source community and contributors who have made this project possible.

Feel free to reach out with any questions or feedback!

Happy spam detecting!
