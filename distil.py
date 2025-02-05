import json
from openai import OpenAI
import concurrent.futures

with open('config.json','r',encoding='utf-8') as f:
    config = json.load(f)

client = OpenAI(api_key=config['api_key'],base_url=config['api_base'])


def manage_line(line):
    if '问：' in line:
        ask_content=line.split('问：')[1]

        response = client.chat.completions.create(
            model=config['model'],
            messages=[
                {'role':'system','content':config['system_prompt']},
                {'role':'user','content':ask_content}
            ]
        )

        ai_response = response.choices[0].message.content
        print(ai_response)

        with open(config['output_file'],'a',encoding='utf-8') as f:
            f.write(f'问：{ask_content}')
            f.write(f'答：{ai_response}\n\n')

def main():
    with open(config['ask_dir'],'r',encoding='utf-8') as f:
        lines = f.readlines()

    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as chuli:
        chuli.map(manage_line,lines)

if __name__ == '__main__':
    main()
