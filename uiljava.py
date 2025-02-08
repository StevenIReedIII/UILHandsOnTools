import os
import shutil

def prompt_for_first_program():
    """Prompt the user for the first program name if needed."""
    program_name = input("Enter the name of the first program (without .java): ").strip()
    return program_name.capitalize()

def ensure_dryrun_files(source_dir):
    """Ensure dryrun.dat and DryRun.java exist and handle them correctly."""
    uil_resources_path = os.path.expanduser("~/UILToolResources")
    dryrun_dat_path = os.path.join(source_dir, "dryrun.dat")
    dryrun_java_path = os.path.join(source_dir, "DryRun.java")
    
    default_dryrun_dat = os.path.join(uil_resources_path, "dryrun.dat")
    default_dryrun_java = os.path.join(uil_resources_path, "DryRun.java")

    # Copy dryrun.dat if it doesn't exist
    if not os.path.exists(dryrun_dat_path) and os.path.exists(default_dryrun_dat):
        shutil.copy(default_dryrun_dat, dryrun_dat_path)
        print("Copied default dryrun.dat.")

    # Always copy DryRun.java
    if os.path.exists(default_dryrun_java):
        shutil.copy(default_dryrun_java, dryrun_java_path)
        print("Copied default DryRun.java.")

def convert_dat_to_java(source_dir, dryrun=False):
    """Convert .dat files to .java files."""
    ensure_dryrun_files(source_dir)

    # List all .dat files
    dat_files = [f for f in os.listdir(source_dir) if f.endswith('.dat')]

    if not dat_files:
        # If no .dat files exist, prompt the user for the first program
        first_program = prompt_for_first_program()
        java_filename = first_program + '.java'
        java_path = os.path.join(source_dir, java_filename)

        with open(java_path, 'w', encoding='utf-8') as java_file:
            java_file.write(f"public class {first_program} {{\n")
            java_file.write("    public static void main(String[] args) {\n")
            java_file.write("        // First program logic here\n")
            java_file.write("    }\n")
            java_file.write("}\n")

        print(f"Created {java_filename} as the first program.")

    for dat_file in dat_files:
        class_name = dat_file[:-4].capitalize()  # Capitalize first letter
        java_filename = class_name + '.java'
        java_path = os.path.join(source_dir, java_filename)

        # Read contents of .dat file
        with open(os.path.join(source_dir, dat_file), 'r', encoding='utf-8') as dat_file_content:
            content = dat_file_content.read()

        # Write Java class
        with open(java_path, 'w', encoding='utf-8') as java_file:
            java_file.write(f"import java.util.*;\n")
            java_file.write(f"import java.io.*;\n\n")
            java_file.write(f"public class {class_name} {{\n")
            java_file.write(f"    public static void main(String[] args) throws FileNotFoundException {{\n")
            java_file.write(f"        Scanner scanner = new Scanner(new File(\"{dat_file}\"));\n")
            java_file.write(f"        // Add logic to process file contents\n")
            java_file.write(f"    }}\n")
            java_file.write(f"}}\n")

        print(f"Generated {java_filename} from {dat_file}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Convert .dat files to .java files with capitalized class names.")
    parser.add_argument("source_dir", help="Directory containing .dat files")
    parser.add_argument("--dryrun", action="store_true", help="Ensure DryRun files exist while processing all .dat files")
    args = parser.parse_args()

    convert_dat_to_java(args.source_dir, dryrun=args.dryrun)

