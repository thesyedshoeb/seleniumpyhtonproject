pipeline {
    agent any

    environment {
        PYTHON_HOME = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.12'
        VENV_PATH = 'venv'
        GIT_REPO_URL = 'https://github.com/pmojumder/pythonProject.git'
        BRANCH_NAME = 'main'
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
                    if (!fileExists('venv')) {
                        echo 'Setting up virtual environment'
                        bat '''
                            python -m venv venv
                            venv\\Scripts\\activate.bat
                            pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    }
                    echo 'Virtual environment setup completed'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    echo 'Test execution started!'
                    bat '''
                        call venv\\Scripts\\activate.bat
                        python 'Test_Folderpytest\test_new.py'

                    '''
                    echo 'Test execution completed!'
                }
            }
        }
    }

    post {
        always {
            echo "Cleaning up"
            bat '''
                call venv\\Scripts\\deactivate.bat
            '''
            echo 'Job completed!'
        }
    }
}
