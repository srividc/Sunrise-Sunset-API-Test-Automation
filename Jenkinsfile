pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
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
