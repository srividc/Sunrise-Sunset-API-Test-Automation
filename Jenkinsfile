pipeline {
  agent any
  stages {
    stage('build') {
      steps {      
        sh 'pip3 install setuptools'
        sh 'pip3 install requests --user'
        sh 'pip3 install behave --user'
        sh 'pip3 install pytest --user'
        sh 'pip3 install pytest-html --user'
      }
    }
    stage('test') {
      steps {
        sh 'python3 -m pytest -v -s --capture=sys test_sunrise_sunset.py --html=report.html'
      }
        post {
        always {
          mail to: srividc26@gmail.com, subject: 'The Python API tests were run '
        }
          success{
            mail to: srividhya.chandrasekar@gmail.com, subject: 'The Python API tests Passed! :)'
          }
        failure {
            mail to: srividhya.chandrasekar@gmail.com, subject: 'The Python API tests failed :('
        }
    }
    }
  }
}
