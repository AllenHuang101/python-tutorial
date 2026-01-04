# Python Tutorial

## 專案環境還原

### 前置需求

- Python 3.12 或更高版本
- uv 套件管理工具

### 安裝步驟

1. **安裝 uv**（如果尚未安裝）

   ```bash
   pip install uv
   ```

2. **還原環境**

   ```bash
   uv sync
   ```

   此指令會自動：

   - 建立虛擬環境（`.venv`）
   - 安裝 `pyproject.toml` 和 `uv.lock` 中指定的所有相依套件

3. **啟動虛擬環境**

   - Windows PowerShell：
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   - Windows CMD：
     ```cmd
     .venv\Scripts\activate.bat
     ```
   - Linux/macOS：
     ```bash
     source .venv/bin/activate
     ```
