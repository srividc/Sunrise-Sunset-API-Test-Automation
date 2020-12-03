pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sudo python -m pip install --upgrade pip
        sudo pip install --upgrade setuptools       
        sh '/usr/local/bin/pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python3 test_sunrise_sunset.py'
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
      }    
    }
  }
}
