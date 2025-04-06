import json
import time
import random
from datetime import datetime

TEMPLATE_FILE = "template_log.json"
LOG_FILE = "logs/app.log"

def generate_random_id():
    return str(random.randint(10**18, 10**19 - 1))

def main():
    print("Log generator iniciado...", flush=True)  # feedback imediato

    while True:
        with open(TEMPLATE_FILE, "r") as f:
            raw = f.read()
            payload = json.loads(raw)

        payload["dd.trace_id"] = generate_random_id()
        payload["dd.span_id"] = generate_random_id()
        payload["@timestamp"] = datetime.utcnow().isoformat() + "Z"

        log_line = json.dumps(payload)

        # Grava no arquivo com flush
        with open(LOG_FILE, "a") as log:
            log.write(log_line + "\n")
            log.flush()

        # Mostra no stdout com flush
        print(log_line, flush=True)

        time.sleep(5)

if __name__ == "__main__":
    main()
