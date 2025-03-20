import os
import sys
import json

def parse_xcstrings(file_path):
    """Parse the xcstrings JSON file and return a dictionary with language codes as keys and privacy policy content as values."""
    privacy_policies = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(f"Loaded JSON data from {file_path}")
            localizations = data.get("strings", {}).get("privacy policy", {}).get("localizations", {})
            for lang_code, content in localizations.items():
                policy_content = content.get("stringUnit", {}).get("value", "")
                if policy_content:
                    privacy_policies[lang_code] = policy_content
                    print(f"Found privacy policy for language: {lang_code}: {policy_content[:50]}...")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file: {file_path}")
    except Exception as e:
        print(f"Error reading file: {e}")
    return privacy_policies

def write_privacy_policy_files(privacy_policies):
    """Write the privacy policy content to corresponding markdown files in the current language folders."""
    for lang_code, content in privacy_policies.items():
        file_path = os.path.join('.', lang_code, 'privacy-policy.md')
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Written privacy policy for {lang_code} to {file_path} with content length: {len(content)}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python update_privacy_policy.py <path_to_Localizable.strings>")
        sys.exit(1)
    
    # xcstrings_file_path = sys.argv[1]
    xcstrings_file_path = '/Users/deanxu/SingularitySignal/AIAssistant/macos/AIAssistant/AIAssistant/AppStoreConnect.xcstrings'
    
    print(f"Parsing file: {xcstrings_file_path}")
    privacy_policies = parse_xcstrings(xcstrings_file_path)
    if not privacy_policies:
        print("No privacy policies found.")
        sys.exit(1)
    
    print(f"Writing privacy policies to current language folders")
    write_privacy_policy_files(privacy_policies)
    print("Done.")

if __name__ == '__main__':
    main()
