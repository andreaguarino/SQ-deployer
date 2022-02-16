from shutil import copyfile
import sys


def deploy_sonar_python(sonar_python_location, sonar_python_version, sonarqube_location):
    src = f"{sonar_python_location}/sonar-python-plugin/target/sonar-python-plugin-{sonar_python_version}-SNAPSHOT.jar"
    dest = f"{sonarqube_location}/lib/extensions/sonar-python-plugin-{sonar_python_version}-SNAPSHOT.jar"
    copyfile(src, dest)
