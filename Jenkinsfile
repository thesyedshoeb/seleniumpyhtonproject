pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                bat 'pytest --alluredir=allure-results'
            }
        }
        stage('Generate Allure Report') {
            steps {
                bat 'allure generate allure-results --clean -o allure-report'
            }
        }
    }
    
    post {
        always {
            archiveArtifacts artifacts: '**/allure-report/**', allowEmptyArchive: true
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
        failure {
            mail to: 'youremail@example.com', subject: "Build Failed: ${env.JOB_NAME}", body: "Please check the Jenkins build log."
        }
    }
}
