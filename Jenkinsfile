// CI/CD pipeline
pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/HarshitaKadiwal/codejudge.git'
            }
        }

        stage('Verify Project Files') {
            steps {
                sh 'ls -la'
            }
        }

        stage('Check Important Files') {
            steps {
                sh '''
                echo "Checking required project files..."
                test -f app.py
                test -f Dockerfile
                test -f requirements.txt
                test -d templates
                test -d static
                test -d database
                test -d judge
                echo "All important files are present."
                '''
            }
        }

        stage('CI Completed') {
            steps {
                echo 'CodeJudge CI pipeline completed successfully.'
                echo 'Source code was fetched from GitHub and project structure was verified.'
                echo 'Docker deployment is demonstrated separately from terminal.'
            }
        }
    }
}