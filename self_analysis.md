# chatgpt-academic项目自译解报告
（Author补充：以下分析均由本项目调用ChatGPT一键生成，如果有不准确的地方，全怪GPT😄）

<<<<<<< HEAD
## [0/18] 程序摘要: functional_crazy.py

这是一个功能扩展的程序，文件名为 `functional_crazy.py`。代码的主要功能是通过提供一系列函数插件，增强程序的功能，让用户可以通过界面中的按钮，快速调用对应的函数插件实现相应的操作。代码中使用了 `HotReload` 函数插件，可以在不重启程序的情况下更新函数插件的代码，让其生效。同时，通过 `UserVisibleLevel` 变量的设置，可以控制哪些插件会在UI界面显示出来。函数插件列表包括了以下功能：解析项目本身、解析一个Python项目、解析一个C++项目头文件、解析一个C++项目、读取文章并生成摘要、批量生成函数注释、全项目切换成英文、批量总结PDF文档、批量总结PDF文档pdfminer、批量总结Word文档、高阶功能模板函数、以及其他未经充分测试的函数插件。

## [1/18] 程序摘要: main.py

该程序是一个基于Gradio构建的对话生成模型的Web界面示例，包含了以下主要功能：

1.加载模型并对用户输入进行响应；
2.通过调用外部函数库来获取用户的输入，并在模型生成的过程中进行处理；
3.支持用户上传本地文件，供外部函数库调用；
4.支持停止当前的生成过程；
5.保存用户的历史记录，并将其记录在本地日志文件中，以供后续分析和使用。

该程序需要依赖于一些外部库和软件包，如Gradio、torch等。用户需要确保这些依赖项已经安装，并且在运行该程序前对config_private.py配置文件进行相应的修改。

## [2/18] 程序摘要: functional.py

该文件定义了一个名为“functional”的函数，函数的作用是返回一个包含多个字典（键值对）的字典，每个键值对表示一种功能。该字典的键值由功能名称和对应的数据组成。其中的每个字典都包含4个键值对，分别为“Prefix”、“Suffix”、“Color”和“PreProcess”，分别表示前缀、后缀、按钮颜色和预处理函数。如果某些键值对没有给出，那么程序中默认相应的值，如按钮颜色默认为“secondary”等。每个功能描述了不同的学术润色/翻译/其他服务，如“英语学术润色”、“中文学术润色”、“查找语法错误”等。函数还引用了一个名为“clear_line_break”的函数，用于预处理修改前的文本。

## [3/18] 程序摘要: show_math.py

该程序文件名为show_math.py，主要用途是将Markdown和LaTeX混合格式转换成带有MathML的HTML格式。该程序通过递归地处理LaTeX和Markdown混合段落逐一转换成HTML/MathML标记出来，并在LaTeX公式创建中进行错误处理。在程序文件中定义了3个变量，分别是incomplete，convError和convert，其中convert函数是用来执行转换的主要函数。程序使用正则表达式进行LaTeX格式和Markdown段落的分割，从而实现转换。如果在Latex转换过程中发生错误，程序将输出相应的错误信息。

## [4/18] 程序摘要: predict.py

本程序文件的文件名为"./predict.py"，主要包含三个函数：

1. predict：正常对话时使用，具备完备的交互功能，不可多线程；
2. predict_no_ui：高级实验性功能模块调用，不会实时显示在界面上，参数简单，可以多线程并行，方便实现复杂的功能逻辑；
3. predict_no_ui_long_connection：在实验过程中发现调用predict_no_ui处理长文档时，和openai的连接容易断掉，这个函数用stream的方式解决这个问题，同样支持多线程。

其中，predict函数用于基础的对话功能，发送至chatGPT，流式获取输出，根据点击的哪个按钮，进行对话预处理等额外操作；predict_no_ui函数用于payload比较大的情况，或者用于实现多线、带嵌套的复杂功能；predict_no_ui_long_connection实现调用predict_no_ui处理长文档时，避免连接断掉的情况，支持多线程。

## [5/18] 程序摘要: check_proxy.py

该程序文件名为check_proxy.py，主要功能是检查代理服务器的可用性并返回代理服务器的地理位置信息或错误提示。具体实现方式如下：

首先使用requests模块向指定网站（https://ipapi.co/json/）发送GET请求，请求结果以JSON格式返回。如果代理服务器参数(proxies)是有效的且没有指明'https'代理，则用默认字典值'无'替代。

然后，程序会解析返回的JSON数据，并根据数据中是否包含国家名字字段来判断代理服务器的地理位置。如果有国家名字字段，则将其打印出来并返回代理服务器的相关信息。如果没有国家名字字段，但有错误信息字段，则返回其他错误提示信息。

在程序执行前，程序会先设置环境变量no_proxy，并使用toolbox模块中的get_conf函数从配置文件中读取代理参数。

最后，检测程序会输出检查结果并返回对应的结果字符串。

## [6/18] 程序摘要: config_private.py

