    agent  { docker { image 'python:3.7.2' } } 
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
    }
  }
}
   
