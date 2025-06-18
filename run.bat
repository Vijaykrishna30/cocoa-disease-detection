@echo off
echo Activating virtual environment...
python -m venv cocoa_env
call cocoa_env\Scripts\activate

echo Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt

echo Starting Cocoa Disease Detector...
streamlit run app.py
pause