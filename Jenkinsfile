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
        sh 'python -m pytest -v -s --capture=sys test_sunrise_sunset.py --html=report.html
      }
      post {
        always {
          
        }
      }    
    }
  }
}
