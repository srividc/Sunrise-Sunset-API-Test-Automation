pipeline {
  agent any
  stages {
    stage('build') {
      steps {      
        sh '/usr/local/bin/pip3 install -r requirements.txt'
        sh 'python3 -m ensurepip3'
        sh '/usr/local/bin/pip3 install requests'
      }
    }
    stage('test') {
      steps {
        sh 'python2 test_sunrise_sunset.py'
      }
      post {
        always {
          echo "I am done"
        }
      }    
    }
  }
}
