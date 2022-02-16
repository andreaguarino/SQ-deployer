from deployer import deploy_sonar_python
import os
from pathlib import Path


def test_deploy(tmp_path):
    sonar_python_version = 1.1
    sonar_python_jar = f"{tmp_path}/sonar-python-plugin/target/sonar-python-plugin-{sonar_python_version}-SNAPSHOT.jar"
    os.makedirs(os.path.dirname(sonar_python_jar), exist_ok=True)
    os.makedirs(f"{tmp_path}/lib/extensions")
    Path(sonar_python_jar).touch()
    deploy_sonar_python(tmp_path, sonar_python_version, tmp_path)
    assert os.path.exists(f"{tmp_path}/lib/extensions/sonar-python-plugin-{sonar_python_version}-SNAPSHOT.jar")

