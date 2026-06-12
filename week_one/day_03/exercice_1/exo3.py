import json

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        db_config = json.load(file)
        return db_config

file_json_path = 'data/json/config.json'
config = load_json(file_json_path)

db_host = config['database']['host']
db_port = config['database']['port']
db_name = config['database']['name']

username = config['database']['credentials']['username']
print(f"Username: {username}")

passing_score = config['analysis']['thresholds']['passing']
honors_score = config['analysis']['thresholds']['honors']
print(f"Thresholds: Passing={passing_score}, Honors={honors_score}")

output_format = config['analysis']['output']['format']
output_dir = config['analysis']['output']['directory']
print(f"Output: {output_format} -> {output_dir}")

log_level = config['logging']['level']
log_file = config['logging']['file']
print(f"Logging: {log_level} -> {log_file}")

print(f"Database : {db_host}:{db_port}/{db_name}")
