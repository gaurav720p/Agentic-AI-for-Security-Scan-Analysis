import subprocess


def run_nmap(target):
    """
    Run an Nmap service version scan.
    Returns the scan output.
    """

    try:

        result = subprocess.run(
            [
                "nmap",
                "-sV",
                target
            ],
            capture_output=True,
            text=True,
            timeout=120
        )

        return result.stdout

    except subprocess.TimeoutExpired:
        return "Nmap Scan Timed Out."

    except Exception as e:
        return f"Error : {str(e)}"