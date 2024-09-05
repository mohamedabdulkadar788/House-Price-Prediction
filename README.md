# House Price Prediction

This project guides you through the entire process of creating a real estate price prediction website. We begin by developing a predictive model using scikit-learn and linear regression, utilizing the Bangalore House price dataset. The project involves creating a Python Flask server that will host the model and handle HTTP requests. Finally, we'll build a website using HTML, CSS, and JavaScript, where users can input details such as square footage and number of bedrooms. The website will then interact with the Flask server to retrieve the predicted price.

Throughout the model-building phase, we will explore a wide range of data science concepts, including data loading and cleaning, detecting and removing outliers, feature engineering, dimensionality reduction, hyperparameter tuning with GridSearchCV, and k-fold cross-validation.

Tools & Techniques used:
  `i)Front End - HTML, CSS, JS`
  `ii)Back End - Flask`
  `iii)Machine Learning - Regression Analysis `

### Deployment Details

- **Amazon EC2 Instance**:
  - The Flask application for house price prediction is hosted on an Amazon EC2 instance.
  - The EC2 instance was selected to ensure scalability and availability of the application.
  - **Instance Type:** (Specify the instance type, e.g., t2.micro)
  - **Region:** (Specify the AWS region, e.g., eu-north-1)
  
- **Nginx**:
  - Nginx is used as a reverse proxy to forward requests from the public internet to the Flask application running on the EC2 instance.
  - Nginx handles static file serving and provides additional security and performance optimizations.
  - The Nginx configuration ensures that the application is accessible via HTTP/HTTPS.

### Project Setup

1. **AWS EC2 Setup**:
   - Launch an EC2 instance with the desired operating system.
   - Configure security groups to allow inbound traffic on necessary ports (e.g., 80 for HTTP, 443 for HTTPS).
   - SSH into the EC2 instance to set up the environment.
   - Connect to your instance using the following command
   ```ssh -i "C:\Users\Viral\.ssh\Banglore.pem" ubuntu@ec2-3-133-88-210.us-east-2.compute.amazonaws.com```

2. **Nginx Configuration**:
   - Install Nginx on the EC2 instance.
   - Configure Nginx to serve as a reverse proxy for the Flask application.
   - The following commands are used to update files and install nginx on EC2 instance.
     ```sudo apt-get update```
     ```sudo apt-get install nginx```
   - Sample Nginx configuration:
     ```
     server {
      listen 80;
          server_name bhp;
          root /home/ubuntu/BHPP/FrontEnd;
          index app.html;
          location /api/ {
               rewrite ^/api(.*) $1 break;
               proxy_pass http://127.0.0.1:5000;
            }
        }
     ```

3. **Running the Flask Application**:
   - Run the Flask application on the EC2 instance:
     ```bash
     python3 server.py
     ```
   - The application will be accessible at `(https://ec2-16-171-182-230.eu-north-1.compute.amazonaws.com/)` or the configured domain name.

### Usage

Visit the deployed application at [House price prediction](https://ec2-16-171-182-230.eu-north-1.compute.amazonaws.com/) to interact with the house price prediction model.


  


