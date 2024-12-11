 
pipeline {
    agent any

    environment {
        // Define the Python version to use
        PYTHON_VERSION = 'python3'
        VIRTUAL_ENV = '.venv'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from GitHub
                git 'https://github.com/thesyedshoeb/seleniumpyhtonproject.git'
            }
        }

        stage('Set up Python environment') {
            steps {
                script {
                    // Set up a virtual environment and install dependencies
                    sh '''
                    # Create a virtual environment
                    $PYTHON_VERSION -m venv $VIRTUAL_ENV
                    # Activate the virtual environment
                    source $VIRTUAL_ENV/bin/activate
                    # Install the necessary dependencies using pip
                    pip install --upgrade pip
                    pip install selenium pytest
                    '''
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                script {
                    // Run Selenium tests using pytest
                    sh '''
                    # Activate the virtual environment
                    source $VIRTUAL_ENV/bin/activate
                    # Run the tests with pytest
                    pytest --maxfail=1 --disable-warnings --capture=no
                    '''
                }
            }
        }

        stage('Archive Test Results') {
            steps {
                // Archive the test results (for pytest, the default location is 'pytest' output)
                archiveArtifacts artifacts: 'test-reports/*.xml', allowEmptyArchive: true
            }
        }

        stage('Clean up') {
            steps {
                script {
                    // Clean up the virtual environment after testing
                    sh '''
                    # Deactivate and remove the virtual environment
                    deactivate
                    rm -rf $VIRTUAL_ENV
                    '''
                }
            }
        }
    }

    post {
        always {
            // Clean up any workspace or other tasks to run regardless of build success/failure
            cleanWs()
        }
        success {
            // Actions to take on success, such as notifications
            echo 'Tests passed successfully!'
        }
        failure {
            // Actions to take on failure, such as notifications
            echo 'Tests failed. Please check the logs.'
        }
    }
}
