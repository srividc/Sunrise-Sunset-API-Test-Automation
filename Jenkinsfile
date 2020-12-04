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
          message '$ The Python API tests {currentBuild.fullDisplayName} were run'
        }
          success{
            message '$ The Python API tests {currentBuild.fullDisplayName} were successful'
          }
        failure {
            message '$ The Python API tests {currentBuild.fullDisplayName} failed'
        }
    }
    }
  }
}
