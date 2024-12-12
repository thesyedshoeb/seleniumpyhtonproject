pipeline {
    agent any

    environment {
        PYTHON_HOME = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.12'
        VENV_PATH = 'venv'
        GIT_REPO_URL = 'https://github.com/thesyedshoeb/seleniumpyhtonproject.git'
        BRANCH_NAME = 'main'
        ALLURE_RESULTS_DIR = 'pomproject\\tests\\allure-results'
        ALLURE_REPORT_DIR = 'pomproject\\tests\\allure-report'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: "${GIT_REPO_URL}", branch: "${BRANCH_NAME}"
            }
        }

        stage('Set up Virtual Environment') {
            steps {
                script {
                    echo 'Setting up environment'
                    if (!fileExists(VENV_PATH)) {
                        echo 'Setting up virtual environment'
                        bat '''
                            python -m venv ${VENV_PATH}
                            call ${VENV_PATH}\\Scripts\\activate.bat
                            pip install --upgrade pip
                            pip install -r requirement.txt
                        '''
                    }
                    echo 'Virtual environment setup completed'
                }
            }
        }

        stage('Run Tests with Allure') {
            steps {
                script {
                    echo 'Test execution started with Allure!'
                    bat '''
                        call ${VENV_PATH}\\Scripts\\activate.bat
                        cd pomproject\\tests\\ || exit /b 1
                        echo Current Directory: %CD%
                        pytest test_shop_with_allure_reports.py -v --alluredir=${ALLURE_RESULTS_DIR} || exit /b 1
                    '''
                    echo 'Test execution completed!'
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                script {
                    echo 'Generating Allure report'
                    bat '''
                        call ${VENV_PATH}\\Scripts\\activate.bat
                        allure generate ${ALLURE_RESULTS_DIR} -o ${ALLURE_REPORT_DIR} --clean
                    '''
                    echo 'Allure report generated!'
                }
            }
        }
    }

    post {
        always {
            echo "Cleaning up"
            bat '''
                call ${VENV_PATH}\\Scripts\\deactivate.bat || exit /b 0
            '''
            echo 'Job completed!'
        }
    }
}
