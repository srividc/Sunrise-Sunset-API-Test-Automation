pipeline {
  agent any
  stages {
    stage('build') {
      steps {      
        sh '/usr/local/bin/pip3 install -r requirements.txt'

      }
    }
    stage('test') {
      steps {
        sh 'python -m pytest -v -s test_sunrise_sunset.py'
      }
      post {
        always {
          
        }
      }    
    }
  }
}
