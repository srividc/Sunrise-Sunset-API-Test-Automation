    agent any 
    stages {
        stage('Run Unit tests to Test the Sunrise API') {
            steps {
                echo 'Run Unit tests to Test the Sunrise API' 
            }
        }
       
        stage('Run Unit Tests') {
            steps {
                      sh 'virtualenv venv && . venv/bin/activate && pip install -r requirements.txt && python tests.py'
                echo 'Run all Unit tests from the source code' 
            }
        }
        stage('Publish Artifacts') {
            steps {
                echo 'Save the assemblies generated from the compilation' 
            }
        }
    }
}
