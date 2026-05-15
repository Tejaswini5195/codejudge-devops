pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Tejaswini5195/codejudge-devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t codejudge-app .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run -d -p 5000:5000 codejudge-app'
            }
        }

    }
}