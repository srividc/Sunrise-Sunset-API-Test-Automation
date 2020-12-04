pipeline {
  agent any
  stages {
    stage('build') {
      steps {      
        sh '/usr/local/bin/pip3 install -r requirements.txt'
        sh 'pip3 install setuptools'
        sh 'pip3 install --upgrade pip'
        sh 'python3 -m ensurepip'
      }
    }
    stage('test') {
      steps {
        sh 'python3 test_sunrise_sunset.py'
      }
      post {
        always {
          echo "I am done"
        }
      }    
    }
  }
}
