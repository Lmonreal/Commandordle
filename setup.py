import subprocess
import sys
import os
from pathlib import Path

def setup_virtual_environment():
    venv_path = Path("venv")
    
    # Create virtual environment if it doesn't exist
    if not venv_path.exists():
        print("Creating virtual environment...")
        subprocess.check_call([sys.executable, "-m", "venv", "venv"])
    
    # Activate virtual environment
    if os.name == "nt":  # Windows
        activate_script = venv_path / "Scripts" / "activate.bat"
        if not activate_script.exists():
            print("Error: Virtual environment activation script not found")
            return False
        
        # Install required packages
        pip_path = venv_path / "Scripts" / "pip.exe"
        subprocess.check_call([str(pip_path), "install", "colorama"])
        
        print("Virtual environment setup complete!")
        print("To activate, run: .\\venv\\Scripts\\activate")
        return True

if __name__ == "__main__":
    setup_virtual_environment()