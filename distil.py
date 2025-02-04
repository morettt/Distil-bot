from openai import OpenAI

API_key = '你的密钥'
API_base = ''
ask_dir = r''
output_qandA = r''

def merge_content():
    client = OpenAI(api_key=API_key,base_url=API_base)
    with open(ask_dir,'r',encoding='utf-8') as f:
        for line in f:
            if '问：' in line:
                ask_content = line.split('问：')[1]

                response = client.chat.completions.create(
                    model='选择模型',
                    messages=[
                        {'role':'system','content':'给AI的性格设定'},
                        {'role':'user','content':ask_content}
                    ]
                )
                ai_response = response.choices[0].message.content
                no_line_response = ai_response.replace('\n','')
                print(no_line_response)

                with open(output_qandA,'a',encoding='utf-8') as f:
                    f.write(f'问：{ask_content}')
                    f.write(f'答：{no_line_response}\n\n')

if __name__ == '__main__':
    merge_content()