@echo off
echo Installing required packages...
python -m venv cocoa_env
call cocoa_env\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
echo Installation complete! Run run.bat to start the app.
pause