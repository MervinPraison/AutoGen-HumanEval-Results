# filename: strong_extension_test.py
import strong_extension

def test_strongest_extension():
    class_name = "my_class"
    extensions = ["AA", "be", "CC"]
    result = strong_extension.Strongest_Extension(class_name, extensions).find_strongest()
    print("Expected: my_class.AA")
    print("Got:", result)
    if result != "my_class.AA":
        print("\nTest failed!\n")
        print(f"Input values:\nClass name: {class_name}\nExtensions: {extensions}")
        print(f"\nFunction internal state (before and after processing):")
        print("Before:\n{strong_extension.Strongest_Extension.__dict__}")
        strong_extension_instance = strong_extension.Strongest_Extension(class_name, extensions)
        print("\nAfter:")
        print(f"\n{strong_extension_instance.\_class\_.\_\_dict\__}")
        assert False
    else:
        print("\nTest passed!\n")

if __name__ == "__main__":
    test_strongest_extension()