本程序文件名为`config_private.py`，其功能为配置私有信息以便在主程序中使用。主要功能包括：

- 配置OpenAI API的密钥和API URL
- 配置是否使用代理，如果使用代理配置代理地址和端口
- 配置发送请求的超时时间和失败重试次数的限制
- 配置并行使用线程数和用户名密码
- 提供检查功能以确保API密钥已经正确设置

其中，需要特别注意的是：最后一个检查功能要求在运行之前必须将API密钥正确设置，否则程序会直接退出。

## [7/18] 程序摘要: config.py

该程序文件是一个配置文件，用于配置OpenAI的API参数和优化体验的相关参数，具体包括以下几个步骤：

1.设置OpenAI的API密钥。

2.选择是否使用代理，如果使用则需要设置代理地址和端口等参数。

3.设置请求OpenAI后的超时时间、网页的端口、重试次数、选择的OpenAI模型、API的网址等。

4.设置并行使用的线程数和用户名密码。

该程序文件的作用为在使用OpenAI API时进行相关参数的配置，以保证请求的正确性和速度，并且优化使用体验。

## [8/18] 程序摘要: theme.py

该程序是一个自定义Gradio主题的Python模块。主题文件名为"./theme.py"。程序引入了Gradio模块，并定义了一个名为"adjust_theme()"的函数。该函数根据输入值调整Gradio的默认主题，返回一个包含所需自定义属性的主题对象。主题属性包括颜色、字体、过渡、阴影、按钮边框和渐变等。主题颜色列表包括石板色、灰色、锌色、中性色、石头色、红色、橙色、琥珀色、黄色、酸橙色、绿色、祖母绿、青蓝色、青色、天蓝色、蓝色、靛蓝色、紫罗兰色、紫色、洋红色、粉红色和玫瑰色。如果Gradio版本较旧，则不能自定义字体和颜色。

## [9/18] 程序摘要: toolbox.py

该程序文件包含了一系列函数，用于实现聊天程序所需的各种功能，如预测对话、将对话记录写入文件、将普通文本转换为Markdown格式文本、装饰器函数CatchException和HotReload等。其中一些函数用到了第三方库，如Python-Markdown、mdtex2html、zipfile、tarfile、rarfile和py7zr。除此之外，还有一些辅助函数，如get_conf、clear_line_break和extract_archive等。主要功能包括：

1. 导入markdown、mdtex2html、threading、functools等模块。
2. 定义函数predict_no_ui_but_counting_down，用于生成对话。
3. 定义函数write_results_to_file，用于将对话记录生成Markdown文件。
4. 定义函数regular_txt_to_markdown，将普通文本转换为Markdown格式的文本。
5. 定义装饰器函数CatchException，用于捕获函数执行异常并返回生成器。
6. 定义函数report_execption，用于向chatbot中添加错误信息。
7. 定义函数text_divide_paragraph，用于将文本按照段落分隔符分割开，生成带有段落标签的HTML代码。
8. 定义函数markdown_convertion，用于将Markdown格式的文本转换为HTML格式。
9. 定义函数format_io，用于将输入和输出解析为HTML格式。
10. 定义函数find_free_port，用于返回当前系统中可用的未使用端口。
11. 定义函数extract_archive，用于解压归档文件。
12. 定义函数find_recent_files，用于查找最近创建的文件。
13. 定义函数on_file_uploaded，用于处理上传文件的操作。
14. 定义函数on_report_generated，用于处理生成报告文件的操作。


## [10/18] 程序摘要: crazy_functions/生成函数注释.py

该程序文件是一个Python脚本，文件名为“生成函数注释.py”，位于“./crazy_functions/”目录下。该程序实现了一个批量生成函数注释的功能，可以对指定文件夹下的所有Python和C++源代码文件中的所有函数进行注释，使用Markdown表格输出注释结果。

该程序引用了predict.py和toolbox.py两个模块，其中predict.py实现了一个基于GPT模型的文本生成功能，用于生成函数注释，而toolbox.py实现了一些工具函数，包括异常处理函数、文本写入函数等。另外，该程序还定义了两个函数，一个是“生成函数注释”函数，用于处理单个文件的注释生成；另一个是“批量生成函数注释”函数，用于批量处理多个文件的注释生成。

## [11/18] 程序摘要: crazy_functions/读文章写摘要.py

这个程序文件是一个名为“读文章写摘要”的函数。该函数的输入包括文章的文本内容、top_p（生成文本时选择最可能的词语的概率阈值）、temperature（控制生成文本的随机性的因子）、对话历史等参数，以及一个聊天机器人和一个系统提示的文本。该函数的主要工作是解析一组.tex文件，然后生成一段学术性语言的中文和英文摘要。在解析过程中，该函数使用一个名为“toolbox”的模块中的辅助函数和一个名为“predict”的模块中的函数来执行GPT-2模型的推理工作，然后将结果返回给聊天机器人。另外，该程序还包括一个名为“fast_debug”的bool型变量，用于调试和测试。

