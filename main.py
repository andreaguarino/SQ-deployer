from deployer import deploy_sonar_python
import sys

if __name__ == "__main__":
    sonarpython_version = sys.argv[2]
    sonarpython_location = "~/git_clone/sonar-python"
    sonarqube_location = "~/git_clone/Products/SQ/sonarqube-9.2.1.49989"
    deploy_sonar_python(sonarpython_location, sonarpython_version, sonarqube_location)

