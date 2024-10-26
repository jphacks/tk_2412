# ReadingAssistant

## 1. 目的
该项目旨在提供一个智能阅读助手，帮助用户提高阅读效率和理解能力。通过分析用户的阅读习惯和情感状态，ReadingAssistant 能够提供个性化的建议和反馈，促进更高效的学习和信息吸收。

## 2. 主要技术
该项目主要使用以下技术：
- **Python**: 作为主要编程语言，用于实现后端逻辑。
- **Reflex**: 一个用于构建现代 web 应用的框架，简化了前端和后端的集成。
- **Animate.css**: 用于增强用户界面的动画效果。
  
## 3. 开发进度
- [X] 基础的应用框架搭建
- [X] 页面导航和状态管理
- [ ] 完善情感状态和段落状态的管理
- [ ] 添加多用户
- [ ] 集成情感分析 API
- [ ] 优化用户界面和用户体验

## 4. 实现细节
### 文件结构
```text
ReadingAssistant/
├── init.py # 包初始化文件
├── ReadingAssistant.py # 主应用程序文件
├── Page/
│ ├── Index.py # 主页面逻辑
│ └── pycache/ # 编译的缓存文件
├── State/
│ ├── EmotionState.py # 情感状态管理
│ ├── ParagraphState.py # 段落状态管理
│ ├── FormRadioState.py # 表单单选状态管理
│ └── QuestionState.py # 问题状态管理
├── Model/
│ └── EmotionModel.py # 情感模型
├── API/
│ └── EmotionAPI.py # 情感 API 接口
└── Utils/
└── question_prompt_experiment.py # 工具函数
```

### 每个文件的功能
- `ReadingAssistant.py`: 启动应用并配置页面和样式。
- `Page/Index.py`: 定义主页面的逻辑和布局。
- `State/`: 包含管理不同状态的模块，如情感状态和段落状态。
- `Model/EmotionModel.py`: 实现情感分析模型。
- `API/EmotionAPI.py`: 提供与情感分析相关的 API 接口。
- `Utils/question_prompt_experiment.py`: 存放实用工具函数，辅助其他模块的功能。

## 5. 亮点
- **个性化体验**: 根据用户的情感和阅读状态调整建议，提升学习效果。
- **模块化设计**: 清晰的文件结构和模块化代码，使得开发和维护变得简单。
- **良好的用户体验**: 利用动画和状态管理提高用户互动性，增强应用的吸引力。