## [12/18] 程序摘要: crazy_functions/代码重写为全英文_多线程.py

该程序文件实现了一个多线程操作，用于将指定目录下的所有 Python 文件中的中文转化为英文，并将转化后的文件存入另一个目录中。具体实现过程如下：

1. 集合目标文件路径并清空历史记录。
2. 循环目标文件，对每个文件启动一个线程进行任务操作。
3. 各个线程同时开始执行任务函数，并在任务完成后将转化后的文件写入指定目录，最终生成一份任务执行报告。

## [13/18] 程序摘要: crazy_functions/高级功能函数模板.py

该程序文件名为高级功能函数模板.py，它包含了一个名为“高阶功能模板函数”的函数，这个函数可以作为开发新功能函数的模板。该函数引用了predict.py和toolbox.py文件中的函数。在该函数内部，它首先清空了历史记录，然后对于今天和今天以后的四天，它问用户历史中哪些事件发生在这些日期，并列举两条事件并发送相关的图片。在向用户询问问题时，使用了GPT进行响应。由于请求GPT需要一定的时间，所以函数会在重新显示状态之前等待一段时间。在每次与用户的互动中，使用yield关键字生成器函数来输出聊天机器人的当前状态，包括聊天消息、历史记录和状态（'正常'）。最后，程序调用write_results_to_file函数将聊天的结果写入文件，以供后续的评估和分析。

## [14/18] 程序摘要: crazy_functions/总结word文档.py

该程序文件名为总结word文档.py，主要功能是批量总结Word文档。具体实现过程是解析docx格式和doc格式文件，生成文件内容，然后使用自然语言处理工具对文章内容做中英文概述，最后给出建议。该程序需要依赖python-docx和pywin32，如果没有安装，会给出安装建议。

## [15/18] 程序摘要: crazy_functions/批量总结PDF文档pdfminer.py

该程序文件名为pdfminer.py，位于./crazy_functions/目录下。程序实现了批量读取PDF文件，并使用pdfminer解析PDF文件内容。此外，程序还根据解析得到的文本内容，调用机器学习模型生成对每篇文章的概述，最终生成全文摘要。程序中还对模块依赖进行了导入检查，若缺少依赖，则会提供安装建议。

## [16/18] 程序摘要: crazy_functions/解析项目源代码.py

这个程序文件中包含了几个函数，分别是：

1. `解析源代码(file_manifest, project_folder, top_p, temperature, chatbot, history, systemPromptTxt)`：通过输入文件路径列表对程序文件进行逐文件分析，根据分析结果做出整体功能和构架的概括，并生成包括每个文件功能的markdown表格。
2. `解析项目本身(txt, top_p, temperature, chatbot, history, systemPromptTxt, WEB_PORT)`：对当前文件夹下的所有Python文件及其子文件夹进行逐文件分析，并生成markdown表格。
3. `解析一个Python项目(txt, top_p, temperature, chatbot, history, systemPromptTxt, WEB_PORT)`：对指定路径下的所有Python文件及其子文件夹进行逐文件分析，并生成markdown表格。
4. `解析一个C项目的头文件(txt, top_p, temperature, chatbot, history, systemPromptTxt, WEB_PORT)`：对指定路径下的所有头文件进行逐文件分析，并生成markdown表格。
5. `解析一个C项目(txt, top_p, temperature, chatbot, history, systemPromptTxt, WEB_PORT)`：对指定路径下的所有.h、.cpp、.c文件及其子文件夹进行逐文件分析，并生成markdown表格。

程序中还包含了一些辅助函数和变量，如CatchException装饰器函数，report_execption函数、write_results_to_file函数等。在执行过程中还会调用其他模块中的函数，如toolbox模块的函数和predict模块的函数。

## [17/18] 程序摘要: crazy_functions/批量总结PDF文档.py

这个程序文件是一个名为“批量总结PDF文档”的函数插件。它导入了predict和toolbox模块，并定义了一些函数，包括is_paragraph_break，normalize_text和clean_text。这些函数是对输入文本进行预处理和清洗的功能函数。主要的功能函数是解析PDF，它打开每个PDF文件并将其内容存储在file_content变量中，然后传递给聊天机器人，以产生一句话的概括。在解析PDF文件之后，该函数连接了所有文件的摘要，以产生一段学术语言和英文摘要。最后，函数批量处理目标文件夹中的所有PDF文件，并输出结果。

## 根据以上你自己的分析，对程序的整体功能和构架做出概括。然后用一张markdown表格整理每个文件的功能。

该程序是一个聊天机器人，使用了OpenAI的GPT语言模型以及一些特殊的辅助功能去处理各种学术写作和科研润色任务。整个程序由一些函数组成，每个函数都代表了不同的学术润色/翻译/其他服务。

下面是程序中每个文件的功能列表：

