# Running Your Own Jupyter Environment
*Complete Setup Guide for Applied Biostatistics*

::::{div} hero-section
:::{div} hero-content

## Set Up Your Local Environment 💻

Follow these step-by-step instructions to install Anaconda Python, launch Jupyter notebooks, and install the course helper package on your computer.

**Perfect for:** Students who prefer working locally or need offline access to course materials.

:::
::::

---

## Why Use a Local Environment?

::::{grid} 1 1 2 2
:class-container: text-center
:gutter: 4

:::{grid-item-card} 🚀 Better Performance
:class-header: bg-primary text-white

Local installations typically run faster than cloud-based solutions and don't require internet connectivity for computation.
:::

:::{grid-item-card} 🔒 Data Privacy
:class-header: bg-success text-white

Keep your data and analyses completely private on your own machine without uploading to cloud services.
:::

:::{grid-item-card} 💾 No Storage Limits
:class-header: bg-info text-white

Work with large datasets without worrying about cloud storage quotas or session timeouts.
:::

:::{grid-item-card} 🛠️ Full Control
:class-header: bg-warning text-white

Install additional packages, customize your environment, and integrate with other local tools as needed.
:::

::::

---

## Installation Instructions by Operating System

Select your operating system below for detailed installation instructions:

::::{tab-set}

:::{tab-item} Windows 🪟
:sync: windows

### Step 1: Download Anaconda

