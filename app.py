from flask import Flask, render_template, request
import subprocess
import sys
import os

app = Flask(__name__)

def run_tool(command):
    """Rulează o comandă în terminal și returnează output-ul ca string."""
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=120,
            shell=False
        )
        output = result.stdout + result.stderr
        return output if output.strip() else "Nicio informație găsită."
    except subprocess.TimeoutExpired:
        return "[✗] Timeout: Operațiunea a durat prea mult."
    except FileNotFoundError:
        return f"[✗] Eroare: Comanda '{command[0]}' nu a fost găsită."
    except Exception as e:
        return f"[✗] Eroare: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    rezultate_carduri = []
    target = None
    search_type = "phone"
    
    if request.method == 'POST':
        target = request.form.get('target')
        search_type = request.form.get('search_type')
        
        if target:
            target = target.strip()
            
            if search_type == "phone":
                command = [sys.executable, "-m", "phonsint", "-p", target, "--all", "-v"]
                output = run_tool(command)
                rezultate_carduri.append({
                    "platform": "Phone OSINT (phonsint)",
                    "url": output,
                    "is_code": True
                })
                
            elif search_type == "email":
                # Calea către holehe.exe din folderul Scripts
                scripts_dir = os.path.join(os.path.dirname(sys.executable), "Scripts")
                holehe_executable = os.path.join(scripts_dir, "holehe.exe")
                
                command = [holehe_executable, target, "--only-used"]
                output = run_tool(command)
                
                limitari = (
                    "\n\n[!] Note: Holehe can sometimes extract partially masked phone numbers "
                    "(e.g., 0*******78) if the platform exposes them during password recovery. "
                    "It cannot extract physical addresses."
                )
                
                rezultate_carduri.append({
                    "platform": "Email OSINT (holehe)",
                    "url": output + limitari,
                    "is_code": True
                })
    
    return render_template('index.html', rezultate=rezultate_carduri, target=target, search_type=search_type)

if __name__ == '__main__':
    app.run(debug=True)