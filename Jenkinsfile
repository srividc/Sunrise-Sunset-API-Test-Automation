pipeline {
  agent any
  stages {
    stage('build') {
      steps {      
        sh '/usr/local/bin/pip install -r requirements.txt'
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
