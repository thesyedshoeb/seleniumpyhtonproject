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
                bat 'pip install -r requirement.txt'
            }
        }
        stage('Run Tests') {
            steps {
                bat '''
                    cd pomproject\tests\
                    echo Current Directory: %CD%
                    pytest test_shop_with_allure_reports.py -v --alluredir=allure-results
                '''
            }
        }
        stage('Generate Allure Report') {
            steps {
                bat 'allure generate pomproject\tests\allure-results --clean -o allure-report'
            }
        }
    }
    
    post {
        always {
            archiveArtifacts artifacts: '**/allure-report/**', allowEmptyArchive: true
            allure includeProperties: false, jdk: '', results: [[path: 'pomproject/tests/allure-results']]
        }
        failure {
            mail to: 'shoeb.syed@infobeans.com', subject: "Build Failed: ${env.JOB_NAME}", body: "Please check the Jenkins build log."
        }
    }
}
