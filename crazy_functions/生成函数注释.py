<<<<<<< HEAD
from predict import predict_no_ui
from toolbox import CatchException, report_execption, write_results_to_file, predict_no_ui_but_counting_down
fast_debug = False


def 生成函数注释(file_manifest, project_folder, top_p, temperature, chatbot, history, systemPromptTxt):
    import time, glob, os
    print('begin analysis on:', file_manifest)
    for index, fp in enumerate(file_manifest):
        with open(fp, 'r', encoding='utf-8') as f:
=======
from toolbox import update_ui
from toolbox import CatchException, report_execption, write_results_to_file
from .crazy_utils import request_gpt_model_in_new_thread_with_ui_alive
fast_debug = False

def 生成函数注释(file_manifest, project_folder, llm_kwargs, plugin_kwargs, chatbot, history, system_prompt):
    import time, os
    print('begin analysis on:', file_manifest)
    for index, fp in enumerate(file_manifest):
        with open(fp, 'r', encoding='utf-8', errors='replace') as f:
>>>>>>> faffc59f517fc0906b43346324521b016a9affd4
            file_content = f.read()

        i_say = f'请对下面的程序文件做一个概述，并对文件中的所有函数生成注释，使用markdown表格输出结果，文件名是{os.path.relpath(fp, project_folder)}，文件内容是 ```{file_content}```'
        i_say_show_user = f'[{index}/{len(file_manifest)}] 请对下面的程序文件做一个概述，并对文件中的所有函数生成注释: {os.path.abspath(fp)}'
        chatbot.append((i_say_show_user, "[Local Message] waiting gpt response."))
<<<<<<< HEAD
        print('[1] yield chatbot, history')
        yield chatbot, history, '正常'
=======
        yield from update_ui(chatbot=chatbot, history=history) # 刷新界面
>>>>>>> faffc59f517fc0906b43346324521b016a9affd4

        if not fast_debug: 
            msg = '正常'
            # ** gpt request **
<<<<<<< HEAD
            gpt_say = yield from predict_no_ui_but_counting_down(i_say, i_say_show_user, chatbot, top_p, temperature, history=[])   # 带超时倒计时

            print('[2] end gpt req')
            chatbot[-1] = (i_say_show_user, gpt_say)
            history.append(i_say_show_user); history.append(gpt_say)
            print('[3] yield chatbot, history')
            yield chatbot, history, msg
            print('[4] next')
=======
            gpt_say = yield from request_gpt_model_in_new_thread_with_ui_alive(
                i_say, i_say_show_user, llm_kwargs, chatbot, history=[], sys_prompt=system_prompt)   # 带超时倒计时

            chatbot[-1] = (i_say_show_user, gpt_say)
            history.append(i_say_show_user); history.append(gpt_say)
            yield from update_ui(chatbot=chatbot, history=history, msg=msg) # 刷新界面
>>>>>>> faffc59f517fc0906b43346324521b016a9affd4
            if not fast_debug: time.sleep(2)

    if not fast_debug: 
        res = write_results_to_file(history)
        chatbot.append(("完成了吗？", res))
<<<<<<< HEAD
        yield chatbot, history, msg
=======
        yield from update_ui(chatbot=chatbot, history=history, msg=msg) # 刷新界面
>>>>>>> faffc59f517fc0906b43346324521b016a9affd4



@CatchException
<<<<<<< HEAD
def 批量生成函数注释(txt, top_p, temperature, chatbot, history, systemPromptTxt, WEB_PORT):
=======
def 批量生成函数注释(txt, llm_kwargs, plugin_kwargs, chatbot, history, system_prompt, web_port):
>>>>>>> faffc59f517fc0906b43346324521b016a9affd4
    history = []    # 清空历史，以免输入溢出
    import glob, os
    if os.path.exists(txt):
        project_folder = txt
    else:
        if txt == "": txt = '空空如也的输入栏'
        report_execption(chatbot, history, a = f"解析项目: {txt}", b = f"找不到本地项目或无权访问: {txt}")
<<<<<<< HEAD
        yield chatbot, history, '正常'
=======
        yield from update_ui(chatbot=chatbot, history=history) # 刷新界面
>>>>>>> faffc59f517fc0906b43346324521b016a9affd4
        return
    file_manifest = [f for f in glob.glob(f'{project_folder}/**/*.py', recursive=True)] + \
                    [f for f in glob.glob(f'{project_folder}/**/*.cpp', recursive=True)]

    if len(file_manifest) == 0:
        report_execption(chatbot, history, a = f"解析项目: {txt}", b = f"找不到任何.tex文件: {txt}")
<<<<<<< HEAD
        yield chatbot, history, '正常'
        return
    yield from 生成函数注释(file_manifest, project_folder, top_p, temperature, chatbot, history, systemPromptTxt)
=======
        yield from update_ui(chatbot=chatbot, history=history) # 刷新界面
        return
    yield from 生成函数注释(file_manifest, project_folder, llm_kwargs, plugin_kwargs, chatbot, history, system_prompt)
>>>>>>> faffc59f517fc0906b43346324521b016a9affd4
