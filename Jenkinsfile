pipeline {
  agent any
  stages {
    stage('build') {
      steps {      
        sh 'sudo /usr/local/bin/pip install -r requirements.txt'
        sh 'sudo pip install setuptools'
        sh 'python -m ensurepip'
      }
    }
    stage('test') {
      steps {
        sh 'python test_sunrise_sunset.py'
      }
      post {
        always {
          echo "I am done"
        }
      }    
    }
  }
}