| 文件名 | 功能 |
|--------|--------|
| functional_crazy.py | 实现高级功能函数模板和其他一些辅助功能函数 |
| main.py | 程序的主要入口，负责程序的启动和UI的展示 |
| functional.py | 定义各种功能按钮的颜色和响应函数 |
| show_math.py | 解析LaTeX文本，将其转换为Markdown格式 |
| predict.py | 基础的对话功能，用于与chatGPT进行交互 |
| check_proxy.py | 检查代理设置的正确性 |
| config_private.py | 配置程序的API密钥和其他私有信息 |
| config.py | 配置OpenAI的API参数和程序的其他属性 |
| theme.py | 设置程序主题样式 |
| toolbox.py | 存放一些辅助函数供程序使用 |
| crazy_functions/生成函数注释.py | 生成Python文件中所有函数的注释 |
| crazy_functions/读文章写摘要.py | 解析文章文本，生成中英文摘要 |
| crazy_functions/代码重写为全英文_多线程.py | 将中文代码内容转化为英文 |
| crazy_functions/高级功能函数模板.py | 实现高级功能函数模板 |
| crazy_functions/总结word文档.py | 解析Word文件，生成文章内容的概要 |
| crazy_functions/批量总结PDF文档pdfminer.py | 解析PDF文件，生成文章内容的概要（使用pdfminer库） |
| crazy_functions/批量总结PDF文档.py | 解析PDF文件，生成文章内容的概要（使用PyMuPDF库） |
| crazy_functions/解析项目源代码.py | 解析C/C++源代码，生成markdown表格 |
| crazy_functions/批量总结PDF文档.py | 对PDF文件进行批量摘要生成 |

总的来说，该程序提供了一系列的学术润色和翻译的工具，支持对各种类型的文件进行分析和处理。同时也提供了对话式用户界面，便于用户使用和交互。
=======
## 对程序的整体功能和构架做出概括。然后用一张markdown表格整理每个文件的功能（包括'check_proxy.py', 'config.py'等）。

整体概括：

该程序是一个基于自然语言处理和机器学习的科学论文辅助工具，主要功能包括聊天机器人、批量总结PDF文档、批量翻译PDF文档、生成函数注释、解析项目源代码等。程序基于 Gradio 构建 Web 服务，并集成了代理和自动更新功能，提高了用户的使用体验。

文件功能表格：

| 文件名称                                                     | 功能                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| .\check_proxy.py                                             | 检查代理设置功能。                                           |
| .\config.py                                                  | 配置文件，存储程序的基本设置。                               |
| .\config_private.py                                          | 存储代理网络地址的文件。                                     |
| .\core_functional.py                                         | 主要的程序逻辑，包括聊天机器人和文件处理。                  |
| .\cradle.py                                                  | 程序入口，初始化程序和启动 Web 服务。                        |
| .\crazy_functional.py                                        | 辅助程序功能，包括PDF文档处理、代码处理、函数注释生成等。  |
| .\main.py                                                    | 包含聊天机器人的具体实现。                                   |
| .\show_math.py                                               | 处理 LaTeX 公式的函数。                                      |
| .\theme.py                                                   | 存储 Gradio Web 服务的 CSS 样式文件。                        |
| .\toolbox.py                                                 | 提供了一系列工具函数，包括文件读写、网页抓取、解析函数参数、生成 HTML 等。 |
| ./crazy_functions/crazy_utils.py                             | 提供各种工具函数，如解析字符串、清洗文本、清理目录结构等。 |
| ./crazy_functions/\_\_init\_\_.py                             | crazy_functions 模块的入口文件。                            |
| ./crazy_functions/下载arxiv论文翻译摘要.py                 | 对 arxiv.org 上的 PDF 论文进行下载和翻译。                   |
| ./crazy_functions/代码重写为全英文_多线程.py                | 将代码文件中的中文注释和字符串替换为英文。                   |
| ./crazy_functions/总结word文档.py                            | 读取 Word 文档并生成摘要。                                    |
| ./crazy_functions/批量总结PDF文档.py                        | 批量读取 PDF 文件并生成摘要。                                 |
| ./crazy_functions/批量总结PDF文档pdfminer.py                | 使用 pdfminer 库进行 PDF 文件处理。                        |
| ./crazy_functions/批量翻译PDF文档_多线程.py                 | 使用多线程技术批量翻译 PDF 文件。                             |
| ./crazy_functions/生成函数注释.py                           | 给 Python 函数自动生成说明文档。                             |
| ./crazy_functions/解析项目源代码.py                         | 解析项目中的源代码，提取注释和函数名等信息。                  |
| ./crazy_functions/读文章写摘要.py                           | 读取多个文本文件并生成对应的摘要。                             |
| ./crazy_functions/高级功能函数模板.py                        | 使用 GPT 模型进行文本处理。                                  |



## [0/22] 程序概述: check_proxy.py

该程序的文件名是check_proxy.py，主要有两个函数：check_proxy和auto_update。

