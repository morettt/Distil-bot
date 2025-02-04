import json
from openai import OpenAI

def merge_content():

    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    client = OpenAI(api_key=config['api_key'], base_url=config['api_base'])
    
    with open(config['ask_dir'], 'r', encoding='utf-8') as f:
        for line in f:
            if '问：' in line:
                ask_content = line.split('问：')[1]
                response = client.chat.completions.create(
                        model='gpt-3.5-turbo',
                        messages=[
                            {'role': 'system', 'content': config['system_prompt']},
                            {'role': 'user', 'content': ask_content}
                        ]
                    )
                ai_response = response.choices[0].message.content
                no_line_response = ai_response.replace('\n', '')
                print(no_line_response)

                with open(config['output_file'], 'a', encoding='utf-8') as out_f:
                    out_f.write(f'问：{ask_content}')
                    out_f.write(f'答：{no_line_response}\n\n')


if __name__ == '__main__':
    merge_content()
