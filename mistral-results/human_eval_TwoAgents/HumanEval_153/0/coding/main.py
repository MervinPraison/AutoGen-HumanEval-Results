# filename: main.py

from my_tests import run_tests
import strong_extension

class TestMyClass:
    def test_strongest_extension(self, capf):
        class_name = "Slices"
        extensions = ["SErviNGSliCes", "Cheese", "StuFfed"]
        assert strong_extension.Strongest_Extension(class_name, extensions) == "Slices.SErviNGSliCes"

run_tests(TestMyClass())