check_proxy函数中会借助requests库向一个IP查询API发送请求，并返回该IP的地理位置信息。同时根据返回的数据来判断代理是否有效。

auto_update函数主要用于检查程序更新，会从Github获取程序最新的版本信息，如果当前版本和最新版本相差较大，则会提示用户进行更新。该函数中也会依赖requests库进行网络请求。

在程序的开头，还添加了一句防止代理网络影响的代码。程序使用了自己编写的toolbox模块中的get_conf函数来获取代理设置。

## [1/22] 程序概述: config.py

该程序文件是一个Python模块，文件名为config.py。该模块包含了一些变量和配置选项，用于配置一个OpenAI的聊天机器人。具体的配置选项如下：

- API_KEY: 密钥，用于连接OpenAI的API。需要填写有效的API密钥。
- USE_PROXY: 是否使用代理。如果需要使用代理，需要将其改为True。
- proxies: 代理的协议、地址和端口。
- CHATBOT_HEIGHT: 聊天机器人对话框的高度。
- LAYOUT: 聊天机器人对话框的布局，默认为左右布局。
- TIMEOUT_SECONDS: 发送请求到OpenAI后，等待多久判定为超时。
- WEB_PORT: 网页的端口，-1代表随机端口。
- MAX_RETRY: 如果OpenAI不响应（网络卡顿、代理失败、KEY失效），重试的次数限制。
- LLM_MODEL: OpenAI模型选择，目前只对某些用户开放的gpt4。
- API_URL: OpenAI的API地址。
- CONCURRENT_COUNT: 使用的线程数。
- AUTHENTICATION: 用户名和密码，如果需要。

## [2/22] 程序概述: config_private.py

该程序文件名为config_private.py，包含了API_KEY的设置和代理的配置。使用了一个名为API_KEY的常量来存储私人的API密钥。此外，还有一个名为USE_PROXY的常量来标记是否需要使用代理。如果需要代理，则使用了一个名为proxies的字典来存储代理网络的地址，其中包括协议类型、地址和端口。

## [3/22] 程序概述: core_functional.py

该程序文件名为`core_functional.py`，主要是定义了一些核心功能函数，包括英语和中文学术润色、查找语法错误、中译英、学术中英互译、英译中、找图片和解释代码等。每个功能都有一个`Prefix`属性和`Suffix`属性，`Prefix`是指在用户输入的任务前面要显示的文本，`Suffix`是指在任务后面要显示的文本。此外，还有一个`Color`属性指示按钮的颜色，以及一个`PreProcess`函数表示对输入进行预处理的函数。

## [4/22] 程序概述: cradle.py

该程序文件名为cradle.py，主要功能是检测当前版本与远程最新版本是否一致，如果不一致则输出新版本信息并提示更新。其流程大致如下：

1. 导入相关模块与自定义工具箱函数get_conf 
2. 读取配置文件中的代理proxies 
3. 使用requests模块请求远程版本信息（url为https://raw.githubusercontent.com/binary-husky/chatgpt_academic/master/version）并加载为json格式 
4. 获取远程版本号、是否显示新功能信息、新功能内容 
5. 读取本地版本文件version并加载为json格式 
6. 获取当前版本号 
7. 比较当前版本与远程版本，如果远程版本号比当前版本号高0.05以上，则输出新版本信息并提示更新 
8. 如果不需要更新，则直接返回

## [5/22] 程序概述: crazy_functional.py

该程序文件名为.\crazy_functional.py，主要定义了一个名为get_crazy_functions()的函数，该函数返回一个字典类型的变量function_plugins，其中包含了一些函数插件。

一些重要的函数插件包括：

- 读文章写摘要：可以自动读取Tex格式的论文，并生成其摘要。

- 批量生成函数注释：可以批量生成Python函数的文档注释。

- 解析项目源代码：可以解析Python、C++、Golang、Java及React项目的源代码。

- 批量总结PDF文档：可以对PDF文档进行批量总结，以提取其中的关键信息。

- 一键下载arxiv论文并翻译摘要：可以自动下载arxiv.org网站上的PDF论文，并翻译生成其摘要。

- 批量翻译PDF文档（多线程）：可以对PDF文档进行批量翻译，并使用多线程方式提高翻译效率。

## [6/22] 程序概述: main.py

本程序为一个基于 Gradio 和 GPT-3 的交互式聊天机器人，文件名为 main.py。其中主要功能包括：

1. 使用 Gradio 建立 Web 界面，实现用户与聊天机器人的交互；
2. 通过 bridge_chatgpt 模块，利用 GPT-3 模型实现聊天机器人的逻辑；
3. 提供一些基础功能和高级函数插件，用户可以通过按钮选择使用；
4. 提供文档格式转变、外观调整以及代理和自动更新等功能。

程序的主要流程为：

