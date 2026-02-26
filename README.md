# Maya_Learn_Helper

- Nonebot2插件，用于qq官方群聊机器人
- 目标
  - [ ] maya api的查询

---

## 环境部署

- `uv sync`拉取依赖
- 根据`.env.example` 建立 `.env.prod` 文件并在其中填写**appid**、**secret**等机器人信息
- `uv run nb run`或`uv run nb run --reload`启动机器人

---

## 命令说明

- `/echo`
  - 内置插件，回显消息
- `/random [max-number]`
  - 生成以max-number为上限的随机正数，如`/random 100`

---

## 开发说明

- 提交代码前可使用`pyright`/`ruff`进行代码检查与格式化
  ```shell
  uv run ruff check .
  uv run ruff format .
  uv run pyright
  # 或 uv run python -m pyright
  ```