1. Visit the [Anaconda website](https://www.anaconda.com/download)
2. Click **"Download"** under the Windows section
3. Choose the **64-bit installer** (recommended for most modern computers)
4. The download file will be named something like `Anaconda3-2024.02-1-Windows-x86_64.exe`

### Step 2: Install Anaconda

1. **Run the installer** by double-clicking the downloaded `.exe` file
2. Click **"Next"** on the welcome screen
3. **Accept the license agreement** and click "Next"
4. Choose **"Just Me (recommended)"** and click "Next"
5. **Keep the default installation location** (usually `C:\Users\YourName\anaconda3`)
6. **Important:** Check **"Add Anaconda3 to my PATH environment variable"** 
   - ⚠️ The installer warns against this, but it makes using conda much easier
7. Click **"Install"** and wait for completion (this may take 10-15 minutes)
8. Click **"Finish"** when installation is complete

### Step 3: Launch Jupyter

**Option 1: Using Anaconda Navigator (Recommended for beginners)**
1. Open **Anaconda Navigator** from the Start Menu
2. Click **"Launch"** under Jupyter Notebook
3. Your web browser will open with the Jupyter interface

**Option 2: Using Command Prompt**
1. Press `Win + R`, type `cmd`, and press Enter
2. Type `jupyter notebook` and press Enter
3. Your web browser will open with the Jupyter interface

### Step 4: Install Course Helper Package

In a new Jupyter notebook cell, run:
```python
!pip install applied-biostats-helper
```
You'll only need to do this once.
:::

:::{tab-item} macOS 🍎
:sync: macos

### Step 1: Download Anaconda

1. Visit the [Anaconda website](https://www.anaconda.com/download)
2. Click **"Download"** under the macOS section
3. Choose the appropriate installer for your Mac:
   - **Apple Silicon (M1/M2/M3):** 64-bit ARM installer
   - **Intel processors:** 64-bit Intel installer
4. The download file will be named something like `Anaconda3-2024.02-1-MacOSX-arm64.pkg`

### Step 2: Install Anaconda

1. **Run the installer** by double-clicking the downloaded `.pkg` file
2. Click **"Continue"** through the introduction screens
3. **Accept the license agreement**
4. **Select your installation location** (default is recommended)
5. Click **"Install"** and enter your password when prompted
6. Wait for installation to complete (this may take 10-15 minutes)
7. Click **"Close"** when installation is finished

### Step 3: Launch Jupyter

**Option 1: Using Anaconda Navigator (Recommended for beginners)**
1. Open **Anaconda Navigator** from Applications or Spotlight search
2. Click **"Launch"** under Jupyter Notebook
3. Your web browser will open with the Jupyter interface

**Option 2: Using Terminal**
1. Open **Terminal** (Cmd + Space, type "Terminal")
2. Type `jupyter notebook` and press Enter
3. Your web browser will open with the Jupyter interface

### Step 4: Install Course Helper Package

In a new Jupyter notebook cell, run:
```python
!pip install applied-biostats-helper
```
You'll only need to do this once.

**Troubleshooting for macOS:**
- If you get a "command not found" error, you may need to add conda to your PATH:
  ```bash
  echo 'export PATH="$HOME/anaconda3/bin:$PATH"' >> ~/.zshrc
  source ~/.zshrc
  ```

:::

:::{tab-item} Linux 🐧
:sync: linux

### Step 1: Download Anaconda

1. Visit the [Anaconda website](https://www.anaconda.com/download)
2. Click **"Download"** under the Linux section
3. Choose the **64-bit (x86) installer**
4. The download file will be named something like `Anaconda3-2024.02-1-Linux-x86_64.sh`

### Step 2: Install Anaconda

1. **Open a terminal** (Ctrl + Alt + T)
2. **Navigate to your downloads folder:**
   ```bash
   cd ~/Downloads
   ```
3. **Make the installer executable:**
   ```bash
   chmod +x Anaconda3-2024.02-1-Linux-x86_64.sh
   ```
4. **Run the installer:**
   ```bash
   ./Anaconda3-2024.02-1-Linux-x86_64.sh
   ```
5. **Follow the prompts:**
   - Press Enter to review the license
   - Type "yes" to accept the license
   - Press Enter to confirm the installation location (default recommended)
   - Type "yes" when asked to initialize Anaconda3
6. **Restart your terminal** or run:
   ```bash
   source ~/.bashrc
   ```

### Step 3: Launch Jupyter

**Option 1: Using Anaconda Navigator**
1. Type `anaconda-navigator` in terminal
2. Click **"Launch"** under Jupyter Notebook
3. Your web browser will open with the Jupyter interface

**Option 2: Using Terminal (Recommended)**
1. Open a new terminal
2. Type `jupyter notebook` and press Enter
3. Your web browser will open with the Jupyter interface

### Step 4: Install Course Helper Package

In a new Jupyter notebook cell, run:
```python
!pip install applied-biostats-helper
```
You'll only need to do this once.

**Troubleshooting for Linux:**
- If conda commands don't work, ensure your PATH is set correctly:
  ```bash
  echo 'export PATH="$HOME/anaconda3/bin:$PATH"' >> ~/.bashrc
  source ~/.bashrc
  ```

:::

::::

---

## Troubleshooting Common Issues

::::{dropdown} **Problem:** "conda: command not found" or "jupyter: command not found"
**Solution:** The installation directory isn't in your system PATH.

**Windows:**
- Restart your command prompt or computer
- If still not working, manually add `C:\Users\YourName\anaconda3\Scripts` to your PATH

**macOS/Linux:**
```bash
echo 'export PATH="$HOME/anaconda3/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```
::::

::::{dropdown} **Problem:** Jupyter opens in the wrong directory
**Solution:** Navigate to your desired folder before launching Jupyter.

```bash
cd /path/to/your/course/folder
jupyter notebook
```
::::

::::{dropdown} **Problem:** Package installation fails with permission errors
**Solution:** Use the `--user` flag to install packages in your user directory.

```bash
pip install --user git+https://github.com/DamLabResources/applied-biostats-helper.git
```
::::

::::{dropdown} **Problem:** Browser doesn't open automatically
**Solution:** Jupyter will display a URL in the terminal. Copy and paste it into your web browser.

Look for something like: `http://localhost:8888/?token=abc123...`
::::

---


*Setup Guide • Last Updated: 2025*