1. 导入所需的库和模块，并通过 get_conf 函数获取配置信息；
2. 设置 Gradio 界面的各个组件，包括聊天窗口、输入区、功能区、函数插件区等；
3. 注册各个组件的回调函数，包括用户输入、信号按钮等，实现机器人逻辑的交互；
4. 通过 Gradio 的 queue 函数和 launch 函数启动 Web 服务，并提供聊天机器人的功能。

此外，程序还提供了代理和自动更新功能，可以确保用户的使用体验。

## [7/22] 程序概述: show_math.py

该程序是一个Python脚本，文件名为show_math.py。它转换Markdown和LaTeX混合语法到带MathML的HTML。程序使用latex2mathml模块来实现从LaTeX到MathML的转换，将符号转换为HTML实体以批量处理。程序利用正则表达式和递归函数的方法处理不同形式的LaTeX语法，支持以下四种情况：$$形式、$形式、\[..]形式和\(...\)形式。如果无法转换某个公式，则在该位置插入一条错误消息。最后，程序输出HTML字符串。

## [8/22] 程序概述: theme.py

该程序文件为一个Python脚本，其功能是调整Gradio应用的主题和样式，包括字体、颜色、阴影、背景等等。在程序中，使用了Gradio提供的默认颜色主题，并针对不同元素设置了相应的样式属性，以达到美化显示的效果。此外，程序中还包含了一段高级CSS样式代码，针对表格、列表、聊天气泡、行内代码等元素进行了样式设定。

## [9/22] 程序概述: toolbox.py

此程序文件主要包含了一系列用于聊天机器人开发的实用工具函数和装饰器函数。主要函数包括：

1. ArgsGeneralWrapper：一个装饰器函数，用于重组输入参数，改变输入参数的顺序与结构。

2. get_reduce_token_percent：一个函数，用于计算自然语言处理时会出现的token溢出比例。

3. predict_no_ui_but_counting_down：一个函数，调用聊天接口，并且保留了一定的界面心跳功能，即当对话太长时，会自动采用二分法截断。

4. write_results_to_file：一个函数，将对话记录history生成Markdown格式的文本，并写入文件中。

5. regular_txt_to_markdown：一个函数，将普通文本转换为Markdown格式的文本。

6. CatchException：一个装饰器函数，捕捉函数调度中的异常，并封装到一个生成器中返回，并显示到聊天当中。

7. HotReload：一个装饰器函数，实现函数插件的热更新。

8. report_execption：一个函数，向chatbot中添加错误信息。

9. text_divide_paragraph：一个函数，将文本按照段落分隔符分割开，生成带有段落标签的HTML代码。

10. markdown_convertion：一个函数，将Markdown格式的文本转换为HTML格式。如果包含数学公式，则先将公式转换为HTML格式。

11. close_up_code_segment_during_stream：一个函数，用于在gpt输出代码的中途，即输出了前面的```，但还没输出完后面的```，补上后面的```。

12. format_io：一个函数，将输入和输出解析为HTML格式。将输出部分的Markdown和数学公式转换为HTML格式。

13. find_free_port：一个函数，返回当前系统中可用的未使用端口。

14. extract_archive：一个函数，解压缩文件。

15. find_recent_files：一个函数，查找目录下一分钟内创建的文件。

16. on_file_uploaded：一个函数，响应用户上传的文件。

## [10/22] 程序概述: crazy_functions\crazy_utils.py

这是一个名为"crazy_utils.py"的Python程序文件，包含了两个函数：
1. `breakdown_txt_to_satisfy_token_limit()`：接受文本字符串、计算文本单词数量的函数和单词数量限制作为输入参数，将长文本拆分成合适的长度，以满足单词数量限制。这个函数使用一个递归方法去拆分长文本。
2. `breakdown_txt_to_satisfy_token_limit_for_pdf()`：类似于`breakdown_txt_to_satisfy_token_limit()`，但是它使用一个不同的递归方法来拆分长文本，以满足PDF文档中的需求。当出现无法继续拆分的情况时，该函数将使用一个中文句号标记插入文本来截断长文本。如果还是无法拆分，则会引发运行时异常。

## [11/22] 程序概述: crazy_functions\__init__.py

这个程序文件是一个 Python 的包，包名为 "crazy_functions"，并且是其中的一个子模块 "__init__.py"。该包中可能包含多个函数或类，用于实现各种疯狂的功能。由于该文件的具体代码没有给出，因此无法进一步确定该包中的功能。通常情况下，一个包应该具有 __init__.py、__main__.py 和其它相关的模块文件，用于实现该包的各种功能。

## [12/22] 程序概述: crazy_functions\下载arxiv论文翻译摘要.py

这个程序实现的功能是下载arxiv论文并翻译摘要，文件名为`下载arxiv论文翻译摘要.py`。这个程序引入了`requests`、`unicodedata`、`os`、`re`等Python标准库，以及`pdfminer`、`bs4`等第三方库。其中`download_arxiv_`函数主要实现了从arxiv网站下载论文的功能，包括解析链接、获取论文信息、下载论文和生成文件名等，`get_name`函数则是为了从arxiv网站中获取论文信息创建的辅助函数。`下载arxiv论文并翻译摘要`函数则是实现了从下载好的PDF文件中提取摘要，然后使用预先训练的GPT模型翻译为中文的功能。同时，该函数还会将历史记录写入文件中。函数还会通过`CatchException`函数来捕获程序中出现的异常信息。

## [13/22] 程序概述: crazy_functions\代码重写为全英文_多线程.py

该程序文件为一个Python多线程程序，文件名为"crazy_functions\代码重写为全英文_多线程.py"。该程序使用了多线程技术，将一个大任务拆成多个小任务，同时执行，提高运行效率。

程序的主要功能是将Python文件中的中文转换为英文，同时将转换后的代码输出。程序先清空历史记录，然后尝试导入openai和transformers等依赖库。程序接下来会读取当前路径下的.py文件和crazy_functions文件夹中的.py文件，并将其整合成一个文件清单。随后程序会使用GPT2模型进行中英文的翻译，并将结果保存在本地路径下的"gpt_log/generated_english_version"文件夹中。程序最终会生成一个任务执行报告。

需要注意的是，该程序依赖于"request_llm"和"toolbox"库以及本地的"crazy_utils"模块。

## [14/22] 程序概述: crazy_functions\总结word文档.py

该程序文件是一个 Python 脚本文件，文件名为 ./crazy_functions/总结word文档.py。该脚本是一个函数插件，提供了名为“总结word文档”的函数。该函数的主要功能是批量读取给定文件夹下的 Word 文档文件，并使用 GPT 模型生成对每个文件的概述和意见建议。其中涉及到了读取 Word 文档、使用 GPT 模型等操作，依赖于许多第三方库。该文件也提供了导入依赖的方法，使用该脚本需要安装依赖库 python-docx 和 pywin32。函数功能实现的过程中，使用了一些用于调试的变量（如 fast_debug），可在需要时设置为 True。该脚本文件也提供了对程序功能和贡献者的注释。

## [15/22] 程序概述: crazy_functions\批量总结PDF文档.py

该程序文件名为 `./crazy_functions\批量总结PDF文档.py`，主要实现了批量处理PDF文档的功能。具体实现了以下几个函数：

1. `is_paragraph_break(match)`：根据给定的匹配结果判断换行符是否表示段落分隔。
2. `normalize_text(text)`：通过将文本特殊符号转换为其基本形式来对文本进行归一化处理。
3. `clean_text(raw_text)`：对从 PDF 提取出的原始文本进行清洗和格式化处理。
4. `解析PDF(file_manifest, project_folder, top_p, temperature, chatbot, history, systemPromptTxt)`：对给定的PDF文件进行分析并生成相应的概述。
5. `批量总结PDF文档(txt, top_p, temperature, chatbot, history, systemPromptTxt, WEB_PORT)`：批量处理PDF文件，对其进行摘要生成。

其中，主要用到了第三方库`pymupdf`对PDF文件进行处理。程序通过调用`fitz.open`函数打开PDF文件，使用`page.get_text()`方法获取PDF文本内容。然后，使用`clean_text`函数对文本进行清洗和格式化处理，生成最终的摘要。最后，调用`write_results_to_file`函数将历史记录写入文件并输出。

## [16/22] 程序概述: crazy_functions\批量总结PDF文档pdfminer.py

这个程序文件名是./crazy_functions\批量总结PDF文档pdfminer.py，是一个用于批量读取PDF文件，解析其中的内容，并对其进行概括的程序。程序中引用了pdfminer和beautifulsoup4等Python库，读取PDF文件并将其转化为文本内容，然后利用GPT模型生成摘要语言，最终输出一个中文和英文的摘要。程序还有一些错误处理的代码，会输出错误信息。

## [17/22] 程序概述: crazy_functions\批量翻译PDF文档_多线程.py

这是一个 Python 程序文件，文件名为 `批量翻译PDF文档_多线程.py`，包含多个函数。主要功能是批量处理 PDF 文档，解析其中的文本，进行清洗和格式化处理，并使用 OpenAI 的 GPT 模型进行翻译。其中使用了多线程技术来提高程序的效率和并行度。

## [18/22] 程序概述: crazy_functions\生成函数注释.py

该程序文件名为./crazy_functions\生成函数注释.py。该文件包含两个函数，分别为`生成函数注释`和`批量生成函数注释`。

函数`生成函数注释`包含参数`file_manifest`、`project_folder`、`top_p`、`temperature`、`chatbot`、`history`和`systemPromptTxt`。其中，`file_manifest`为一个包含待处理文件路径的列表，`project_folder`表示项目文件夹路径，`top_p`和`temperature`是GPT模型参数，`chatbot`为与用户交互的聊天机器人，`history`记录聊天机器人与用户的历史记录，`systemPromptTxt`为聊天机器人发送信息前的提示语。`生成函数注释`通过读取文件内容，并调用GPT模型对文件中的所有函数生成注释，最后使用markdown表格输出结果。函数中还包含一些条件判断和计时器，以及调用其他自定义模块的函数。

函数`批量生成函数注释`包含参数`txt`、`top_p`、`temperature`、`chatbot`、`history`、`systemPromptTxt`和`WEB_PORT`。其中，`txt`表示用户输入的项目文件夹路径，其他参数含义与`生成函数注释`中相同。`批量生成函数注释`主要是通过解析项目文件夹，获取所有待处理文件的路径，并调用函数`生成函数注释`对每个文件进行处理，最终生成注释表格输出给用户。

## [19/22] 程序概述: crazy_functions\解析项目源代码.py

该程序文件包含了多个函数，用于解析不同类型的项目，如Python项目、C项目、Java项目等。其中，最核心的函数是`解析源代码()`，它会对给定的一组文件进行分析，并返回对应的结果。具体流程如下：

1. 遍历所有待分析的文件，对每个文件进行如下处理：

   1.1 从文件中读取代码内容，构造成一个字符串。

   1.2 构造一条GPT请求，向`predict_no_ui_but_counting_down()`函数发送请求，等待GPT回复。

   1.3 将GPT回复添加到机器人会话列表中，更新历史记录。

   1.4 如果不是快速调试模式，则等待2秒钟，继续分析下一个文件。

2. 如果所有文件都分析完成，则向机器人会话列表中添加一条新消息，提示用户整个分析过程已经结束。

3. 返回机器人会话列表和历史记录。

除此之外，该程序文件还定义了若干个函数，用于针对不同类型的项目进行解析。这些函数会按照不同的方式调用`解析源代码()`函数。例如，对于Python项目，只需要分析.py文件；对于C项目，需要同时分析.h和.cpp文件等。每个函数中都会首先根据给定的项目路径读取相应的文件，然后调用`解析源代码()`函数进行分析。

## [20/22] 程序概述: crazy_functions\读文章写摘要.py

该程序文件为一个名为“读文章写摘要”的Python函数，用于解析项目文件夹中的.tex文件，并使用GPT模型生成文章的中英文摘要。函数使用了request_llm.bridge_chatgpt和toolbox模块中的函数，并包含两个子函数：解析Paper和CatchException。函数参数包括txt，top_p，temperature，chatbot，history，systemPromptTxt和WEB_PORT。执行过程中函数首先清空历史，然后根据项目文件夹中的.tex文件列表，对每个文件调用解析Paper函数生成中文摘要，最后根据所有文件的中文摘要，调用GPT模型生成英文摘要。函数运行过程中会将结果写入文件并返回聊天机器人和历史记录。

## [21/22] 程序概述: crazy_functions\高级功能函数模板.py

该程序文件为一个高级功能函数模板，文件名为"./crazy_functions\高级功能函数模板.py"。

该文件导入了两个模块，分别是"request_llm.bridge_chatgpt"和"toolbox"。其中"request_llm.bridge_chatgpt"模块包含了一个函数"predict_no_ui_long_connection"，该函数用于请求GPT模型进行对话生成。"toolbox"模块包含了三个函数，分别是"catchException"、"report_exception"和"write_results_to_file"函数，这三个函数主要用于异常处理和日志记录等。

该文件定义了一个名为"高阶功能模板函数"的函数，并通过"decorator"装饰器将该函数装饰为一个异常处理函数，可以处理函数执行过程中出现的错误。该函数的作用是生成历史事件查询的问题，并向用户询问历史中哪些事件发生在指定日期，并索要相关图片。在查询完所有日期后，该函数返回所有历史事件及其相关图片的列表。其中，该函数的输入参数包括：

1. txt: 一个字符串，表示当前消息的文本内容。
2. top_p: 一个浮点数，表示GPT模型生成文本时的"top_p"参数。
3. temperature: 一个浮点数，表示GPT模型生成文本时的"temperature"参数。
4. chatbot: 一个列表，表示当前对话的记录列表。
5. history: 一个列表，表示当前对话的历史记录列表。
6. systemPromptTxt: 一个字符串，表示当前对话的系统提示信息。
7. WEB_PORT: 一个整数，表示当前应用程序的WEB端口号。

该函数在执行过程中，会先清空历史记录，以免输入溢出。然后，它会循环5次，生成5个历史事件查询的问题，并向用户请求输入相关信息。每次询问不携带之前的询问历史。在生成每个问题时，该函数会向"chatbot"列表中添加一条消息记录，并设置该记录的初始状态为"[Local Message] waiting gpt response."。然后，该函数会调用"predict_no_ui_long_connection"函数向GPT模型请求生成一段文本，并将生成的文本作为回答。如果请求过程中出现异常，该函数会忽略异常。最后，该函数将问题和回答添加到"chatbot"列表和"history"列表中，并将"chatbot"和"history"列表作为函数的返回值返回。
>>>>>>> faffc59f517fc0906b43346324521b016a9affd4

